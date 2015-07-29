from django.conf.urls import patterns, url
from homePage import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^regist/', views.regist),
    url(r'^course/', views.course),
    url(r'^manage/', views.manage),
    url(r'^add_course/', views.add_course),
    url(r'cancel_course/', views.cancel_course),
)

