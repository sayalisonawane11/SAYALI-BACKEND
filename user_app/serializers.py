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
    user = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset = User.objects.get()
    )
    class Meta:
        model = Recipe
        fields = ('recipe_id', 'name', 'desc', 'image', 'user')
        read_only_fields = ('recipe_id',)

class IngredientsSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(
    many=True,
    queryset = Recipe.objects.all()
    )
    class Meta:
        model = Ingredients
        fields = ('ingredient_id', 'items', 'amount', 'unit', 'recipe')
        read_only_fields = ('ingredient_id',)
    
class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = "__all__"
