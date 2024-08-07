from django.shortcuts import render
from django.http import JsonResponse
from .serializer import DrinkSerializer
from .models import Drink
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# def drink_list(request):
#     context = {}
#     drinks = Drink.objects.all()
#     serializer = DrinkSerializer(drinks, many= True)
#     context['drinks']= serializer.data
#     return JsonResponse(context, safe=False)


# ViewSets define the view behavior.

@api_view(['GET','POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many= True)
        # return JsonResponse({'drinks':serializer.data})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse({'message':'Drink created successfully'}, status=201)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id, format=None):
    
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
        

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

