from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CommentViewset, GroupViewset, PostViewset


router = DefaultRouter()
router.register('posts', PostViewset, basename='posts')
router.register('groups', GroupViewset, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewset,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
