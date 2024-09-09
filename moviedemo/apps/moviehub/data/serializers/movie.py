from rest_framework import serializers

from ..models import Movie, Cinema

class MovieSerializer(serializers.ModelSerializer):
    """Movie serializer"""
    class Meta:
        model = Movie
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    """Cinema serializer"""
    class Meta:
        model = Cinema
        fields = "__all__"