from .models import task
from rest_framework import serializers

class taskserializers(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ('id', 'name', 'priority', 'date')
