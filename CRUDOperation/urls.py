from django.urls import path

from CRUDOperation import views

urlpatterns = [
    path('', views.welcome, name="welcome.html"),
    path('load_form/', views.load_form),
    path('add', views.add),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('search/', views.search),
]
