from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .path import build_react_pathes


@api_view(['GET'])
def build_react_pathes_view(request, *args, **kwargs):
    return Response(build_react_pathes())


class BaseAPIViewList(APIView):
    """List all models that should be shown.
    Use base class to avoid code duplication"""
    def get(self, request, *args, **kwargs):
        version = kwargs.get('version')

        if version == 'v1':
            return self.get_v1(request, *args, **kwargs)

        # If there is unsupported version
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_v1(self, request, *args, **kwargs):
        objects = self.get_queryset()

        if not objects:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = self.serializer(objects, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        # Using just queryset evaluate that and the result will be cached
        return self.model.objects.list()
