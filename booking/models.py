from django.db import models
import datetime
from django.contrib.auth.models import User
from properties.models import Property

# Create your models here.
class Booking(models.Model):
    
    book_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    book_check_in = models.DateField(("Date"), default=datetime.date.today)
    book_check_out = models.DateField(("Date"), default=datetime.date.today)

    # def __str__(self):
    #     return f'{self.book_user} booked From {self.book_check_in} To {self.book_check_out}'


