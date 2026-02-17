from django.urls import path

from MainApp import views


urlpatterns = [
    path("", views.MainView.as_view(), name="main")
]
