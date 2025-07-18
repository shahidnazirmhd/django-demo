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

def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())

    if 1 <= month <= 12:    #if month >= 1 and month <= 12:
        month_name = months[month - 1]
        challenge_text = monthly_challenges[month_name]
        return HttpResponse(f"<h1>{month_name.capitalize()}: {challenge_text}</h1>")
    else:
        return HttpResponseNotFound("<h1>Invalid month. Please provide a number between 1 and 12.</h1>")


def monthly_challenge(request, month):
    month = month.lower()
    if month in monthly_challenges:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f"<h1>{challenge_text}</h1>")
    else:
        return HttpResponseNotFound("<h1>Invalid month. Please try again.</h1>")
