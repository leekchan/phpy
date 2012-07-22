class PHPFileDoesNotExist(Exception):
    """ The target PHP file does not exist. """
    def __init__(self, warnings):
        self.warnings = warnings

    def __str__(self):
        return 'The target PHP file does not exist. - %s' % self.warnings


class PHPWarning(Exception):
    """ There is a warning in execution. """
    def __init__(self, warnings):
        self.warnings = warnings

    def __str__(self):
        return '%s' % self.warnings


class InvalidType(Exception):
    """ Invalid type. """
    def __str__(self):
        return 'Ony list type is permitted.'
