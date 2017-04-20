from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MatchListView.as_view(), name='home'),
]
