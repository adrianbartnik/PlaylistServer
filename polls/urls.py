from django.conf.urls import patterns, url
from mysite import settings

from polls import views

urlpatterns = patterns("", 
        url(r"^$", views.index, name="index"),
	url(r"^sound$", views.sound, name="sound")
)
