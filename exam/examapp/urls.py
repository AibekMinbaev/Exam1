from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet, LikeViewSet, UserRegisterAPIViews
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter() 

router.register('post', PostViewSet, basename = 'post')
router.register('comment', CommentViewSet, basename = 'comment')
router.register('like', LikeViewSet, basename = 'like')

urlpatterns = [
    path("",include(router.urls)),
    path('register/', UserRegisterAPIViews.as_view()),
    path('login/',obtain_auth_token) 
] 



