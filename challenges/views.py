from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


monthly_challenges = {
    "january": "Walk 10,000 steps every day!",
    "february": "Read a book every week!",
    "march": "Eat no sugar for the whole month!",
    "april": "Go for a run 3 times a week!",
    "may": "Drink 2 liters of water daily!",
    "june": "Meditate for 10 minutes every day!",
    "july": "Write in a journal every night!",
    "august": "No social media!",
    "september": "Learn a new skill!",
    "october": "Take a photo every day!",
    "november": "Practice gratitude daily!",
    "december": "Reflect on the year!"
}


def monthly_challenge(request, month):
    month = month.lower()
    if month in monthly_challenges:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f"<h1>{challenge_text}</h1>")
    else:
        return HttpResponseNotFound("<h1>Invalid month. Please try again.</h1>")
