from django.urls import path
from . import views


urlpatterns = [  
    path('api/blogs/index/', views.index, name='index'),
    path('api/blogs/add/', views.create_blog, name='create-blog'), 
	path('api/blogs/update/<int:pk>', views.update_blog, name='update-blog'), 
    path('api/blogs/delete/<int:pk>', views.delete_blog, name='delete-blog'),
	
    path('api/blogs/', views.blog_list, name='blog-list'),
    path('api/blogs/<int:pk>', views.blog_detail, name='blog-detail'),
    path('api/blogs/published', views.blog_list_published, name='blog-list-published')
]