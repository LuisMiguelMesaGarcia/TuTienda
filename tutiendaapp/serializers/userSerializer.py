from rest_framework import serializers
from tutiendaapp.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'nombres', 'apellidos', 'email', 'password']

    """def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'nombres': user.nombres,
            'apellidos': user.apellidos,
            'email': user.email,
        }""" 