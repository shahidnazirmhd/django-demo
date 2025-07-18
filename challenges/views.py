from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    if not 1 <= month <= 12:   #if month < 1 or month > len(months):
        return HttpResponseNotFound("<h1>Invalid month. Please try again.</h1>")

    redirect_month_name = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month_name)


def monthly_challenge(request, month):
    month = month.lower()
    try:
        challenge_text = monthly_challenges[month.lower()]
    except:
        return HttpResponseNotFound("<h1>Invalid month. Please try again.</h1>")
    return HttpResponse(f"<h1>{challenge_text}</h1>")
