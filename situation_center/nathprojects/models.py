from django.db import models


class Hospital(models.Model):
    year = models.IntegerField()
    deaths = models.IntegerField()

    def __str__(self):
        return f"{self.year} - {self.deaths} смертей"
