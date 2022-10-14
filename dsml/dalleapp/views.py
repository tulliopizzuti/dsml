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
#summarizer = pipeline("summarization", model=model_name)


# Create your views here.

def get(key, default):
    return getattr(settings, key, default)

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
        dalle = Dalle2(get('OPENAI_SESS_K',"")) 
        generations = dalle.generate_amount(text,int(get('OPENAI_N_IMAGE',4)))
        #j='[[{"id":"generation-60JncM5O5UCyO7OnW4IUhqx9","object":"generation","created":1665761390,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-60JncM5O5UCyO7OnW4IUhqx9/image.webp?st=2022-10-14T14%3A30%3A53Z&se=2022-10-14T16%3A28%3A53Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T14%3A27%3A23Z&ske=2022-10-21T14%3A27%3A23Z&sks=b&skv=2021-08-06&sig=IaO43OTvqznTLOPbke1fkmxvlpIbxHx3xJis7d4AVa4%3D"},"task_id":"task-y7Kuld6wIeM2Aqqd7qOF20eG","prompt_id":"prompt-uQ6mONyVQkxE7Ca3ICiMnF1e","is_public":false},{"id":"generation-X4v8R9DNQamHbbEi69We4bHM","object":"generation","created":1665761392,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-X4v8R9DNQamHbbEi69We4bHM/image.webp?st=2022-10-14T14%3A30%3A53Z&se=2022-10-14T16%3A28%3A53Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T14%3A27%3A23Z&ske=2022-10-21T14%3A27%3A23Z&sks=b&skv=2021-08-06&sig=tnoMR5nhuSE2T18cbTxowvcHvC5nFGYE81NvU%2B38HbM%3D"},"task_id":"task-y7Kuld6wIeM2Aqqd7qOF20eG","prompt_id":"prompt-uQ6mONyVQkxE7Ca3ICiMnF1e","is_public":false},{"id":"generation-B2uk27XYyPwBTs5FKymKyul8","object":"generation","created":1665761390,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-B2uk27XYyPwBTs5FKymKyul8/image.webp?st=2022-10-14T14%3A30%3A53Z&se=2022-10-14T16%3A28%3A53Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T14%3A27%3A23Z&ske=2022-10-21T14%3A27%3A23Z&sks=b&skv=2021-08-06&sig=dNfdiiPVcaxoSSL8UruFI0mzGtsfB8EBIR%2BwwocvkAc%3D"},"task_id":"task-y7Kuld6wIeM2Aqqd7qOF20eG","prompt_id":"prompt-uQ6mONyVQkxE7Ca3ICiMnF1e","is_public":false},{"id":"generation-3xS6eV1H8fIqQdpgh12aTGpu","object":"generation","created":1665761392,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-3xS6eV1H8fIqQdpgh12aTGpu/image.webp?st=2022-10-14T14%3A30%3A53Z&se=2022-10-14T16%3A28%3A53Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T14%3A27%3A23Z&ske=2022-10-21T14%3A27%3A23Z&sks=b&skv=2021-08-06&sig=lEschxCuCKLk%2B3czGK49Cq/p388pO63QVSmkRvi4XKo%3D"},"task_id":"task-y7Kuld6wIeM2Aqqd7qOF20eG","prompt_id":"prompt-uQ6mONyVQkxE7Ca3ICiMnF1e","is_public":false}],[{"id":"generation-THq9QYuLsjndIVtHRdwq9NXC","object":"generation","created":1665761402,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-THq9QYuLsjndIVtHRdwq9NXC/image.webp?st=2022-10-14T14%3A31%3A04Z&se=2022-10-14T16%3A29%3A04Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T14%3A55%3A21Z&ske=2022-10-21T14%3A55%3A21Z&sks=b&skv=2021-08-06&sig=8OsCeOVt2tbzwGG38D2kV5S0EfAxQJAURnDcA7SyvzY%3D"},"task_id":"task-WCvJ9oxLb1TpjYe7kph4W0F2","prompt_id":"prompt-L0eqaj0TSWqQE68xIYDJKRvJ","is_public":false},{"id":"generation-WA3wfs6GKV0bsN9WUIhwDAyy","object":"generation","created":1665761402,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-WA3wfs6GKV0bsN9WUIhwDAyy/image.webp?st=2022-10-14T14%3A31%3A04Z&se=2022-10-14T16%3A29%3A04Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T14%3A55%3A21Z&ske=2022-10-21T14%3A55%3A21Z&sks=b&skv=2021-08-06&sig=OhastSJmcnAGxze1XrIM%2B9Rm1s1vvKfXdhZ/lpmBcTU%3D"},"task_id":"task-WCvJ9oxLb1TpjYe7kph4W0F2","prompt_id":"prompt-L0eqaj0TSWqQE68xIYDJKRvJ","is_public":false},{"id":"generation-eMS0fSlSH3Anm2HDqg3eSJJv","object":"generation","created":1665761400,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-eMS0fSlSH3Anm2HDqg3eSJJv/image.webp?st=2022-10-14T14%3A31%3A04Z&se=2022-10-14T16%3A29%3A04Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T14%3A55%3A21Z&ske=2022-10-21T14%3A55%3A21Z&sks=b&skv=2021-08-06&sig=qip0y4/Gr/gNFgYJzJEVFcM%2ByxQnJNrYQlm6KgizO98%3D"},"task_id":"task-WCvJ9oxLb1TpjYe7kph4W0F2","prompt_id":"prompt-L0eqaj0TSWqQE68xIYDJKRvJ","is_public":false},{"id":"generation-5nJItcZgeFTRp7zGBABmS9H7","object":"generation","created":1665761400,"generation_type":"ImageGeneration","generation":{"image_path":"https://openailabsprodscus.blob.core.windows.net/private/user-jUu7fCE5KYKhGHCL5HWVPj6M/generations/generation-5nJItcZgeFTRp7zGBABmS9H7/image.webp?st=2022-10-14T14%3A31%3A04Z&se=2022-10-14T16%3A29%3A04Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/webp&skoid=15f0b47b-a152-4599-9e98-9cb4a58269f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-10-14T14%3A55%3A21Z&ske=2022-10-21T14%3A55%3A21Z&sks=b&skv=2021-08-06&sig=JHjNJW8oS0DyuCTkXVvAHbWgA4AyGfeDppqInIS6TRc%3D"},"task_id":"task-WCvJ9oxLb1TpjYe7kph4W0F2","prompt_id":"prompt-L0eqaj0TSWqQE68xIYDJKRvJ","is_public":false}]]'
        #generations = json.loads(j)
        out=[]
        for g in generations:
            out.extend(list(map(lambda x : x["generation"]["image_path"], g)))
        return Response(out, status=status.HTTP_200_OK)

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
