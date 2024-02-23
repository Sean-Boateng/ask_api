from django.urls import path, include
from response import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('<str:unique_link>/', views.submit_reply, name='submit_reply'),
    path('get/<str:unique_link>/', views.get_responses),
]
