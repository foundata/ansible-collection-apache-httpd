# SPDX-FileCopyrightText: foundata GmbH <https://foundata.com>
# SPDX-License-Identifier: GPL-3.0-or-later

"""Keep an Apache response in flight until the verifier has applied the reload."""

import socket
import sys
import time
from http.client import HTTPConnection
from pathlib import Path
from tempfile import NamedTemporaryFile


def main(document_root, barrier):
    # Keep the body larger than Apache's TCP send buffer. Once the client pauses,
    # the worker cannot finish the transfer until after the verifier releases it.
    size = 32 * 1024 * 1024
    with NamedTemporaryFile(dir=document_root, prefix="molecule-transfer-") as asset:
        asset.truncate(size)
        path = Path(asset.name)
        path.chmod(0o644)
        connection = HTTPConnection("127.0.0.1", timeout=30)
        try:
            connection.connect()
            connection.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
            connection.request("GET", f"/{path.name}", headers={"Host": "example.com"})
            response = connection.getresponse()
            if response.status != 200 or response.read(1) != b"\0":
                raise ValueError("Apache did not start serving the test asset")
            (barrier / "ready").touch()
            deadline = time.monotonic() + 120
            while not (barrier / "resume").exists():
                if time.monotonic() >= deadline:
                    raise TimeoutError(
                        "The verification play did not release the client"
                    )
                time.sleep(0.1)
            received = 1
            while chunk := response.read(65536):
                received += len(chunk)
            if received != size:
                raise ValueError(
                    f"Reload interrupted transfer at {received}/{size} bytes"
                )
        finally:
            connection.close()


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
