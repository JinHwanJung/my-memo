from rest_framework.response import Response
from rest_framework.views import APIView

from study.serializers import AddSerializer


class AddAPI(APIView):
    def post(self, request):
        serializer = AddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.data['number1'] + serializer.data['number2']
        return Response(data={'result': result})

