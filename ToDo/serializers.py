from rest_framework.serializers import HyperlinkedModelSerializer
from .models import *


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'