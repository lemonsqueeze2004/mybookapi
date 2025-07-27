from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book
from django.shortcuts import get_object_or_404


class BookListCreateAPIView(APIView):

    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)


    def post(slef,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\
        
class BookDetailAPIView(APIView):
    def get(self,request,pk):
        book=get_object_or_404(Book,pk=pk)
        serializer=BookSerializer(book)
        return Response(serializer.data)


    def put(self,request,pk):
        book=get_object_or_404(Book,pk=pk)
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
    def delete(self,request,pk):
        book=get_object_or_404(Book,pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    






# Create your views here.
