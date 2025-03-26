from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PeopleSerializer, LoginSerializer

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset

        if search : 
            result = queryset.filter(name__startswith = search)
        serialized_query = PeopleSerializer(result, many=True)

        
        return Response({"status" : 200, "data" : serialized_query.data}, status=status.HTTP_204_NO_CONTENT)
       
        

class PersonAPI(APIView):

    def get(self, request):
        return Response({"message" : "This is from the personapi class and method is GET"})
    
    def post(self, request):
        return Response({"message" : "This is from the personapi class and method is post"})
    
    def put(self, request):
        return Response({"message" : "This is from the personapi class and method is put"})
    
    def patch(self, request):
        return Response({"message" : "This is from the personapi class and method is patch"})
    
    def delete(self, request):
        return Response({"message" : "This is from the personapi class and method is delete"})



@api_view(['GET', 'POST'])
def index(request):
    courses = {
        "Name" : "Python",
        "learn" : ['django', 'flask', 'fastapi'],
        'course_outcome' : "12 LPA JOB"
    }

    if request.method == 'GET':
        print('You hit a GET request')
        print("The query parameter in get request is : ", request.GET.get('search'))
        return Response(courses)
    elif request.method == 'POST':
        print('You hit a POST request')
        data = request.data

        print("*****")
        print(data)
        print("*****")
        return Response(data)
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Person was posted")
            print("******")
            print(serializer.data)
            print("******")
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id=data['id'])

        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print("Method used is PUT")
            print("******")
            print(serializer.data)
            print("******")
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])

        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print("Person was patched")
            print("******")
            print(serializer.data)
            print("******")
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        data = request.data

        
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        message = "Person with id : " + str(data['id']) +" was deleted"
        return Response({"message" : message})
        

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)


    if serializer.is_valid():
        data = serializer.validated_data
        return Response({"message" : "Success"})
    
    return Response(serializer.errors)
        


from django.contrib.auth.models import User
from .serializers import UserSerializer


class RegisterAPI(APIView):
    
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if not serializer.is_valid():
            return Response({"status" : False,
                             "message" : serializer.errors},  status = status.HTTP_400_BAD_REQUEST)