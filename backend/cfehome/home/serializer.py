from rest_framework import serializers
from home.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['name', 'age', 'location']
