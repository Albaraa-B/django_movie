from django.urls import path

from . import views

app_name="users"
urlpatterns = [
    # ex: /movie/detail
    path('favorites/<int:user_id>', views.favorites, name='favorites'),
    # ex: /polls/5/
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('search', views.search, name='search'),
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('add_favorite', views.add_favorite, name="add_favorite"),
    path('remove_favorite', views.remove_favorite, name='remove_favorite'),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
]