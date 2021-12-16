from rest_framework import serializers
from .models import ProgLanguage

class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgLanguage
        fields = ['id_language', 'language_name', 'descript', 'creation_year']
