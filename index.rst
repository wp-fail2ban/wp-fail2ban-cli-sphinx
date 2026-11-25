===============
WP fail2ban CLI
===============

The ``wp-fail2ban/wp-fail2ban-cli`` package registers the ``wp fail2ban``
parent command before WordPress loads. The active WP fail2ban plugin adds the
subcommands when WordPress loads. Run ``wp help fail2ban`` to browse the
commands on your installation, or ``wp help fail2ban status`` for help with
an individual command.

.. toctree::
   :caption: Manual
   :maxdepth: 2

   installation
   exit-status

