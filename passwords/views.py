from rest_framework.views import Response, status
from rest_framework.views import APIView

from passwords.models import Password, PasswordCategory
from passwords.serializers import PasswordSerializer, PasswordCategorySerializer


class PasswordListAPIView(APIView):
    def get(self, request):
        passwords = Password.objects.all()
        serializer = PasswordSerializer(passwords, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordDetailAPIView(APIView):
    def get(self, request, id):
        try:
            password = Password.objects.get(pk=id)
            serializer = PasswordSerializer(password)

            return Response(serializer.data)
        except Password.DoesNotExist:
            return Response(
                {"message": "Password not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print("Error getting password by id", e)

            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, id):
        try:
            password = Password.objects.get(pk=id)
            serializer = PasswordSerializer(password, data=request.data)

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Password.DoesNotExist:
            return Response(
                {"message": "Password not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print("Error updating password", e)

            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, id):
        try:
            password = Password.objects.get(pk=id)
            password.delete()

            return Response(
                {"message": "Password deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Password.DoesNotExist:
            return Response(
                {"message": "Password not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print("Error deleting password", e)

            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PasswordCategoryListAPIView(APIView):
    def get(self, request):
        passwords = PasswordCategory.objects.all()
        serializer = PasswordCategorySerializer(passwords, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PasswordCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordCategoryDetailAPIView(APIView):
    def get(self, request, id):
        try:
            password_category = PasswordCategory.objects.get(pk=id)
            serializer = PasswordCategorySerializer(password_category)

            return Response(serializer.data)
        except PasswordCategory.DoesNotExist:
            return Response(
                {"message": "Password category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            print("Error getting password category by id", e)

            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, id):
        try:
            password_category = PasswordCategory.objects.get(pk=id)
            serializer = PasswordCategorySerializer(
                password_category, data=request.data
            )

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PasswordCategory.DoesNotExist:
            return Response(
                {"message": "Password category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            print("Error updating password category", e)

            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, id):
        try:
            password_category = PasswordCategory.objects.get(pk=id)
            password_category.delete()

            return Response(
                {"message": "Password category deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except PasswordCategory.DoesNotExist:
            return Response(
                {"message": "Password category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            print("Error deleting password category", e)

            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
