from rest_framework.response import Response
from rest_framework.views import APIView


class TestApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = [{"id": 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        return Response(data)
