from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Render the page for sending and receiving push notifications."""
    return render(request, "notifications/index.html")
