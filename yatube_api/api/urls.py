from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CommentViewset, FollowingViewset, GroupViewset, PostViewset


router = DefaultRouter()
router.register('posts', PostViewset, basename='posts')
router.register('groups', GroupViewset, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewset,
    basename='comments'
)
router.register('follow', FollowingViewset,
                'follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
