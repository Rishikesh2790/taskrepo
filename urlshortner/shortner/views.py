from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
import random
from django.utils import baseconv
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ShortUrl
from .forms import URLForm
from .shortnertoken import Shortnerclass
from .serializers import ShortUrlSerializer

# Create your views here.
def create(request):
    token = ''
    # print(baseconv.base62.encode(367891))
    if request.method == 'POST':
        obj = ShortUrl.objects.all()
        fm = URLForm(request.POST)
        if fm.is_valid():
            Url = fm.save(commit = False)
            token = Shortnerclass().generateToken()
            Url.short_url = token
            Url.save()
    else:
        fm = URLForm()
        obj = ShortUrl.objects.all()
    return render(request,'Home.html',{'form':fm,'token':token,'obj':obj})

@csrf_exempt
@api_view(['POST'])
def createAPI(request):
	if request.method == 'POST':
		token = ''
		serializer = ShortUrlSerializer(data=request.data)
		if serializer.is_valid():
			token = Shortnerclass().generateToken()
			Url = serializer.save()
			Url.short_url = token
			Url.save()
			return JsonResponse({ 'status':status.HTTP_201_CREATED,'data':serializer.data,})
		return JsonResponse(serializer.errors,safe=False)

def list(request):
    obj = ShortUrl.objects.all()
    a = []
    for i in obj:
        a.append(i.short_url)
    data = {'short_url':a}
    return JsonResponse({'data':data})

def detail(request,token):
    obj = ShortUrl.objects.filter(short_url=token)[0]
    data = {'long_url':obj.long_url}
    return JsonResponse({'data':data})

def delete(request,token):
    obj = ShortUrl.objects.filter(short_url=token)[0]
    obj.delete()
    return JsonResponse({'Successfully delete'})


def display(request,token):
    l_url = ShortUrl.objects.filter(short_url=token)[0]
    return redirect(l_url.long_url)