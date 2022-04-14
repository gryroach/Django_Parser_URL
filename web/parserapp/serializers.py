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

    def create(self, validated_data):
        mx_data = validated_data.pop("MX", None)
        domain = DomainModel.objects.create(**validated_data)
        for i_mx in mx_data:
            MxModel.objects.create(domain=domain, **i_mx)
        return domain
