from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import status

from .serializers import UserSerializer


@api_view(["POST"])
def login(request):
    return Response({"token": "your-token-here"})


@api_view(["POST"])
def sign_up(request):
    serializer = UserSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()

    user = User.objects.get(username=serializer.data["username"])

    print(serializer.data)
    return Response({"message": "Sign up successful!"})


@api_view(["GET"])
def get_profile_information(request):
    return Response({"message": "Profile information here"})
