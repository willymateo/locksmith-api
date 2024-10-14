from rest_framework import serializers

from passwords.models import Password, PasswordCategory


class PasswordCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordCategory
        fields = "__all__"


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ["id", "name", "username", "password", "category"]
        depth = 1

    def create(self, validated_data):
        password_category_id = validated_data.pop("password_category_id")
        password_category = PasswordCategory.objects.get(pk=password_category_id)

        return Password.objects.create(**validated_data, category=password_category)

    def update(self, instance, validated_data):
        password_category_id = validated_data.pop("password_category_id")
        password_category = PasswordCategory.objects.get(pk=password_category_id)

        return Password.objects.update(**validated_data, category=password_category)
