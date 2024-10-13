from rest_framework.views import Response, status
from rest_framework.decorators import api_view

from passwords.models import Password, PasswordCategory


@api_view(["GET"])
def get_passwords():
    passwords = Password.objects.all()

    return Response(passwords)


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
        category_id=request.data.get("category_id"),
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
        password.category_id = request.data.get("category_id")

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
