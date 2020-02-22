from django.shortcuts import render
from django.http import HttpResponse
from .models import video
# Create your views here.
def videos(request):
	context = {
	'videos'		: video.objects.values_list('video',flat=True).order_by('-date'),
	'description'	: video.objects.values_list('description',flat=True),
	}
	return render(request, 'Funny_Videos/videos.html', context)
