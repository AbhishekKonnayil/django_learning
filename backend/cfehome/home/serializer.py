from rest_framework import serializers
from home.models import Person
from home.models import Team


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['team_name']


class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    team_info=serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'
        depth = 1
    
    def get_team_info(self,obj):
        return "extra field"

    def validate(self, data):
        spl_char = '!@#$%^&*()_+{}|:"<>?'
        if any(char in spl_char for char in data['name']):
            raise serializers.ValidationError(
                "special characters are not allowed in name")
        if data['age'] < 18:
            raise serializers.ValidationError("age should be greater than 18")
        return data
