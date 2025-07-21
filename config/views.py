from django.http import HttpResponse
from django.urls import reverse

def home(request):
    challenges_url = reverse("challenges-index")  # Named route from your app
    response_data = f"""
        <h1>Welcome to the Monthly Challenges Project!</h1>
        <p>Click <a href="{challenges_url}">here</a> to navigate to the challenges.</p>
    """
    return HttpResponse(response_data)