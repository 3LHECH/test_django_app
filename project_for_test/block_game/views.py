from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Score
# Create your views here.

def game(request):
    score = Score.objects.all().first()
    return render(request,"index.html",{"score":score})

@api_view(['POST'])
def save_score(request):
    score = int(request.data.get("score"))
    old_score = Score.objects.all().first()
    if(old_score == None and score > 0):
        obj, created = Score.objects.update_or_create(
            id=1,
            defaults={"score": score}
        )
        return Response(
            {"score": obj.score, "created": created},
            status=status.HTTP_200_OK
        )
    if score is not None and score > old_score.score :
        obj, created = Score.objects.update_or_create(
            id=1,
            defaults={"score": score}
        )
        return Response(
            {"score": obj.score, "created": created},
            status=status.HTTP_200_OK
        )

    return Response(
            {"score": old_score.score, "created": "no"},
            status=status.HTTP_200_OK
    )