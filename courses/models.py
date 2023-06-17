from django.db import models




class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    subtitle = models.CharField(max_length=50, unique=True)
    # description = models.TextField(max_length=255, blank=True)
    course_image = models.ImageField(upload_to='photos/', blank=True)
  

    

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


    def __str__(self):
        return self.title