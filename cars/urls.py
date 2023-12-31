
from django.urls import path
from . import views
urlpatterns = [
    path('add-brand/', views.add_brand, name='add_brand'),
    path('add-car/', views.AddCarCreateView, name='add_car'),
    path('edit-car/<int:id>', views.EditCarView, name='edit_car'),
    path('delete/<int:id>', views.delete_car, name='delete_car'),
    path('details/<int:id>', views.DetailCarView, name='detail_car'),
]