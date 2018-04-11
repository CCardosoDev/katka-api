from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from ..exceptions import BadRequest


class BroadExceptionView(APIView):
    """
    View for testing how Exceptions are handled.
    """
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        raise Exception('Any exception')


class IndexView(APIView):
    """
    Raise an exception that should be logged.
    Can be used to see if exceptions are handled correctly.
    """
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        return Response({
            'any': reverse('error:any', request=request),
            'silent': reverse('error:silent', request=request)
        })


class SilentExceptionView(APIView):
    """
    Raise an exception that should be logged.
    Can be used to see if exceptions are handled correctly.
    """
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        raise BadRequest('No log exception')
