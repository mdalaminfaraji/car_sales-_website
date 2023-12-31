
from django.urls import path
from . import views
urlpatterns = [
    path('add_brand/', views.add_brand, name='add_brand'),
    path('add_car/', views.AddCarCreateView.as_view(), name='add_car'),
    path('edit_car/<int:id>', views.EditCarView.as_view(), name='edit_car'),
    path('delete/<int:id>', views.delete_car, name='delete_car'),
    path('details/<int:id>', views.DetailCarView.as_view(), name='detail_car'),
]