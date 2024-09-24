from django.shortcuts import render
import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def badge_view(request, username):
    # Fetch user data from Folding@home API
    response = requests.get(f'https://api.foldingathome.org/user/{username}/stats')
    if response.status_code != 200:
        return HttpResponse(status=500)

    data = response.json()
    points = data.get('earned', 0)

    # Generate badge URL
    badge_url = f'https://img.shields.io/badge/Folding%40home-{points}-blue'

    # Fetch the badge image
    badge_image = requests.get(badge_url)
    if badge_image.status_code != 200:
        return HttpResponse(status=500)

    # Return the badge image
    return HttpResponse(badge_image.content, content_type='image/svg+xml')
