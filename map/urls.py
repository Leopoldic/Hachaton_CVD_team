from django.urls import path
from . import views

urlpatterns = [
    path('', views.present, name='map'),
    path('change/heatmap', views.change_heatmap),
    path('change/camera', views.change_camera_map),
    path('add-point', views.add_point),
]