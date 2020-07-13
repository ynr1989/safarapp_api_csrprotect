from rest_framework import serializers

from users.models import User, UserToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email Already Exists!'})
        if User.objects.filter(mobile=data['mobile']).exists():
            raise serializers.ValidationError({'mobile number Already Exists!'})
        return data


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = ('__all__')
