from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^entrar/', views.LoginView.as_view(), name='login'),
    url(r'^sair/', views.logout, name='logout'),
    url(r'^cadastro/', views.CreateUserView.as_view(), name='cadastro'),
]
