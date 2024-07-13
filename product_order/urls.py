from django.urls import path
from .import views

urlpatterns = [
    path('place-order/', views.place_order, name='place_order'),
    path('payments/', views.make_payment, name='make_payment'),
    path('complete-order/', views.complete_order, name='complete_order'),
]