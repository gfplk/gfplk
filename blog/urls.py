from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^change_password$', views.change_password, name='change_password'),
    url(r'^logout$', views.logout, name='logout'),

    url(r'^add_article$', views.add_article, name='add_article'),
    url(r'^delete_article$', views.delete_article, name='delete_article'),
    url(r'^view_article$', views.view_article, name='view_article'),
    url(r'^edit_article$', views.edit_article, name='edit_article'),

    url(r'^add_article_type$', views.add_article_type, 
        name='add_article_type'),
    url(r'^delete_article_type$', views.delete_article_type, 
        name='delete_article_type'),
    url(r'^view_article_type$', views.view_article_type, 
        name='view_article_type'),
    url(r'^edit_article_type$', views.edit_article_type,
        name='edit_article_type'),

    url(r'^add_comment$', views.add_comment, name='add_comment'),
    url(r'^delete_comment$', views.delete_comment, name='delete_comment'),
    url(r'^view_comment$', views.view_comment, name='vew_comment'),
]
