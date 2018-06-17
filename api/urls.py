from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('executors', views.ExecutorViewSet, 'executors')
router.register('customers', views.CustomerViewSet, 'customers')
router.register('tasks', views.TaskViewSet, 'tasks')

urlpatterns = [
    url('^v1/', include(router.urls))
]
