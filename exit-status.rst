.. _cli-exit-status:

Exit status
===========

Scripts can use the process exit status to distinguish failures reported by
the package. Error messages go to standard error. Command output can still be
present on standard output when the exit status is non-zero.

.. list-table::
   :header-rows: 1

   * - Status
     - Meaning
   * - 0
     - The command succeeded.
   * - 1
     - An unclassified error reached the package's error handler.
   * - 2
     - The invocation is invalid, such as a missing argument or incompatible
       flags.
   * - 3
     - A named item, such as a configuration setting or report kind, is
       unknown.
   * - 4
     - A supplied value failed validation.
   * - 5
     - A well-formed identifier refers to a missing item, such as a site or
       an event record.
   * - 6
     - An attempted write failed.
   * - 7
     - The command requires an active or compatible plugin, a different
       edition, or an available dependency.
   * - 8
     - A value is controlled by another configuration source, or the supplied
       selectors conflict.
   * - 9
     - A diagnostic completed with at least one critical result.

WP-CLI can reject an invocation before it reaches a command and return its
own status.