from django import forms 
from .models import Car, Brand,Comment

class BrandForm(forms.ModelForm):
        class Meta:
                model=Brand
                fields="__all__"

class CarForm(forms.ModelForm):
        class Meta:
                model = Car
                fields="__all__"
                
                
class CommentForm(forms.ModelForm):
        class Meta:
                model=Comment
                fields=['name', 'comment_text']