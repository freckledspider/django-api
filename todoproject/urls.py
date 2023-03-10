from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todos.views import TodoViewSet

# Create a Router
router = routers.DefaultRouter()
# Register viewset with the router
router.register(r'todos', TodoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
]