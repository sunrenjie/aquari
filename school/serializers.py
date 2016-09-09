from rest_framework import serializers

from .models import App, AppCategory, AppDeveloper, AppRelease, AppTag


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('name', 'slug', 'info', 'summary', 'category')
