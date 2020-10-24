from rest_framework import serializers
from msteams.models import Msteams

class MsteamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Msteams
        fields = ('id','subject','email','password','prof','time','days')