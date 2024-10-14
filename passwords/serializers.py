from rest_framework import serializers

from passwords.models import Password, PasswordCategory


class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ["id", "name", "username", "password", "category"]


class PasswordCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PasswordCategory
        fields = ["id", "name"]
