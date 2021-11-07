from rest_framework import serializers
from AddPage.models import UserDetails, Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId', 'UserName')

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('Id','Pincode','Status','UserId')
