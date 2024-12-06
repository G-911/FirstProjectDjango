from django.urls import path
from .views import TemplateView
#create your urls here

urlpatterns = [
    path("", TemplateView.as_view(), name = "home"),
]
