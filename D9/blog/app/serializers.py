from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    
    author = AuthorSerializer(required=False)

    class Meta:
        model = Post
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['posts'] = PostSerializer(many=True, required=False)
        return fields