from rest_framework import serializers
from .models import Configuration, Text


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ["id","descrizione", "testo"]

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ["id","summaryModel", "openaiSessK", "nImages"]