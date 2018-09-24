# -*- coding: utf-8 -*-

"""
    eve.exceptions
    ~~~~~~~~~~~~~~

    This module implements Eve custom exceptions.

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""


class ConfigException(Exception):
    """ Raised when errors are found in the configuration settings (usually
    `settings.py`).
    """
    pass


class SchemaException(ConfigException):
    """ Raised when errors are found in a field schema definition """
    pass

class ResponseMappingError(Exception):
    ''' Raised when the custom response mapping is not defined but requests for a custom response'''
    pass