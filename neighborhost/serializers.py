from rest_framework import serializers
from . import models
from datetime import datetime

class NeighborSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Neighbor
        fields = '__all__'

    def create(self, validated_data):

        user = models.Neighbor.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
            is_superuser = False,
            is_staff = False,
            is_active = True,
            date_joined = datetime.now(),
            zipcode_id = validated_data['zipcode'].zipcode_id
        )
        user.set_password(validated_data['password'])
        user.save()
        return user