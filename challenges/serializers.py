from rest_framework import serializers
from .models import Challenge


class ChallengeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        fields = ('title', 'score', 'category')


class ChallengeDetailSerializer(serializers.ModelSerializer):
    hints = serializers.StringRelatedField(many=True)

    class Meta:
        model = Challenge
        fields = ('title', 'description', 'category', 'hints', 'score')


class SubmitFlagSerializer(serializers.Serializer):
    flag = serializers.CharField(required=True)
