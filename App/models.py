from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=100)
    head=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    Sname=models.CharField(max_length=100)
    age=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='student')
    # "related_name" attribute is used to fetch the info of child table with the help of parent table, without using child table.

    def __str__(self) -> str:
        return self.Sname