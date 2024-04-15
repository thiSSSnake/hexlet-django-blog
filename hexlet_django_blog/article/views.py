from django.shortcuts import render
from django.http import Http404
from django.views.decorators.http import require_http_methods
# from .models import Article

def index(request, tags, article_id):
    return render(
        request,
        'articles/index.html',
        context={
            'tags': tags,
            'article_id': article_id,
            }
    )
