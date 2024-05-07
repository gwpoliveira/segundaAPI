from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
# from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['full_name'] = user.prfile.full_name
        token['username'] = user.username
        token['email'] = user.email
        token['bio'] = user.prfile.bio
        token['image'] = str(user.prfile.image)
        token['verified']=user.prfile.verified

        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Senha não são iguais'})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'], email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


