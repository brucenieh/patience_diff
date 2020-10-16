def build_dependency_list(deps, version_prefix=''):
    """Build a list of dependency specifiers from a dependency map.

    This can be used along with :py:data:`package_dependencies`,
    :py:data:`npm_dependencies`, or other dependency dictionaries to build a
    list of dependency specifiers for use on the command line or in
    :file:`setup.py`.

    Args:
        deps (dict):
            A dictionary of dependencies.

    Returns:
        list of unicode:
        A list of dependency specifiers.
    """
    return sorted(
        [
            '%s%s%s' % (dep_name, version_prefix, dep_version)
            for dep_name, dep_version in deps.items()
        ],
        key=lambda s: s.lower())


def _dependency_message(message, prefix=''):
    """Utility function to print and track a dependency-related message.

    This will track that a message was printed, allowing us to determine if
    any messages were shown to the user.

    Args:
        message (unicode):
            The dependency-related message to display. This will be wrapped,
            but long strings (like paths) will not contain line breaks.

        prefix (unicode, optional):
            The prefix for the message. All text will be aligned after this.
    """
    sys.stderr.write('\n%s\n'
                     % textwrap.fill(message,
                                     initial_indent=prefix,
                                     subsequent_indent=' ' * len(prefix),
                                     break_long_words=False,
                                     break_on_hyphens=False))


def dependency_error(message):
    """Print a dependency error.

    This will track that a message was printed, allowing us to determine if
    any messages were shown to the user.

    Args:
        message (unicode):
            The dependency error to display. This will be wrapped, but long
            strings (like paths) will not contain line breaks.
    """
    global _dependency_error_count

    _dependency_message(message, prefix='ERROR: ')
    _dependency_error_count += 1


def dependency_warning(message):
    """Print a dependency warning.

    This will track that a message was printed, allowing us to determine if
    any messages were shown to the user.

    Args:
        message (unicode):
            The dependency warning to display. This will be wrapped, but long
            strings (like paths) will not contain line breaks.
    """
    global _dependency_warning_count

    _dependency_message(message, prefix='WARNING: ')
    _dependency_warning_count += 1


def fail_if_missing_dependencies():
    """Exit the process with an error if dependency messages were shown.

    If :py:func:`dependency_error` or :py:func:`dependency_warning` were
    called, this will print some help information with a link to the manual
    and then exit the process.
    """
    if _dependency_warning_count > 0 or _dependency_error_count > 0:
        from reviewboard import get_manual_url

        _dependency_message('Please see %s for help setting up Review Board.'
                            % get_manual_url())

        if _dependency_error_count > 0:
            sys.exit(1)
