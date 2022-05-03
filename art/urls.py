from django.urls import path, re_path

from . import views
from .views import *
from .views import EmailAttachementView
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', views.registration, name='register'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('send/', EmailAttachementView.as_view(), name='emailattachment'),

]
