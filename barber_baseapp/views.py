from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from django.core.paginator import Paginator

def main_page(request):
    return render(request, 'barber_baseapp/main.html')