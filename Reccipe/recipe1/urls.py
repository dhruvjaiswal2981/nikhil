from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL points to index view
    path('recipes/', views.recipes, name='recipes'),
    path('delete_recipe/<id>/', views.delete_recipe, name='delete_recipe'),
    path('update_recipe/<id>/', views.update_recipe, name='update_recipe'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
]
