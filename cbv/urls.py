from django.urls import path

from . import views

app_name = 'cbv'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('list/', views.FamilyListView.as_view(), name='list'),
    path('create/', views.FamilyCreateView.as_view(), name='family_create'),
    path('update/<int:pk>/', views.FamilyUpdateView.as_view(), name='family_update'),
    path('delete/<int:pk>/', views.FamilyDeleteView.as_view(), name='family_delete'),
]
