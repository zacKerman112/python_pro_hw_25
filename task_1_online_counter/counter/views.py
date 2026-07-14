from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Render the page with the real-time online users counter."""
    return render(request, "counter/index.html")
