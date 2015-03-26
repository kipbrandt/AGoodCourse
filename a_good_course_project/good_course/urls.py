from django.conf.urls import patterns, url
from good_course import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^school/(?P<school_tag>[\w\-]+)/$', views.school, name='school'),
        url(r'^add_course/$', views.add_course, name='add_course'),
        url(r'^course/(?P<course_name_slug>[\w\-]+)/$', views.course, name='course'),
        url(r'^profile/', views.profile, name='profile'),
        url(r'^add_profile/', views.register_profile, name='add_profile')
        )
