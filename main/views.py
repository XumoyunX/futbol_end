from django.shortcuts import render, redirect
from main.models import *
from main.formas import *




def index(request):
    region = Region.objects.all()

    ctx = {
        "region": region
    }
    return render(request, "main/index.html", ctx)




def region(request, pk):
    tuman = District.objects.filter(region_id=pk)

    ctx = {
        "tuman": tuman
    }

    return render(request, "main/index.html", ctx)



def reklama(request, pk):
    post_re = Post.objects.filter(district_id=pk)

    ctx = {
        "post_re": post_re
    }
    return render(request, "main/region.html", ctx)



def malumotlar(request):
    malumot = Post.objects.all()
    cxt = {
        "malumot": malumot
    }

    return render(request, "main/barcha_post.html", cxt)



def post(request):
    model = Post()
    print(model)
    form = PostFrom(request.POST, request.FILES, instance=model)
    post_r = Region.objects.all()
    dic_r = District.objects.all()
    # print(form)
    if request.POST:
        if form.is_valid():
            print(form)
            form.save()
            return redirect('malumotlar')
        else:
            print(form.errors)
    ctx = {
        "form": form,
        "post_r": post_r,
        "dic_r": dic_r
    }
    return render(request, 'main/post.html', ctx)