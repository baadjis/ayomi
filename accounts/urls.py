from django.conf.urls import url
from django.urls import path

from . import views
app_name='accounts'
urlpatterns = [
  url('^register/$', views.RegisterView.as_view(), name='register'),
  url('^login/$', views.LoginView.as_view(), name='login'),
  url('^profile/$', views.ProfileView.as_view(), name='profile'),
  url('^logout/$',views.logout_view,name='logout')


]