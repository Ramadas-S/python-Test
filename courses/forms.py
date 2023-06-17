from django import forms
from .models import Course



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'subtitle', 'course_image']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
        'course_image': forms.FileInput(attrs={'class': 'dropify','data-bs-height':"180"}),
    }
      
