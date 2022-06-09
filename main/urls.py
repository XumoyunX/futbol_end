from django.urls import path
from main.views import index, region, reklama, malumotlar, post

urlpatterns = [
    path("", index, name="index"),
    path("region/<int:pk>/", region, name="region"),
    path("reklama/<int:pk>/", reklama, name="reklama"),
    path("malumotlar/", malumotlar, name="malumotlar"),
    path("post/", post, name="post")

]