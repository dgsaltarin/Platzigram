"""Posts views"""

from django.shortcuts import render
from datetime import datetime

# Create your views here.

posts = [
    {
        'name':'Mont Blanc',
        'user':'Daniel Saltarin',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name':'Via Lactea',
        'user':'Daniel Saltarin',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903'
    }
]

def list_posts(request):
    """Retrn a list of posts"""    
    return render(request, 'feed.html', {'posts':posts})