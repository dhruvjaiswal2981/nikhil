from django.urls import path
from .import views


urlpatterns = [
    path('index/',views.index),
    path('recipes/', views.recipes),
    path('delete_recipe/<id>/',views.delete_recipe),#here dynamic url genrate using <id>
    path('update_recipe/<id>/',views.update_recipe),
    path('login/',views.login_page),
    path('register/',views.register_page),
    path('logout/',views.logout_page),

    ]
