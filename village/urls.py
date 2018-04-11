from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:child_id>/', views.show, name='show'),
    path('post_child/', views.post_child, name='post_child' ),
    path('user/<username>', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:child_id>/edit/', views.edit_child, name='edit_child'),
    path('<int:child_id>/destroy/', views.delete_child, name='delete_child'),
    # path('<int:cat_id>/toy/create/', views.create_toy, name='create_toy'),
]
