from rest_framework import serializers
from home.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['name', 'age', 'location']

    def validate(self, data):
        spl_char = '!@#$%^&*()_+{}|:"<>?'
        if any(char in spl_char for char in data['name']):
            raise serializers.ValidationError(
                "special characters are not allowed in name")
        if data['age'] < 18:
            raise serializers.ValidationError("age should be greater than 18")
        return data
