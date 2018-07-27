from django.urls import path,include
from. import views

urlpatterns = [
	path('blog/', views.index),
	path('poste/(?p<id> [0-9]+)$', views.index),
]
