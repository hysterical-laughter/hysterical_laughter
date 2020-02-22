from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import picture, like, comment

def pictures(request):
	if request.is_ajax():
		if request.method == "POST":
			N = int(request.POST['N_img'])#get how many imgs shown on user browser
		data = {
		'images': list(picture.objects.values_list('picture',flat=True).order_by('-date')[N:N+5])
		}
		return JsonResponse(data)

	context = {
	'images': picture.objects.values_list('picture',flat=True).order_by('-date')[:20]
	}
	return render(request, 'funny_pictures/pictures.html', context)
def image(request, image):
	if request.is_ajax():
		if request.user.is_authenticated:
			USER_ID = request.user.id
			if request.method == "POST" and image == "like":
				IMG = request.POST['img']
				if like.objects.filter(picture=IMG).count() == 0:
					liked = str([USER_ID])
					data = like(picture=IMG, likes=liked)
					data.save()
				else:
					q = like.objects.get(picture=IMG).likes
					print(q)
					q = eval(q)#return string to list
					if not USER_ID in q:
						q.append(USER_ID)
						print(IMG+' liked by: ',q)
						data = like.objects.get(picture=IMG)
						data.likes = str(q)
						data.save()
					else:
						print(request.user, ' aleady liked the post')
				context = {'status': 'ok'}
				return JsonResponse(context)
		else:
			context = {'status': 'no'}
			return JsonResponse(context)
	if request.method == "POST":
		if request.user.is_authenticated:
			pic = image
			user = request.user
			com = request.POST['comment']
			data = comment(username=user,picture=pic,comment=com)
			data.save()
		else:
			return redirect('/')
	Q = 'funny_images/'+str(image)
	IMG = picture.objects.get(picture=Q)
	comments = comment.objects.filter(picture=image).values('username','comment').order_by('-date')
	context = {
		'img': IMG,
		'com': comments
		}
	return render(request, 'funny_pictures/image.html', context)
