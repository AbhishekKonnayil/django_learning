from rest_framework.decorators import api_view
from rest_framework.response import Response


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
