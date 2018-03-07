from django.urls import path

from . import views

urlpatterns = [
    # ex: /movie/detail
    path('favorites/<int:user_id>', views.favorites, name='favorites'),
    # ex: /polls/5/
    path('<int:movie_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('results/<str:query>', views.results, name='results'),
    path('', views.index, name='index'),
]