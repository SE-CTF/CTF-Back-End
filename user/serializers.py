from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email',
                  'username', 'password', 'bio', 'admin']
        extra_kwargs = {
            'password': {'write_only': True},
            'admin': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.admin = validated_data.get('admin', instance.admin)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance
