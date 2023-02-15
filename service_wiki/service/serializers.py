from rest_framework import serializers

from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    create_timestamp = serializers.FloatField()
    timestamp = serializers.FloatField()
    language = serializers.CharField(max_length=256)
    wiki = serializers.CharField(max_length=256)
    title = serializers.CharField(max_length=256)
    category = serializers.ListField()
    auxiliary_text = serializers.ListField()

    class Meta:
        model = Content
        fields = ('create_timestamp', 'timestamp', 'language', 'wiki', 'title', 'category', 'auxiliary_text')


class ContentSerializer1(serializers.ModelSerializer):
    create_timestamp = serializers.FloatField()
    timestamp = serializers.FloatField()
    language = serializers.CharField(max_length=256)
    wiki = serializers.CharField(max_length=256)
    title = serializers.CharField(max_length=256)
    category = serializers.ListField()
    auxiliary_text = serializers.ListField()

    class Meta:
        model = Content
        fields = ('create_timestamp', 'timestamp', 'language', 'wiki', 'title', 'category', 'auxiliary_text')