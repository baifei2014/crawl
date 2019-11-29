# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]


# from rest_framework.routers import DefaultRouter
# from rouse import views

# router = DefaultRouter()
# router.register(r'hello', views.HelloWorldViewSet, base_name="hello")
# urlpatterns = router.urls

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rouse import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'image', views.ImageCrawlViewSet, base_name="image")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]