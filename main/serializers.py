from rest_framework import serializers
from main.models import News, ImageNews, Publication, Laws

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'pk title short_description date image'.split()

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = '__all__'
class NewsSingleSerializer(serializers.ModelSerializer):
    images = ImageSerializers(many=True)
    class Meta:
        model = News
        fields = 'title full_description images'.split()


class LawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laws
        fields = 'title short_description date type'.split()
class LawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laws
        fields = 'title full_description file'.split()


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'title short_description date type'.split()

class PublicationSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'title full_description file'.split()