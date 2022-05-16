from rest_framework import serializers, validators
from .models import Post, Comment, Like 
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


User = get_user_model()

class PostSerializers(serializers.ModelSerializer): 
    class Meta: 
        model = Post 
        fields = '__all__' 


class CommentSerializers(serializers.ModelSerializer): 
    class Meta: 
        model = Comment 
        fields = '__all__' 

class LikeSerializers(serializers.ModelSerializer): 
    class Meta: 
        model = Like 
        fields = '__all__' 
     

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, min_length=8, write_only=True)
    confirm_password = serializers.CharField(required=True, min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data["username"],password=validated_data["password"])
        Token.objects.create(user=user)
        return user 


    def to_representation(self, instance): 
        response = super().to_representation(instance) 
        token = Token.objects.filter(user_id=instance.id).first() 
        response['token'] = token.key 
        return response