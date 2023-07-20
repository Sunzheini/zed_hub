from django.urls import path, include

from zed_hub.main_app.views import index_view, list_view, create_view, show_view, edit_view, delete_view

urlpatterns = [
    path('', index_view, name='main app index'),
    path('main-app-list/', list_view, name='main app list'),
    path('main-app-add/', create_view, name='main app add'),
    path('main-app-show/<int:pk>/<slug:slug>/', show_view, name='main app show'),
    path('main-app-edit/<int:pk>/<slug:slug>/', edit_view, name='main app edit'),
    path('main-app-delete/<int:pk>/<slug:slug>/', delete_view, name='main app delete'),
]
