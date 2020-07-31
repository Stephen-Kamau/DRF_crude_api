from .models import Mycrude
from rest_framework import serializers



# serialize the model

class MycrudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mycrude
        fields = "__all__"
