from rest_framework.response import Response
from rest_framework import status


def project404Handler(request, exception):
    print("404 error", exception)

    return Response({"Message": "Resource not found"}, status.HTTP_404_NOT_FOUND)
