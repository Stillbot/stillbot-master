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
        return "index=%s model='%s' name='%s'" % (self.index, self.model, self.name or '')

    @property
    def latest_temp(self):
        return Temperature.objects.filter(thermistor=self).first().temp


class Temperature(models.Model):
    thermistor = models.ForeignKey(Thermistor, related_name='temperatures')
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'thermistor=%s temp=%s' % (self.thermistor.index, self.temp)

    class Meta:
        get_latest_by = 'created_on'
        ordering = ['-created_on']
