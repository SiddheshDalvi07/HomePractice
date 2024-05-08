from django.urls import path
from .views import StateListView, StateDetailView, StateCreateView, StateUpdateView, StateDeleteView

urlpatterns = [
    path('', StateListView.as_view(), name='state-list'),
    path('create/', StateCreateView.as_view(), name='state-create'),
    path('<int:pk>/', StateDetailView.as_view(), name='state-detail'),
    path('<int:pk>/update/', StateUpdateView.as_view(), name='state-update'),
    path('<int:pk>/delete/', StateDeleteView.as_view(), name='state-delete'),
]
