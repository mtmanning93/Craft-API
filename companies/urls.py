from django.urls import path
from companies import views

urlpatterns = [
    path('list/', views.CompanyList.as_view()),
    path('details/<int:pk>/', views.CompanyDetail.as_view()),
]
