Installation
============

The CLI package requires WP-CLI and PHP 7.4 or newer. Use it with an active
WP fail2ban plugin from the 5.6 line or version 6.3.0 or newer. The
:external+wp-fail2ban:ref:`6.3 plugin requirements <installation_requirements>`
apply when running that version of the plugin.

Install the package through WP-CLI under the account that will run the commands.

.. code-block:: console

   $ wp package install wp-fail2ban/wp-fail2ban-cli

From the WordPress installation directory, run these commands to list the
available subcommands and confirm that WP fail2ban has loaded.

.. code-block:: console

   $ wp fail2ban
   $ wp fail2ban status

Use WP-CLI's global ``--path`` option to select a different WordPress
installation. On multisite, use ``--url`` to select the site.

If WP-CLI loads the package but the plugin is unavailable, a bare
``wp fail2ban`` exits with :ref:`status 7 <cli-exit-status>` and reports one of
these messages.

.. list-table::
   :header-rows: 1

   * - Message
     - What to check
   * - ``WP fail2ban is not active.``
     - Confirm that WP fail2ban is active and loaded for the selected site.
   * - ``WP fail2ban 6.3 or newer is required.``
     - Check the active plugin version. The 5.6 line is also supported.
