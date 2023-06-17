from django.shortcuts import get_object_or_404, redirect, render
from . models import Course
from .forms import CourseForm
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

def short_term_courses(request):
    courses = Course.objects.all()
    paginator = Paginator(courses,3)
    page = request.GET.get('page')
    paged_courses = paginator.get_page(page)

    context ={
        'courses':paged_courses,
    }

  
    return render(request,'short-course-view.html',context)


def short_course_create(request):
        
        if request.method == 'POST':
              form = CourseForm(request.POST,request.FILES)
              if form.is_valid():
                form.save()
                return redirect('short_term_courses')
        else:
            form = CourseForm()

        return render(request,'short-course-create.html',{'form':form})


def edit_course(request,pk):
     course = get_object_or_404(Course,pk=pk)
     title = course.title
     subtitle = course.subtitle
     course_image = course.course_image
     context ={
          'title':title,
          'subtitle':subtitle,
          'course_image':course_image,
     }
     return render(request,'edit-page.html',context)
        
    
def course_delete(request,pk):
     course = get_object_or_404(Course,pk=pk)
     course.delete()
     return redirect('short_term_courses')
     

def search(request):
     
     if 'keyword' in request.GET:
          keyword = request.GET['keyword']
          if keyword:
               courses = Course.objects.filter(Q(title__icontains=keyword) | Q (subtitle__icontains=keyword))
     context ={
        'courses':courses,
    }
     return render(request,'short-course-view.html',context)