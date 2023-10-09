from django.urls import path
from approvals import views

urlpatterns = [
    path('approvals/', views.ApprovalList.as_view()),
    path('approvals/<int:pk>/', views.ApprovalDetail.as_view()),
]
