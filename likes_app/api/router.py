from rest_framework import routers

from .views.likes import LikePostView, LikeCommentView


api_router = routers.DefaultRouter()

api_router.register('like/post', LikePostView)
api_router.register('like/comment', LikeCommentView)
