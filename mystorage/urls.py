from rest_framework.routers import DefaultRouter #router를 기반으로 작성할겁니다.
from django.urls import path, include
from mystorage import views


router = DefaultRouter()
router.register('essay', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
