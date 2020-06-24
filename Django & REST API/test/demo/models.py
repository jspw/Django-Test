from django.db import models

# Create your models here.

class Number (models.Model):
    bal1 = models.IntegerField(blank=True)


    # def __str__(self):
    #     return self.bal1


class Book(models.Model):
    status = (
        ("0","Paid"),
        ('1',"Free"),
        ("2","Unknown"),
    )
    
    Title = models.CharField(max_length=256,unique=True)

    Status = models.CharField(max_length=128,choices=status,null=True)

    Description = models.TextField(max_length=512,blank=True)

    # price = models.IntegerField(default=0,blank=False)
    # price = models.BigIntegerField(default=0,blank=False)
    # price = models.DecimalField(default=0,blank=False)
    Price = models.FloatField(default=0,blank=False)

    # Published = models.DateTimeField(auto_now_add=True)
    Published = models.DateTimeField(auto_now=True)
    # published = models.DateField(auto_now=True)
    # published = models.TimeField(auto_now=True)

    cover = models.FileField(upload_to="covers/",null=True)
    # cover = models.ImageField(upload_to="covers/",height_)

    number = models.OneToOneField(Number,null=True ,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.Title


class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="characters")


    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    books=models.ManyToManyField(Book,related_name="authors")

    def __str__(self):
        return self.name
