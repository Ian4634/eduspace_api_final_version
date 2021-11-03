from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddVideoForm
from django.http import JsonResponse
from .models import Video


# Create your views here.

def index(request):
    if request.method == 'GET' and not ("submitted" in request.GET):
        context = {'form': AddVideoForm}
        return render(request, 'index.html', context)
    elif request.method == "POST":
        name = request.POST['name']
        source = request.POST['source']
        description = request.POST['description']
        category = request.POST['category']
        Video.objects.create(name = name, source = source, descriptions = description,category = category).save()
        return HttpResponseRedirect("?submitted=True")
    elif "submitted" in request.GET:
        return redirect(reverse('myapp:query'))


def query(request):
    retrieve = Video.objects.all()  # a list of objects
    data = []
    for obj in retrieve:
        data.append({
            'name': obj.name,
            'source': obj.source,
            'description': obj.descriptions
        })

    return JsonResponse({"video": data})

def delete(request):
    if request.method == "POST":
        name = request.POST['name']
        objs = Video.objects.filter(name=name)
        for obj in objs:
            obj.delete()
        return redirect(reverse("myapp:query"))
    else:
        return render(request, 'delete.html', )
