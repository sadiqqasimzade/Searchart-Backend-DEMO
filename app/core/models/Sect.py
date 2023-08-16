from django.db import models


class Sect(models.Model):
    sector = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.sector

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"
