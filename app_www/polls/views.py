from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Osoba, Druzyna
from .serializers import OsobaModelSerializer, DruzynaModelSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class PersonsList(APIView):

    def get(self, request, format=None):
        persons = Osoba.objects.all()
        serializer = OsobaModelSerializer(persons, many=True)
        return Response(serializer.data)

class PersonDetail(APIView):

    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        person = Osoba.objects.get(pk=pk)
        serializer = OsobaModelSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = OsobaModelSerializer(self.get_object(pk), data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DruzynaList(APIView):

    def get(self, request, format=None):
            teams = Druzyna.objects.all()
            serializer = DruzynaModelSerializer(teams, many=True)
            return Response(serializer.data)


class DruzynaDetail(APIView):

    def get_object(self,request, pk, format=None):
        try:
            return Druzyna.objects.get(pk=pk)
        except Druzyna.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        team = Druzyna.objects.get(pk=pk)
        serializer = DruzynaModelSerializer(team)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = DruzynaModelSerializer(self.get_object(pk), data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        team = self.get_object(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)