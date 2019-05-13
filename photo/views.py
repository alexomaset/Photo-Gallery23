from django.shortcuts import render
from django.http import HttpResponse
from datetime as dt
from .models import *
# Create your views here.
def day_photos(request):
    date = dt.date.today()
    photos = Image.objects.all()

    return render(request, 'day_photos.html', {"date": date,"images":photos})

def image(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'image.html', {'image': image})

def search_results(request):
    # categories = Category.objects.all()
    # print(categories)

    if 'image' in request.GET and request.GET["image"]:
        search_input = request.GET.get("image")
        images = Image.search_by_category(search_input)
        message = f"{search_input}"
        print(search_term)

        return render(request, 'search.html',{"images":images,"message":message})

    else:
        message = "You haven't searched for any term"
        # context={"message":message}
        return render(request, 'search.html',{"message":message})

def display_images_categories(request):    
   photos = Image.category(1)
   return render(request, 'category.html', {"photos":photos})

def location_filter(request):

    photo = Image.location()
    locations = Location.objects.all()
    return render(request,'location.html',{"images":images,"locations":locations})