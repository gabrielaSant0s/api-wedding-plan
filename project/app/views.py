from rest_framework.views import APIView
from rest_framework.response import Response

class ApiView(APIView):
    def get(self, request):
        data = ['object1', 'object2', 'object3']
        return Response(data)
