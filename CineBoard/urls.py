from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie/add/', views.MovieCreateView.as_view(), name='movie_add'),
    path('movie/<int:pk>/edit/', views.MovieUpdateView.as_view(), name='movie_edit'),
    path('movie/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('search/', views.MovieSearchView.as_view(), name='movie_search'),
    path('genre/<int:genre_id>/', views.GenreFilterView.as_view(), name='genre_filter'),
]


