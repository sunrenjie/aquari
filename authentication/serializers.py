from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.tagline = validated_data.get('tagline', instance.tagline)
            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)
            if password and confirm_password and password == confirm_password:
                # In real world system, we shall enforce password strength here.
                instance.set_password(password)

            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance
