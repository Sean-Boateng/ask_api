from django.urls import path, include
from response import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('<int:prompt_id>/', views.submit_reply, name='submit_reply'),
    path('get/<int:prompt_id>/', views.get_responses),
]
