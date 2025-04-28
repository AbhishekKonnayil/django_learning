from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializer import PersonSerializer, RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token


class RegisterAPI(APIView):
    def post(self, request):
        _data = request.data
        serializer = RegisterSerializer(data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'user created succesfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_404_NOT_FOUND)


class LoginAPI(APIView):
    def post(self, request):
        _data = request.data
        serializer = LoginSerializer(data=_data)
        if not serializer.is_valid():
            return Response({'message': serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        user = authenticate(
            username=_data['username'], password=_data['password'])
        if not user:
            return Response({'message': 'invalid credentials'}, status == status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'message': 'Login successfull', 'token': str(token)}, status=status.HTTP_200_OK)


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
        # serializer = PersonSerializer(data=data)
        # if serializer.is_valid():
        #    serializer.save()
        return Response({'data': 'person from api view fn'})
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


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset

        if search:
            queryset = queryset.filter(name__startswith=search)

        serializer = PersonSerializer(queryset, many=True)
        return Response({'status': 200, 'data': serializer.data})
