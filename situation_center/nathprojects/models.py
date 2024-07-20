from django.db import models


class Hospital(models.Model):
    year = models.IntegerField()
    deaths = models.IntegerField()

    class Meta:
        verbose_name = 'Здравоохранение'
        verbose_name_plural = 'Здравоохранение'

    def __str__(self):
        return f"{self.year} - {self.deaths} смертей"
