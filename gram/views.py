from django.shortcuts import render,redirect
from .forms import ImagePostForm
from django.contrib.auth.decorators import login_required
from .models import ImagePost,Profile
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    '''
    function to display the index page
    '''
    images = ImagePost.objects.all()
    for image in images:
        if request.method=='post' and 'comment' in request.image:
            comment=Comment(comment=request.image.get("comment"),
                            image=int(request.image.get("image")),
                            user=request.image.get("user"),
                            count=0)
            comment.save()
            comment.count=F('count')+1
            return redirect('index')
        elif request.method=='post' and 'image' in request.image:
            posted=request.image.get("image")
            for image in images:
                if (int(image.id)==int(posted)):
                    image.likes+=1
                    image.save()
            return redirect('index')
    return render(request, 'index.html', {"images": images})
#.....
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        profile = None
        search_term = request.GET.get("user")
        current_user = User.objects.filter(username__icontains = search_term)
        for item in current_user:
            profile = Profile.objects.filter(user=item)
        print(current_user)
        message = f"{search_term}"
        
        return render(request, 'search.html',{"results": profile, "user": current_user, "message":message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = ImagePostForm()
    return render(request, 'new_image.html', {"form": form})

def like_image(request,image_id):
    current_user = request.user
    image = ImagePost.objects.filter(id=image_id).first()
    ImagePost.objects.filter(id=image_id).update(likes=image.likes+1)
    return redirect('home')