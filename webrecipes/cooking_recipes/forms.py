from django import forms

from .models import Recipes, Steps, Category, Comments


# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipes
#         fields = ['title', 'recipe_description', 'img', 'ctg']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update({'class': 'form-control py-4'})
#         self.fields['recipe_description'].widget.attrs.update({'class': 'form-control py-4'})
#         self.fields['img'].widget.attrs.update({'class': 'form-control py-4', 'size': (300, 200)})
#         self.fields['ctg'].widget.attrs.update({'class': 'form-control py-4'})

class RecipeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control py-4', 'size': (300, 200)}))
    ctg = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 widget=forms.Select(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = Recipes
        fields = ['title', 'description', 'image', 'ctg']


class StepForm(forms.ModelForm):
    step = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = Steps
        fields = ['step_description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text']
