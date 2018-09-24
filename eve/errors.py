from eve.exceptions import ResponseMappingError


def response_map_error(error):
    raise ResponseMappingError('Missed the mapping of custom response?')