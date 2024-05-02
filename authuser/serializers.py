from rest_framework import serializers
from django.contrib.auth import get_user_model
user = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['first_name','middle_name','last_name','email','password']

    def validate(self, attrs):
        if user.objects.filter(username = attrs.get('email')).exists():
            raise serializers.ValidationError('email already in use')
        if len(attrs.get('password'))<8 or len(attrs.get('password'))>65:
            raise serializers.ValidationError('password must be between 8 and 65 characters')
        
        return super().validate(attrs)
