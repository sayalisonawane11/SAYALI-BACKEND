from rest_framework import serializers
from .models import User, Recipe, Ingredients, Process
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'user_id', 'password')

    def validate(self, data):
        user_id = data.get('user_id')
        if len(user_id)==0:
            raise serializers.ValidationError('User_id is required for login!!!')
        password = data.get('password')
        if len(password)==0:
            raise serializers.ValidationError('password is required for login!!!')
        return data


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = "__all__"
    
class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = "__all__"
