from rest_framework import serializers

from passwords.models import Password, PasswordCategory


class PasswordCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordCategory
        fields = "__all__"


class PasswordSerializer(serializers.ModelSerializer):
    password_category_id = serializers.UUIDField(write_only=True, required=False)
    category = PasswordCategorySerializer(read_only=True)

    class Meta:
        model = Password
        fields = [
            "id",
            "name",
            "username",
            "password",
            #  "user",
            #  "user_id",
            "category",
            "password_category_id",
        ]
        depth = 1

    def create(self, validated_data):
        #  user_id = validated_data.pop("user_id")
        #  user = User.objects.get(pk=user_id)

        password_category_id = validated_data.pop("password_category_id", None)

        password_category = None
        if password_category_id:
            password_category = PasswordCategory.objects.get(pk=password_category_id)

        return Password.objects.create(
            **validated_data,
            #  user=user,
            category=password_category
        )

    def update(self, instance, validated_data):
        password_category_id = validated_data.pop('password_category_id', None)

        if password_category_id:
            try:
                password_category = PasswordCategory.objects.get(pk=password_category_id)
                instance.category = password_category
            except PasswordCategory.DoesNotExist:
                raise serializers.ValidationError({"password_category_id": "Invalid password_category_id."})

        instance.name = validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()

        return instance
