from django.db import models


class Thermistor(models.Model):
    CHOICES = (
            ('DS18B20', 'DS18B20'),
            ('DS18S20', 'DS18S20'),
    )
    model = models.CharField(choices=CHOICES, max_length=10)
    index = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'model=%s index=%s' % (self.model, self.index)

    @property
    def latest_temp(self):
        return Temperature.objects.filter(thermistor=self).last().temp


class Temperature(models.Model):
    thermistor = models.ForeignKey(Thermistor)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'thermistor=%s temp=%s' % (self.thermistor.index, self.temp)
