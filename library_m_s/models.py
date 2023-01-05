from django.db import models
from django.db.models import Max
# Create your models here.

# tablka boogaagta


class books(models.Model):
    name = models.CharField(max_length=100)
    auth = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    #
    # Set the quantity
    def set_quantity(self, quantity):
        self.quantity = quantity

    # Get the name
    def get_name(self):
        return self.name

    # Get the most quantity
    @classmethod
    def get_quantity(cls, self):
        return cls.objects.all().aggregate(total=Max(self.quantity))


# studen as user table
class student(models.Model):

    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.address

    # Concat students name
    # Get ful name
    def get_name(self):
        return self.fname + ' ' + self.mname + ' ' + self.lname


# narow table
class narrow_book(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    book = models.ForeignKey(books, on_delete=models.CASCADE, default=None)
    student = models.ForeignKey(
        student, on_delete=models.CASCADE, default=None)

    # Return date as a string

    def return_date_as_string(self):
        return {
            'start': self.start_date.strftime("%Y-%m-%d"),
            'end': self.end_date.strftime("%Y-%m-%d"),
        }


# staf_user
class staf_user(models.Model):
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.IntegerField()
