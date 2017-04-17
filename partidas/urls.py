from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MatchsListView.as_view(), name='home'),
]
