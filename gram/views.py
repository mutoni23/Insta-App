from django.shortcuts import render,redirect
from .forms import ImagePostForm
from django.contrib.auth.decorators import login_required
from .models import ImagePost

# Create your views here.

def index(request):
    '''
    function to display the index page
    '''
    images = ImagePost.objects.all()
    return render(request, 'index.html', {"images": images})
#.....
@login_required(login_url='/accounts/login/')
def new_post(request):
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