from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string
# Create your views here.


monthly_challenges = {
    "january": "Walk 10,000 steps every day!",
    "february": 
    #"Read a book every week!",
    None,
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


def index(request):
    months = _get_month_list()
    return render(request, "challenges/index.html", {"render_list_items": months})


def monthly_challenge_number(request, month):
    months = _get_month_list()
    if not 1 <= month <= 12:   #if month < 1 or month > len(months):
        return HttpResponseNotFound("<h1>Invalid month. Please try again.</h1>")

    redirect_month_name = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month_name])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    month_in_lower = month.lower()
    try:
        challenge_text = monthly_challenges[month_in_lower]
        return render(request, "challenges/challenge.html", {"render_text": challenge_text, "render_month": month_in_lower})
    except:
        return HttpResponseNotFound("<h1>Invalid month. Please try again.</h1>")


def _get_month_list():
    return list(monthly_challenges.keys())
