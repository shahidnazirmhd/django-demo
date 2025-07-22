from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string
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


def index(request):
    list_items = ""
    months = _get_month_list()

    for month in months:
        cap_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{cap_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_number(request, month):
    months = _get_month_list()
    if not 1 <= month <= 12:   #if month < 1 or month > len(months):
        return HttpResponseNotFound("<h1>Invalid month. Please try again.</h1>")

    redirect_month_name = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month_name])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    month = month.lower()
    try:
        challenge_text = monthly_challenges[month.lower()]
        #respose_data = f"<h1>{challenge_text}</h1>"
        #respose_data = render_to_string("challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>Invalid month. Please try again.</h1>")
    #return HttpResponse(respose_data)
    return render(request, "challenges/challenge.html")


def _get_month_list():
    return list(monthly_challenges.keys())
