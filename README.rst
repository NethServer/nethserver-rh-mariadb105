========================
nethserver-rh-mariadb105
========================

MariaDB 10.5 comes from SCL, similar package https://www.softwarecollections.org/en/scls/rhscl/rh-mariadb103/

This package doesn't start any MariaDB instance by default.

Database instances
==================

Each software can create its own MariaDB instance by:

- creating a service key like `rh-mariadb105-mariadb@<name>`
- adding a fragment to `/etc/opt/rh/rh-mariadb105/my.cnf.d/mariadb-server.cnf` template
- creating a directory where to store files like: ::

    mkdir -p /var/opt/rh/rh-mariadb105/lib/mysql-<name>
    chown mysql:mysql /var/opt/rh/rh-mariadb105/lib/mysql-<name>

Backup
======

Backup and restore is not implemented system-wide: every application
should provide its own scripts.

Backup actions must be linked inside the ``pre-backup-data`` event.
Example of backup action: ::

  #!/bin/bash

  scl enable rh-mariadb105 -- mysqldump --socket /var/lib/mysql/<name>-mysql.sock <name> > /var/lib/nethserver/<name>/<name>.sql

Restore actions must be linked inside the ``post-restore-data`` event.
Example of restore action: ::

  #!/bin/bash

  ...

