from distutils.log import Log
from lib2to3.pgen2.tokenize import tokenize
from django.shortcuts import render
from .models import Text
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404

from nltk.tokenize import word_tokenize
from transformers import pipeline
from dalle2 import Dalle2

from django.conf import settings

import os

model_name = "facebook/bart-large-cnn"
#https://huggingface.co/models?pipeline_tag=summarization&sort=downloads
#https://huggingface.co/docs/transformers/v4.21.0/en/main_classes/pipelines#transformers.SummarizationPipeline
summarizer = pipeline("summarization", model=model_name)


# Create your views here.


def index(req):
    return render(req, 'index.html')


def wordtree(req):
    text=req.GET.get("text")
    
    return render(req, 'wordtree.html', {"text":"" if text is None else text})


def texts(req):
    return render(req, 'texts.html')

class SummaryApiView(APIView):
    def get(self, request, id=None):
        text = request.query_params.get("text")
        summarizer = pipeline(
                "summarization",
                model=model_name
        )
        wordCount=len(word_tokenize(text))
        maxLen=int((wordCount/4)*3)
        summ = summarizer(text, min_length=1, max_length=maxLen)
        out = summ[0]["summary_text"]
        return Response(out, status=status.HTTP_200_OK)


class Dalle2ApiView(APIView):
    def get(self, request, id=None):
        text = request.query_params.get("text")
        dalle = Dalle2("sess-m5P8qcas7Sv7A5vq2OiAvw9iJmmpW99IdMv5q0kB") 
        generations = dalle.generate(text)
        return Response(generations, status=status.HTTP_200_OK)

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
        summarization = request.query_params.get("summarization")
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
        if(id and summarization == "true"):

            summarizer = pipeline(
                "summarization",
                model=model_name
            )
            article=result["data"]["testo"]
            wordCount=len(word_tokenize(article))
            maxLen=(wordCount/4)*3
            print(maxLen)
            summ = summarizer(article, min_length=1, max_length=maxLen)
            out = summ[0]["summary_text"]
            result["data"]["testo"] = out

        if(not id):
            result["recordsTotal"] = len(item)
            result["recordsFiltered"] = len(item)
        return Response(result, status=status.HTTP_200_OK)
