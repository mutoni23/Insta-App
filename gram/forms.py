from .models import ImagePost
from django import forms
#......
class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        
        exclude = ['user', 'pub_date', 'likes']
        