from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.http import require_http_methods

# Create your views here.
class ArticleView(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Articles')


# def index(request):
#     return render(
#         request,
#         'articles/index.html',
#         context={'app': 'article'},
#     )
