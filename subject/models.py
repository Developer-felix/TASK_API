from django.db import models

# Create your models here.

#create subject model
class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    added_by = models.ForeignKey('users.Acount', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'
