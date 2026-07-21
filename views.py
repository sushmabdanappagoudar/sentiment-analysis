from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def analyze_text(request):
    data = json.loads(request.body)
    text = data.get("text")

    return JsonResponse({
        "primary_emotion": "happy",
        "sentiment": "positive",
        "confidence": 0.93,
        "analysis": f"Text '{text}' expresses positive emotion."
    })

from .models import SentimentResult

def analyze_text(request):
    if request.method == "POST":
        text = request.POST.get("text")
        result = analyze_sentiment(text)

        SentimentResult.objects.create(
            user=request.user,
            text=text,
            label=result["label"],
            score=result["score"]
        )

        return JsonResponse(result)