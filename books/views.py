from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .pagination import CustomPagination
from django.db.models import Q

class BookFilterListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        try:
            queryset = Book.objects.all()
            
            # Apply filters based on query parameters
            book_id = self.request.query_params.get('book_id')
            if book_id:
                queryset = queryset.filter(id=book_id)
            
            language = self.request.query_params.get('language')
            if language:
                queryset = queryset.filter(language=language)
            
            mime_type = self.request.query_params.get('mime_type')
            if mime_type:
                queryset = queryset.filter(mime_type=mime_type)
            
            topic = self.request.query_params.get('topic')
            if topic:
                queryset = queryset.filter(Q(subject__icontains=topic) | Q(bookshelf__icontains=topic))
            
            author = self.request.query_params.get('author')
            if author:
                queryset = queryset.filter(author__icontains=author)
            
            title = self.request.query_params.get('title')
            if title:
                queryset = queryset.filter(title__icontains=title)
            
            return queryset
        except Exception as e:
            print("Error occurred:", e)
            return None



class BookSortListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all().order_by('-downloads')
        return queryset


class BookPaginationListView(generics.ListAPIView):
    serializer_class = BookSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Book.objects.all().order_by('-downloads')
        return queryset
