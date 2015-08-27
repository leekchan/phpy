try:
    import simplejson as json
except ImportError:
    import json
from subprocess import Popen, PIPE
from exceptions import *


class PHP:
    def __init__(self, file_path):
        self.file_path = file_path

    def __escape(self, string):
        return string.replace('\\', '\\\\').replace("'", "\\'")

    def __quote(self, arguments):
        for arg in arguments:
            if isinstance(arg, basestring):
                if isinstance(arg, unicode):
                    arg = arg.encode('utf-8')
                yield '\'%s\'' % self.__escape(arg)
            elif arg is None:
                yield 'NULL'
            else:
                yield str(arg)

    def __join_arguments(self, arguments):
        if arguments:
            return ','.join(self.__quote(arguments))
        else:
            return ''

    def __call_function(self, function_name, arguments):
        if (type(arguments)) != list and arguments:
            raise InvalidType
        p = Popen('php', stdin=PIPE, stdout=PIPE, stderr=PIPE)
        print >>p.stdin, '<?php '
        print >>p.stdin, 'include \'%s\';' % self.__escape(self.file_path)
        print >>p.stdin, '%s(%s);' % (function_name,
                                    self.__join_arguments(arguments))
        p.stdin.close()
        result = p.stdout.read()
        if result.find('include(): Failed opening') > 0:
            raise PHPFileDoesNotExist(result)
        if result.find('Warning: ') > 0 and result.find('on line ') > 0:
            raise PHPWarning(result)

        return result

    def get_raw(self, function_name, arguments=None):
        return self.__call_function(function_name, arguments)

    def get_dict(self, function_name, arguments=None):
        return json.loads(self.__call_function(function_name, arguments))
