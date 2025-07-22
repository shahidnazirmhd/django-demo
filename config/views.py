from django.shortcuts import render
from django.urls import reverse

def home(request):
    challenges_url = reverse("challenges-index")  # Named route from your app
    return render(request, "config/index.html", {"render_url": challenges_url})