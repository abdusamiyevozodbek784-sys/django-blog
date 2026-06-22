from django.http import HttpResponse

from django.http import HttpResponse
from .models import Post  # Bazadagi Post jadvalini chaqirdik

from django.shortcuts import render
from .models import Post


def home_page(request):
    # Ombordan hamma postlarni olamiz
    hamma_postlar = Post.objects.all()

    # Uni index.html shabloniga jo'natamiz
    return render(request, 'index.html', {'maqolalar': hamma_postlar})


def about_page(request):
    return HttpResponse("Bu loyiha Django darslari doirasida yaratildi.")

def about_page(request):
    return HttpResponse("Bu loyiha Django darslari doirasida yaratildi.")