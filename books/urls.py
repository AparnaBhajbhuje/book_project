from django.urls import path
from .views import BookFilterListView

urlpatterns = [
    path('filter/', BookFilterListView.as_view(), name='book-filter-list'),
    # Add other URL patterns as needed
]
