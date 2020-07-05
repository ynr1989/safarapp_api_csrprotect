from rest_framework import serializers
from patients.models import Patient, UserToken


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('__all__')

    def validate(self, data):
        if Patient.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email Already Exists!'})
        if Patient.objects.filter(mobile=data['mobile']).exists():
            raise serializers.ValidationError({'mobile number Already Exists!'})
        return data


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = ('__all__')
