from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, 'cooking_recipes/index.html')


def about(request):
    return render(request, 'cooking_recipes/about.html')

# class Index(View):
#     def get(self, request):
#         return HttpResponse('Hello, world!')
#
#     def post(self, request):
#         return HttpResponse('Got a POST request')
