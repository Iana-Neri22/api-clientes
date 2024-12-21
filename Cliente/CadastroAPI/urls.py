from django.urls import path

from . import views

urlpatterns = [
        path('',views.IndexView.as_view(), name=views.IndexView.__name__),
        path('cliente',views.ClienteView.as_view(), name=views.ClienteView.__name__),
    ]