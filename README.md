# Ansible collection: `foundata.apache_httpd`

This repository contains the `foundata.apache_httpd` Ansible Collection.

It provides resources to manage and use the
[Apache HTTP server](https://httpd.apache.org/), a HTTP web server, reverse
proxy, load balancer.


<!-- Preserve the existing centered project banner. -->
<!-- rumdl-disable MD033 -->

<div align="center" id="project-readme-header">
<br>
<br>

**⭐ Found this useful? Support open-source and star this project:**

[![GitHub repository](https://img.shields.io/github/stars/foundata/ansible-collection-apache-httpd.svg)](https://github.com/foundata/ansible-collection-apache-httpd)

<br>
</div>

<!-- rumdl-enable MD033 -->



## Table of contents<a id="toc"></a>

- [Included content](#content)
- [Dependencies](#dependencies)
- [Licensing, copyright](#licensing-copyright)
- [Author information](#author-information)



## Included content<a id="content"></a>

### Role: `foundata.apache_httpd.run`

The primary role in this collection to configure and maintain Apache HTTPD,
including virtual hosts (vHosts) and related configuration.
[Its `README.md`](./roles/run/README.md) covers configuration, usage examples,
and more:

<!-- ANSIBLE DOCSMITH TOC-FULL run START -->
- [Ansible role: `foundata.apache_httpd.run`](roles/run/README.md#ansible-role-foundataapache_httpdrun)
  - [Table of contents](roles/run/README.md#toc)
  - [Features](roles/run/README.md#features)
  - [Example playbooks, using this role](roles/run/README.md#examples)
  - [Supported tags](roles/run/README.md#tags)
  - [Role variables](roles/run/README.md#variables)
    - [`run_apache_httpd_state`](roles/run/README.md#variable-run_apache_httpd_state)
    - [`run_apache_httpd_autoupgrade`](roles/run/README.md#variable-run_apache_httpd_autoupgrade)
    - [`run_apache_httpd_service_state`](roles/run/README.md#variable-run_apache_httpd_service_state)
    - [`run_apache_httpd_mpm`](roles/run/README.md#variable-run_apache_httpd_mpm)
    - [`run_apache_httpd_vhosts_default_manage`](roles/run/README.md#variable-run_apache_httpd_vhosts_default_manage)
    - [`run_apache_httpd_main_config_block`](roles/run/README.md#variable-run_apache_httpd_main_config_block)
    - [`run_apache_httpd_main_config_baseline_manage`](roles/run/README.md#variable-run_apache_httpd_main_config_baseline_manage)
    - [`run_apache_httpd_vhosts_config`](roles/run/README.md#variable-run_apache_httpd_vhosts_config)
      - [`run_apache_httpd_vhosts_config['name']`](roles/run/README.md#variable-run_apache_httpd_vhosts_config-sub-name)
      - [`run_apache_httpd_vhosts_config['enabled']`](roles/run/README.md#variable-run_apache_httpd_vhosts_config-sub-enabled)
      - [`run_apache_httpd_vhosts_config['content']`](roles/run/README.md#variable-run_apache_httpd_vhosts_config-sub-content)
    - [`run_apache_httpd_vhosts_delete_unmanaged`](roles/run/README.md#variable-run_apache_httpd_vhosts_delete_unmanaged)
    - [`run_apache_httpd_modules_enabled`](roles/run/README.md#variable-run_apache_httpd_modules_enabled)
    - [`run_apache_httpd_modules_disable_unmanaged`](roles/run/README.md#variable-run_apache_httpd_modules_disable_unmanaged)
    - [`run_apache_httpd_snippets_manage`](roles/run/README.md#variable-run_apache_httpd_snippets_manage)
    - [`run_apache_httpd_snippet_settings`](roles/run/README.md#variable-run_apache_httpd_snippet_settings)
      - [`run_apache_httpd_snippet_settings['hsts']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-hsts)
        - [`run_apache_httpd_snippet_settings['hsts']['max_age']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-hsts-sub-max_age)
        - [`run_apache_httpd_snippet_settings['hsts']['include_subdomains']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-hsts-sub-include_subdomains)
        - [`run_apache_httpd_snippet_settings['hsts']['preload']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-hsts-sub-preload)
      - [`run_apache_httpd_snippet_settings['php-fpm']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-php-fpm)
        - [`run_apache_httpd_snippet_settings['php-fpm']['type']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-php-fpm-sub-type)
        - [`run_apache_httpd_snippet_settings['php-fpm']['socket']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-php-fpm-sub-socket)
        - [`run_apache_httpd_snippet_settings['php-fpm']['tcp_host']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-php-fpm-sub-tcp_host)
        - [`run_apache_httpd_snippet_settings['php-fpm']['tcp_port']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-php-fpm-sub-tcp_port)
      - [`run_apache_httpd_snippet_settings['tls-baseline']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-tls-baseline)
        - [`run_apache_httpd_snippet_settings['tls-baseline']['dhparam_path']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-tls-baseline-sub-dhparam_path)
        - [`run_apache_httpd_snippet_settings['tls-baseline']['ecdh_curves']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-tls-baseline-sub-ecdh_curves)
        - [`run_apache_httpd_snippet_settings['tls-baseline']['resolvers']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-tls-baseline-sub-resolvers)
        - [`run_apache_httpd_snippet_settings['tls-baseline']['resolver_timeout']`](roles/run/README.md#variable-run_apache_httpd_snippet_settings-sub-tls-baseline-sub-resolver_timeout)
    - [`run_apache_httpd_snippets_delete_unmanaged`](roles/run/README.md#variable-run_apache_httpd_snippets_delete_unmanaged)
  - [Dependencies](roles/run/README.md#dependencies)
  - [Compatibility](roles/run/README.md#compatibility)
  - [External requirements](roles/run/README.md#requirements)
<!-- ANSIBLE DOCSMITH TOC-FULL run END -->



## Dependencies<a id="dependencies"></a>

See `dependencies` in [`galaxy.yml`](./galaxy.yml).



## Licensing, copyright<a id="licensing-copyright"></a>

<!--REUSE-IgnoreStart-->
<!-- rumdl-disable MD034 --><!-- should match SPDX-PackageSupplier -->
Copyright (c) 2026, [foundata GmbH](https://foundata.com/)
(https://foundata.com)
<!-- rumdl-enable MD034 -->

This project is licensed under the GNU General Public License v3.0 or later
(SPDX-License-Identifier: `GPL-3.0-or-later`), see
[`LICENSES/GPL-3.0-or-later.txt`](./LICENSES/GPL-3.0-or-later.txt) for the full
text.

The [`REUSE.toml`](./REUSE.toml) file provides detailed licensing and copyright
information in a human- and machine-readable format. This includes parts that
may be subject to different licensing or usage terms, such as third-party
components. The repository conforms to the
[REUSE specification](https://reuse.software/spec/). You can use
[`reuse spdx`](https://reuse.readthedocs.io/en/latest/readme.html#cli) to create
an
[SPDX software bill of materials (SBOM)](https://en.wikipedia.org/wiki/Software_Package_Data_Exchange).
<!--REUSE-IgnoreEnd-->

[![REUSE status](https://api.reuse.software/badge/github.com/foundata/ansible-collection-apache-httpd)](https://api.reuse.software/info/github.com/foundata/ansible-collection-apache-httpd)



### Trademarks<a id="trademarks"></a>

Third-party trademarks used in this repository:

- Ansible®, CentOS®, Fedora®, Red Hat® and RHEL® are trademarks of Red Hat, LLC,
  registered in the United States and other countries.
- Debian® is a trademark of Software in the Public Interest, Inc., registered in
  Germany and the United States.
- Linux® is a trademark of Linus Torvalds, registered in Germany, the European
  Union and the United States.
- openSUSE® is a trademark of SUSE LLC or its affiliates, registered in the
  European Union and the United States.
- SUSE® is a trademark of SUSE LLC or its affiliates, registered in Germany, the
  European Union and the United States.
- Ubuntu® is a trademark of Canonical Ltd., registered in Germany, the European
  Union and the United States.

Their use here is purely descriptive and does not imply any affiliation with or
endorsement by the trademark holders.

Own and licensed trademarks used in this repository:

- foundata® is a trademark of [IPAM GmbH](https://ipam-services.com/),
  registered in Germany and the European Union, licensed to
  [foundata GmbH](https://foundata.com/).


## Author information<a id="author-information"></a>

This [project](https://foundata.com/en/projects/) was created and is maintained
by [foundata](https://foundata.com/).

Initially based on an
[Ansible skeleton](https://foundata.com/en/projects/ansible-skeletons/)
developed by [foundata](https://foundata.com/).
