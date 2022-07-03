from django.urls import path

from services import views

urlpatterns = [
    path('service', views.ServiceRegistrationView.as_view()),
    path('service/acquire', views.ServiceAcquirementView.as_view()),
]
