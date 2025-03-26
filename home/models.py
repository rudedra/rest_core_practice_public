from django.db import models

# Create your models here.
class Color(models.Model):
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.color_name)



class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    fav_color = models.ForeignKey(Color, null=True, on_delete=models.CASCADE, related_name='color', blank=True, default=None)





    def __str__(self):
        return str(self.name)
    

