from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializer import PersonSerializer
from rest_framework.views import APIView


class ClassPerson(APIView):
    def get(self, request):
        objPerson = Person.objects.filter(team__isnull=False)
        serializer = PersonSerializer(objPerson, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        people_details = {
            "name": "Abhishek",
            "age": 25,
            "job": "Software Engineer"
        }
        return Response(people_details)
    elif request.method == 'POST':
        return Response("This is a post request")


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objPerson = Person.objects.filter(team__isnull=False)
        print(objPerson)
        serializer = PersonSerializer(objPerson, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id=request.data['id'])
        serializer = PersonSerializer(obj, data=data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=request.data['id'])
        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'Person deleted'})
