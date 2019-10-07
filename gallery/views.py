from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Location,categories

# Create your views here.
def gallery(request):
    images = Image.all_images()
    locations = Location.objects.all()
    return render(request, 'index.html', {"images":images,"locations":locations})

def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    images = Image.objects.filter(location = selected_location.id)
    return render(request, 'location.html', {"location":selected_location,"locations":locations,"images":images})


def search(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        search_term = request.GET.get("category")
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request,'search.html',{"images":searched_images,"category":search_term})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {"message": message})
