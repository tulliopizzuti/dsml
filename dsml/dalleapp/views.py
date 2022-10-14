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
import json

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
        #generations = dalle.generate(text)
        j='[{"id":"generation-Gygq603zRr3MqxTFVo6J7Z1F","object":"generation","created":1665753021,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-Gygq603zRr3MqxTFVo6J7Z1F/image.webp?st=2022-10-14T12%3A11%3A26Z&se=2022-10-14T14%3A09%3A26Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T08%3A49%3A33Z&ske=2022-10-21T08%3A49%3A33Z&sks=b&skv=2021-08-06&sig=m7ShuVKK4IaTaB94KJmUsNXSM5npMdWoNbvCVnWKawo%3D"},"task_id":"task-ZO7nOIr7x1uaNJ3aDzm9T5Hb","prompt_id":"prompt-zOy14wn8xv50G8WCwXfq76Vz","is_public":false},{"id":"generation-0mWV2IFHtM5hoQvmEGGwgDjC","object":"generation","created":1665753021,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-0mWV2IFHtM5hoQvmEGGwgDjC/image.webp?st=2022-10-14T12%3A11%3A26Z&se=2022-10-14T14%3A09%3A26Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T08%3A49%3A33Z&ske=2022-10-21T08%3A49%3A33Z&sks=b&skv=2021-08-06&sig=bpTwAN5aY060jcvvm8fuy%2B4armwyWyHA3IAF6LArPuA%3D"},"task_id":"task-ZO7nOIr7x1uaNJ3aDzm9T5Hb","prompt_id":"prompt-zOy14wn8xv50G8WCwXfq76Vz","is_public":false},{"id":"generation-1DFxjeMUWYNjmNSbNr7SpzrK","object":"generation","created":1665753022,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-1DFxjeMUWYNjmNSbNr7SpzrK/image.webp?st=2022-10-14T12%3A11%3A26Z&se=2022-10-14T14%3A09%3A26Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T08%3A49%3A33Z&ske=2022-10-21T08%3A49%3A33Z&sks=b&skv=2021-08-06&sig=Z1OHYUx9EYnHCvJu87%2B802wda6c%2BkmP11WfUeKIRjyY%3D"},"task_id":"task-ZO7nOIr7x1uaNJ3aDzm9T5Hb","prompt_id":"prompt-zOy14wn8xv50G8WCwXfq76Vz","is_public":false},{"id":"generation-XOXaX4vvPYfDuqd2GDcRiLwC","object":"generation","created":1665753022,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-XOXaX4vvPYfDuqd2GDcRiLwC/image.webp?st=2022-10-14T12%3A11%3A26Z&se=2022-10-14T14%3A09%3A26Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T08%3A49%3A33Z&ske=2022-10-21T08%3A49%3A33Z&sks=b&skv=2021-08-06&sig=Sp7relmnho3H5PPgPDF3eZqWr%2BG23rsc7NoNWv9ElRU%3D"},"task_id":"task-ZO7nOIr7x1uaNJ3aDzm9T5Hb","prompt_id":"prompt-zOy14wn8xv50G8WCwXfq76Vz","is_public":false}]'
        generations = json.loads(j)
        out = map(lambda x : x["generation"]["image_path"], generations)
        return Response(list(out), status=status.HTTP_200_OK)

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
