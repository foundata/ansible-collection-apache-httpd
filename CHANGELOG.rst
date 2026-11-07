=======================================================
foundata.apache\_httpd Ansible collection Release Notes
=======================================================

.. contents:: Topics

v1.4.0
======

Minor Changes
-------------

- Add role-prefixed handler topics and use them for internal notifications. Retain the previous topics as migration aliases until version 2.0.0.
- Add the handler topic run_apache_httpd_reload_apache_httpd as the replacement for "run_apache_httpd: reload apache_httpd.service".
- Add the handler topic run_apache_httpd_reload_systemd_daemon as the replacement for "run_apache_httpd: systemd daemon-reload".
- Add the handler topic run_apache_httpd_restart_apache_httpd as the replacement for "run_apache_httpd: restart apache_httpd.service".
- Add the handler topic run_apache_httpd_validate_configuration as the replacement for "run_apache_httpd: validate configuration".

Bugfixes
--------

- Check the minimum ansible-core version before gathering role facts so unsupported versions fail with the intended diagnostic.
- Limit automatic fact gathering to each role's declared subsets while retaining missing-fact recovery and reuse of cached facts.
- The declared ansible-core minimum is corrected from 2.16 to 2.19. The roles write Jinja's own filters and tests as ``ansible.builtin.<name>``, which ansible-core resolves from 2.19 only; on 2.16 to 2.18 every run failed at the first such expression, so no working installation is affected.

v1.3.0
======

Release Summary
---------------

Release Date: 2026-08-28

Maintenance release.

Minor Changes
-------------

- ``run`` - Improve Ansible compatibility for roles and collections used in the wild by giving every loop in the role a private, purpose-specific loop variable derived from the role's public variable prefix (``__run_apache_httpd_*_item``) instead of ``item``. This avoids rebinding a caller's ``item`` when role parameters reference it, such as when the role itself is included from a loop, and makes the role behave more robustly across common Ansible usage patterns.

v1.2.1
======

Release Summary
---------------

Release Date: 2026-08-13

Bugfix release.

Bugfixes
--------

- ``run`` - the uninstall sweep only treats files as role-owned when they contain the ownership marker as an exact line. Previously the marker was matched as a substring (and with regex semantics), so a foreign file merely mentioning the marker text (e.g. quoted in a comment) was deleted.
- boolean role arguments are now coerced with ``ansible.builtin.bool`` in every conditional. String values, as delivered by ``-e var=false`` command line extra-vars, were evaluated by truthiness before, so ``"false"`` enabled the gated behavior instead of disabling it.

v1.2.0
======

Release Summary
---------------

Release Date: 2026-07-30

Maintenance and bugfix release.

Minor Changes
-------------

- The Molecule ``default`` scenario now selects the test backend per platform via a ``type`` key: ``podman`` (container, the default when omitted) or ``libvirt`` (QEMU/KVM virtual machine from a vendor cloud image via a session libvirt daemon, without root privileges). VM platforms allow tests containers cannot cover; commented ``libvirt`` alternates for every platform are included in ``molecule.yml``. ``molecule login`` now works through a per-instance login command for both backends. See ``extensions/molecule/README.md`` for requirements and usage.

Bugfixes
--------

- The comment written into neutralized distribution config files contained a stray double quote in the Debian hint (``dpkg -S '<file>'"``), so the suggested command could not be copied and pasted as-is. The quote is removed.
- ``run`` role - A ``run_apache_httpd_vhosts_config`` entry without ``enabled: true`` no longer fails the run: the enable/disable task passed ``src`` together with ``state: absent``, which ansible-core rejects. The options are now omitted when the symlink is being removed.
- ``run`` role - Documentation: reinstalling the distribution's Apache on Debian/Ubuntu after ``run_apache_httpd_state: absent`` requires ``apt purge`` first; this dpkg conffile behavior is now documented in the ``run_apache_httpd_state`` description.
- ``run`` role - Duplicate ``name`` values in ``run_apache_httpd_vhosts_config`` now cause a validation error. Entries sharing a name wrote the same ``<name>.conf`` file with different content on every run, producing order-dependent results and permanent non-idempotence. Uniqueness was already documented but not enforced.
- ``run`` role - Platform-specific task files are now guaranteed to run before the shared default tasks. The former single include loop did not preserve that order with several platforms in one play: Ansible batches the includes across hosts and the insertion order depends on when results arrive (non-deterministic), so default tasks could run before platform-specific ones. The includes are now two sequential tasks, which is a hard ordering barrier.
- ``run`` role - Stale enabled-vhost symlinks are now reaped. The unmanaged-vhost cleanup used ``find`` with ``file_type: "file"``, which skipped the symlinks in the vhosts-enabled directory; removing a vhost from ``run_apache_httpd_vhosts_config`` could leave the old enabled vhost active. The cleanup now matches symlinks too.
- ``run`` role - Stale role-managed (symlink-type) module configs are now removed even when ``run_apache_httpd_modules_enabled`` is emptied. The cleanup was gated on there being enabled symlink modules, so emptying the list (after modules had previously been managed) left the old module symlinks enabled. The cleanup now runs whenever ``run_apache_httpd_modules_disable_unmanaged`` is true and only ever removes files whose name is part of the role's module map (``__run_apache_httpd_modules_map_resources``, symlink type).
- ``run`` role - The documentation of the ``unmanaged`` service state falsely claimed the service "will not start at boot". The role leaves the service completely alone in this state: both the running state and the boot (enablement) state stay exactly as they are. The description now documents the real behavior.
- ``run`` role - The self-signed (snakeoil) certificate pair for the HTTPS catch-all VirtualHost is now regenerated when either half is missing. Before, only the certificate was checked: an existing certificate with a missing key was left as-is, and Apache refused to start over the broken ``SSLCertificateKeyFile`` reference in the catch-all VirtualHost.
- ``run`` role - The service restart and reload handlers were gated only on ``run_apache_httpd_service_state != 'unmanaged'``. With ``run_apache_httpd_service_state: "disabled"`` a configuration change still notified them and, because handlers run after the service management tasks, the restart started the just-stopped unit again (and the reload failed on the inactive unit), leaving a running service although the declared state is stopped. The handlers are now gated on ``run_apache_httpd_service_state in ['enabled', 'running']``.
- ``run`` role - Uninstall (``run_apache_httpd_state: absent``) now removes managed vhost configs by absolute path from both the vhosts-available and vhosts-enabled directories. The removal list was built from bare filenames (e.g. ``example.com.conf``) that did not resolve, so on Debian/SUSE — where the vhost directories are intentionally kept — managed vhost files and their enabled symlinks were left behind after uninstall.
- ``run`` role - Uninstall now removes historical leftovers it previously could not see: vhost config files carry an ownership marker and both vhost directories are swept for it (covering vhosts renamed or de-listed since deployment on Debian/SUSE, where the directories are kept), the role-managed module symlinks are removed from ``mods-enabled`` on Debian, and the SUSE ``/etc/sysconfig/apache2`` edits (``APACHE_MODULES`` and the cleared ``APACHE_*`` values) are restored from a copy of the pre-role file saved before the first edit.

v1.1.0
======

Release Summary
---------------

Release Date: 2026-05-11

Maintenance release.

Minor Changes
-------------

- Added Fedora 44 as supported platform for all collection roles and Molecule test scenarios.
- Added Ubuntu 26.04 LTS (Resolute Raccoon) as supported platform for all collection roles and Molecule test scenarios.

Removed Features (previously deprecated)
----------------------------------------

- Removed Fedora 42 support (End of Life, EOL) from collection roles and Molecule scenarios. The collection may still work on Fedora 42, but no testing or bugfixes will be provided. A warning will be displayed when used on unsupported platforms.

v1.0.0
======

Release Summary
---------------

Release Date: 2026-05-05

First public release, providing all functionality and files.
