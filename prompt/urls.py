from django.urls import path, include
from prompt import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('manage', views.manage_prompts),
    path('all/', views.get_all_prompts),
]
