from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ChallengeListSerializer, ChallengeDetailSerializer
from .models import Challenge


class ChallengeList(APIView):
    def get(self, request):
        try:
            challenges = Challenge.objects.all()
            challenges_serializer = ChallengeListSerializer(
                challenges, many=True)
            return Response(data=challenges_serializer.data, status=status.HTTP_200_OK)
        except Challenge.DoesNotExist:
            return Response(data={'error': 'Challenges not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChallengeDetail(APIView):
    def get(self, request, pk):
        try:
            challenge = Challenge.objects.get(pk=pk)
            challenge_serializer = ChallengeDetailSerializer(challenge)
            return Response(data=challenge_serializer.data, status=status.HTTP_200_OK)
        except Challenge.DoesNotExist:
            return Response(data={'error': 'Challenge not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
