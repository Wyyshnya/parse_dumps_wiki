from django.urls import path, re_path

from . import views

urlpatterns = [
    path('create_db/', views.do_base),
    path('search/<str:name>/f', views.get_formatted_article),
    path('search/<name>/', views.get_article),
    path('statistic/', views.get_statistic_all),
    path('statistic/<name>/', views.get_statistic),
]


