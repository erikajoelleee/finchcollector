from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def _str_(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'finch_id': self.id})
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    finch = models.ForeignKey(
        Finch, 
        on_delete=models.CASCADE
        )
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    class Meta:
     ordering = ['-date']