from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^cadastro/', views.CreateUserView.as_view(), name='cadastro'),
]
