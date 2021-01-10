from .models import ImagePost,Profile, Comments
from django import forms

#......
class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        exclude = ['user', 'pub_date', 'likes']

class AddProfileForm(forms.ModelForm):    
     class Meta:
         model= Profile
         exclude = ['user'] 

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['post', 'user']