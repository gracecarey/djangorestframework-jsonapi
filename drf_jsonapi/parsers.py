from rest_framework import parsers
from rest_framework.exceptions import ParseError
from django.conf import settings
import json
from django.utils import six

class JSONApiParser(parsers.BaseParser):
    """
    Parses JSON-serialized data.
    """
    media_type = 'application/vnd.api+json'
    # renderer_class = renderers.JSONRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return json.loads(data)
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))
