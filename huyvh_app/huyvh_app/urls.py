"""huyvh_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
router = routers.DefaultRouter()
router.register(r'ws', views.PostViewSet)
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	#url(r'^blog/', views.index, name='index'),
	url(r'^blog_list/', views.blog_list, name='blog_list'),
    url(r'^search_post/', views.search_post, name='search_post'),
    url(r'^client/', views.blog_client, name='blog_client'),
    url(r'^client_search/', views.blog_client_search, name='blog_client_search'),
    url(r'^searchblog/$', views.get_blog_list),
	#url(r'^$', views.blog_list, name='blog_list'),
	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit, name='post_edit'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  #  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
