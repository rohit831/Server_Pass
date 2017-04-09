from rest_framework import serializers
from .models import Sarees

class SareesCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Sarees
        fields = ('category',)