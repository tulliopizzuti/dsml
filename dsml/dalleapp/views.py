from django.shortcuts import render
from .models import Text
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.


def index(req):
    return render(req, 'index.html')


def wordtree(req):
    return render(req, 'wordtree.html')


def texts(req):
    return render(req, 'texts.html')


class TextListApiView(APIView):

    def post(self, request, id=None):
        if id:
            item = Text.objects.get(id=id)
            serializer = TextSerializer(item, data=request.data, partial=True)
        else:
            serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Text, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

    def get(self, request, id=None):
        if id:
            item = Text.objects.get(id=id)
        else:
            limit = request.query_params.get("limit")
            skip = request.query_params.get("skip")
            sortField = request.query_params.get("sortField")
            sortType = request.query_params.get("typeSort")
            fieldName = request.query_params.get("fieldName")
            fieldValue = request.query_params.get("value")
            if(limit):
                limit = int(limit)
            if(skip):
                skip = int(skip)

            item = Text.objects

            if(fieldName and fieldValue):
                item = item.filter(**{fieldName+"__icontains": fieldValue})

            if(sortField and sortType):
                item = item.order_by(
                    '-'+sortField if sortType == '-1' else sortField)

            if(limit and skip):
                item = item.values()[skip:skip+limit]
            elif(limit and not skip):
                item = item.values()[:limit]
            elif(not limit and skip):
                item = item.values()[skip:]
            elif(not limit and not skip):
                item = item.values()

        serializer = TextSerializer(item, many=(False if id else True))
        result = {
            "status": "success",
            "data": serializer.data
        }
        if(not id):
            result["recordsTotal"]=len(item)
            result["recordsFiltered"]=len(item)
        return Response(result, status=status.HTTP_200_OK)
