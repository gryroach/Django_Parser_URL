from rest_framework import serializers
from .models import DomainModel, MxModel


class MxSerializer(serializers.ModelSerializer):
    class Meta:
        model = MxModel
        fields = ("exchange", "priority")


class DomainSerializer(serializers.ModelSerializer):
    MX = MxSerializer(many=True)

    class Meta:
        model = DomainModel
        fields = ("url", "domain", "create_date", "update_date",
                  "country", "isDead", "A", "NS", "CNAME", "MX", "TXT")
