from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^realizar/', views.BetCreateView.as_view(), name='realizar-aposta'),
]
