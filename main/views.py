from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *




# Create your views here.

@api_view(['GET'])
def newsView(request):
    news = News.objects.all()
    data = NewsSerializer(news, many=True).data
    return Response(data=data)

@api_view(['GET'])
def newsSingleView(request, pk):
    try:
        singleNews = News.objects.get(id=pk)
    except News.DoesNotExist:
        return Response(data={'message': 'News not found'}, status=status.HTTP_404_NOT_FOUND)
    data = NewsSingleSerializer(singleNews).data
    return Response(data=data)

@api_view(['GET'])
def lawsView(request):
    laws = Laws.objects.all()
    data = LawsSerializer(laws, many=True).data
    return Response(data=data)

@api_view(['GET'])
def lawsSingleView(request, pk):
    try:
        law = Laws.objects.get(id=pk)
    except Laws.DoesNotExist:
        return Response(data={'message': 'Law does not exist'},
                        status=status.HTTP_404_NOT_FOUND)
    data = LawSerializer(law).data
    return Response(data=data)

@api_view(['GET'])
def publicationView(request):
    publications = Publication.objects.all()
    data = PublicationSerializer(publications, many=True).data
    return Response(data=data)

@api_view(['GET'])
def publicationSingleView(request, pk):
    try:
        publication = Publication.objects.get(id=pk)
    except Publication.DoesNotExist:
        return Response(data={'message': 'publication does not exist'})
    data = PublicationSingleSerializer(publication).data
    return Response(data=data)
