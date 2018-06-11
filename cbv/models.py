from django.db import models
from django.urls import reverse

# Create your models here.


class FamilyMember(models.Model):
    LAST_NAME = (
        ('Dube', 'Dube'),
        ('Mabuto', 'Mabuto'),
        ('Kubiku', 'Kubiku'),
    )
    last_name = models.CharField(max_length=10, choices=LAST_NAME, default=True)
    first_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('cbv:family_update', kwargs={'pk': self.pk})
