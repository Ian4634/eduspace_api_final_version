from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddVideoForm
from django.http import JsonResponse
from .models import Video, Category
from . import my_funcs

# Create your views here.

def index(request):
    if request.method == 'GET' and not ("submitted" in request.GET):
        context = {'form': AddVideoForm}
        return render(request, 'index.html', context)
    elif request.method == "POST":
        source = request.POST['source']
        category = Category.objects.get(name = request.POST['forma'])
        position = len(Video.objects.filter(category = category))
        Video.objects.create( source = source, category = category, position = position).save()
        return HttpResponseRedirect("?submitted=True")
    elif "submitted" in request.GET:
        return redirect(reverse('myapp:query'))


def query(request):
    goals = Category.objects.all()
    data = []
    for obj in goals:
        videos_objs = obj.video_set.all().order_by('position')
        source = []
        for videos_obj in videos_objs:
            source.append(videos_obj.source)
        data.append({
            'name':obj.name,
            'source':source,
            'description':''
        })

    return JsonResponse({"video": data})

def delete(request):
    if request.method == "POST":
        position = request.POST['position']
        category = Category.objects.get(name = request.POST['forma'])
        video = Video.objects.get(category = category, position = position).delete()

        # move forward all objs after the one deleted
        videos = Video.objects.filter(category = category)
        affected_video = videos[position:]

        for vid in affected_video:
            vid.position = int(vid.position) - 1
            vid.save()
        return redirect(reverse("myapp:query"))
    else:
        return render(request, 'delete.html', )

def edit(request):
    if request.method == "GET":
        return render(request, 'edit.html')

    elif request.method == "POST":
        category = Category.objects.get(name = request.POST['forma'])
        videos = Video.objects.filter(category=category).order_by('position')
        
        # rearrange order 
        original_position = request.POST['original_position']
        new_position = request.POST['new_position']
        
        # all index that will be affected
        my_funcs.move(videos, original_position, new_position)

        return redirect('/')

