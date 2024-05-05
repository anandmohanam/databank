from django.db import models


class Data(models.Model):      # Renamed model to avoid underscore
    name = models.CharField(max_length=250)
    age = models.IntegerField(null=True)
    place = models.TextField(max_length=250)
    job = models.TextField(max_length=250)
    education = models.TextField(max_length=250)
    number = models.IntegerField()  # Removed max_length
    email = models.TextField(null=True)
    facebook=models.TextField(null=True)
    instagram=models.TextField(null=True)
    dob=models.DateField()
    img=models.ImageField(upload_to='pics',null=True,blank=True)
    car_or_two_wheel_number=models.CharField(max_length=250)

    def __str__(self):
        return self.name
