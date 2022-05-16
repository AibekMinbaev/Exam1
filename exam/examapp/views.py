from rest_framework import views, response, status, viewsets
from rest_framework.authtoken.admin import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from .serializers import PostSerializers, CommentSerializers, LikeSerializers 
from django.contrib.auth import get_user_model

User = get_user_model()



class UserRegisterAPIViews(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post 
    serializer_class = PostSerializers 
    permission_classes = IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet): 
    queryset = Comment 
    serializer_class = CommentSerializers 
    permission_classes = IsAuthenticated


class LikeViewSet(viewsets.ModelViewSet): 
    queryset = Like
    serializer_class = LikeSerializers 
    permission_classes = IsAuthenticated




