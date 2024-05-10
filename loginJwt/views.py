from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status

from .models import User, Todo

from .serializer import MyTokenObtainPairSerializer, RegisterSerializer,TodoSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = User.objects.get(id=user_id)

        todo = Todo.objects.filter(user=user)
        return todo
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        todo_id = self.kwargs['todo_id']

        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=todo_id, user=user)

        return todo

class TodoMarkAsCompleted(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        todo_id = self.kwargs['todo_id']

        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=todo_id, user=user)

        todo.complete = True
        todo.save()

        return todo

# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = ['/loginJwt/token/', '/loginJwt/register/', '/loginJwt/token/refresh/']
    return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def testEndPoint(request):
    if request.method == 'GET':
        data = f'Parabéns {request.user}, sua api responde a sua solicitação GET'
        return Response({'response':data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = 'Hello buddy'
        data = f'Parabéns {request.user}, sua api respondeu ao seu POST request com texto: {text}'
        return Response({'response':data}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


