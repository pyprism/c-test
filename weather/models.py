from django.db import models


class CityNameManager(models.Manager):
    def get_all_city(self):
        return super().order_by('-id')

    def get_city_by_pk(self, pk):
        return super().filter(pk=pk).values('name').first()


class CityName(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CityNameManager()

    def __str__(self):
        return self.name
