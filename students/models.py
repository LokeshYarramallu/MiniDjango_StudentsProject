from django.db import models

# Create your models here.


class Student(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    rollno = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    batch = models.CharField(max_length=5)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to="profileimg")

    def __str__(self):
        return self.name
