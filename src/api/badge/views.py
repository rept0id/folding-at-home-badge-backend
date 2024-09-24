from django.shortcuts import render
import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime

@api_view(['GET'])
def badge_view(request, username):
    response = requests.get(f'https://api.foldingathome.org/user/{username}/stats')
    if response.status_code != 200:
        return HttpResponse(status=500)

    data = response.json()
    points = data.get('earned', 0)

    badge_url = f'https://img.shields.io/badge/Folding%40home-{points}-blue'

    badge_image = requests.get(badge_url)
    if badge_image.status_code != 200:
        return HttpResponse(status=500)

    res = HttpResponse(badge_image.content, content_type='image/svg+xml')

    res['Expires'] = format_datetime(datetime.now(timezone.utc) + timedelta(hours=12), usegmt=True)
    res['Cache-Control'] = 'public, max-age=43200'
    res['Pragma'] = 'no-cache'
    res['Last-Modified'] = format_datetime(datetime.utcnow(), usegmt=True)
    res['ETag'] = f'W/"{points}-{int(datetime.utcnow().timestamp())}"'

    return res
