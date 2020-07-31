from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.response import Response


from .serializers import MycrudeSerializer
from .models import Mycrude




# this view will return the urls possiple
@api_view(['GET'])
def index(request):
    my_urls = {
                "forAllCrude":"api/mycrude" ,
                "forSpecific":"api/mycrude/id",

                }



    return Response(my_urls)
# lets first create a view that will have 3 https functions ....delete , post and get


@api_view(['POST' , "GET" ,"DELETE"])
def mycrude_list(request):
    # if request is for post
    if request.method == "POST":
        # we will get the data and then save them
        # mycrude_data = MycrudeSerializer(data = JSONParser().parse(request))
        mycrude_data = MycrudeSerializer(data = request.data)

        # check if valid
        if mycrude_data.is_valid():
            mycrude_data.save()

            return Response(mycrude_data.data , status = status.HTTP_201_CREATED)

        return Response(mycrude_data.errors  , status = status.HTTP_400_BAD_REQUEST)


    # if the request is GET

    elif request.method == "GET":
        mycrude_data = MycrudeSerializer(Mycrude.objects.all() , many = True)
        return Response(mycrude_data.data)

    # if the retuest is DELETE
    elif request.method == "DELETE":
        mycrude_data = Mycrude.objects.all()
        mycrude_data.delete()
        return Response({"message":"All Data Have been deleted suuccessfully"} , status=status.HTTP_204_NO_CONTENT)





#this view will find crude by id , update , delete or get it depending on the type of request
@api_view(["GET" , "PUT" , "DELETE"])
def mycrude_detail(request , id):
    try:
        mycrude_data = Mycrude.objects.get(id = id)
    except Mycrude.DoesNotExist:
        return Response({"message": "Crude requested does not exists"} , status=status.HTTP_404_NOT_FOUND)


    if request.method == "PUT":
        # update the item with that id
        # update_data  = MycrudeSerializer(mycrude_data , JSONParser().parse(request))
        update_data = MycrudeSerializer(mycrude_data , request.data)

        if update_data.is_valid():
            update_data.save()
            return Response(update_data.data , status = status.HTTP_201_CREATED)
        return Response(update_data.errors , status = status.HTTP_400_BAD_REQUEST)


    elif request.method == "GET":
        # returm the given item
        mycrude_data = MycrudeSerializer(mycrude_data)
        return Response(mycrude_data.data)


    elif request.method == "DELETE":
        # delete the data passed by the id

        mycrude_data.delete()
        return Response({"message":"Item suuccessfully Deleted"})
