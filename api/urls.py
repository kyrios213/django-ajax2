from django.urls import path

from . import views

app_name ='posts'

urlpatterns = [
    path('', views.post_list_and_create, name="home"),

    path('hello-world/', views.hello_world_view, name='hello-world'),
    path('data/<int:num_posts>/', views.load_post_data_view, name='post-data'),
    path('like-unlike/', views.like_unlike_post, name='like-unlike'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    path('<int:pk>/data/', views.post_detail_data_view, name='post-detail-data'),

]
