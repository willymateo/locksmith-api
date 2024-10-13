from rest_framework.views import Response, status
from rest_framework.decorators import api_view
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
    def get(self, request, pk):
        try:
            password = Password.objects.get(pk=pk)
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

    def put(self, request, pk):
        try:
            password = Password.objects.get(pk=pk)
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

    def delete(self, request, pk):
        try:
            Password.objects.get(pk=pk).delete()

            return Response({"message": "Password deleted successfully"})
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
    def get(self, request, pk):
        try:
            password_category = PasswordCategory.objects.get(pk=pk)
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

    def put(self, request, pk):
        try:
            password_category = PasswordCategory.objects.get(pk=pk)
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

    def delete(self, request, pk):
        try:
            PasswordCategory.objects.get(pk=pk).delete()

            return Response({"message": "Password category deleted successfully"})
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


@api_view(["GET"])
def get_password_by_id(request):
    try:
        password_id = request.query_params.get("id")
        password = Password.objects.get(id=password_id)

        return Response(password)
    except Password.DoesNotExist:
        return Response(
            {"message": "Password not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        print("Error getting password by id", e)

        return Response(
            {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
def create_password(request):
    new_password = Password.objects.create(
        name=request.data.get("name"),
        username=request.data.get("username"),
        password=request.data.get("password"),
        password_category_id=request.data.get("password_category_id"),
    )

    return Response(new_password)


@api_view(["PUT"])
def update_password(request):
    try:
        password_id = request.query_params.get("id")
        password = Password.objects.get(id=password_id)

        password.name = request.data.get("name")
        password.username = request.data.get("username")
        password.password = request.data.get("password")
        password.password_category_id = request.data.get("password_category_id")

        password.save()

        return Response(password)
    except Password.DoesNotExist:
        return Response(
            {"message": "Password not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        print("Error updating password", e)

        return Response(
            {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["DELETE"])
def delete_password(request):
    try:
        password_id = request.query_params.get("id")

        Password.objects.get(id=password_id).delete()

        return Response({"message": "Password deleted successfully"})
    except Password.DoesNotExist:
        return Response(
            {"message": "Password not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        print("Error deleting password", e)

        return Response(
            {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["GET"])
def get_password_categories(request):
    passwords = PasswordCategory.objects.all()

    return Response(passwords)


@api_view(["GET"])
def get_password_category_by_id(request):
    try:
        password_category_id = request.query_params.get("id")
        password_category = PasswordCategory.objects.get(id=password_category_id)

        return Response(password_category)
    except PasswordCategory.DoesNotExist:
        return Response(
            {"message": "Password category not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        print("Error getting password category by id", e)

        return Response(
            {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
def create_password_category(request):
    new_password_category = PasswordCategory.objects.create(
        name=request.data.get("name"),
    )

    return Response(new_password_category)


@api_view(["PUT"])
def update_password_category(request):
    try:
        password_category_id = request.query_params.get("id")
        password_category = PasswordCategory.objects.get(id=password_category_id)

        password_category.name = request.data.get("name")

        password_category.save()

        return Response(password_category)
    except PasswordCategory.DoesNotExist:
        return Response(
            {"message": "Password category not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        print("Error updating password category", e)

        return Response(
            {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["DELETE"])
def delete_password_category(request):
    try:
        password_category_id = request.query_params.get("id")

        PasswordCategory.objects.get(id=password_category_id).delete()

        return Response({"message": "Password category deleted successfully"})
    except PasswordCategory.DoesNotExist:
        return Response(
            {"message": "Password category not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        print("Error deleting password category", e)

        return Response(
            {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
