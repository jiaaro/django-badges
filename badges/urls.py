from django.conf.urls import url

from badges import views

urlpatterns = [
    url(r'^$', views.overview, name="badges_overview"),
    url(r'^(?P<slug>[A-Za-z0-9_-]+)/$', views.detail, name="badge_detail"),
]