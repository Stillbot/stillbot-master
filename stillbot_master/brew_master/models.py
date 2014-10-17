from django.db import models
from django.utils import timezone


class Wash(models.Model):
    name            = models.CharField(max_length=255)
    ingredients     = models.ManyToManyField('IngredientMeasurement', null=True, blank=True)
    created_on      = models.DateTimeField(default=timezone.now(), help_text='The time the yeast was pitched')
    starting_sg     = models.DecimalField(max_digits=4, decimal_places=2, help_text='The SG right before the yeast was pitched', blank=True, null=True)
    ended_sg        = models.DecimalField(max_digits=4, decimal_places=2, help_text='The SG right before the wash was racked',  blank=True, null=True)
    pitching_temp   = models.DecimalField(max_digits=5, decimal_places=2, help_text='The temperature at which the yeast was pitched. This is your starting temperature.')
    procedure       = models.TextField(null=False, blank=False, help_text='The steps taken to prepare the wash')
    starting_ph     = models.DecimalField(max_digits=4, decimal_places=2, help_text='pH level when the wash started fermenting', blank=True, null=True)
    ending_ph     = models.DecimalField(max_digits=4, decimal_places=2, help_text='pH level when the wash finished fermenting', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)


class IngredientMeasurement(models.Model):
    MEASUREMENT_TYPES = (
            ('kg', 'kg'),
            ('g', 'g'),
            ('L', 'L'),
            ('mL', 'mL'),
            ('tbps', 'tbps'),
            ('tsp', 'tsp'),
            ('cup', 'cup'),
    )
    ingredient = models.ForeignKey('Ingredient')
    amount      = models.DecimalField(max_digits=6, decimal_places=2)
    measurement = models.CharField(choices=MEASUREMENT_TYPES, max_length=5)

    def __unicode__(self):
        return unicode('%s%s of %s' % (self.amount, self.measurement, self.ingredient))


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    place_of_origin = models.ForeignKey('Place', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)


class Place(models.Model):
    name        = models.CharField(max_length=255)
    latitude    = models.IntegerField(blank=True, null=True)
    longitude   = models.IntegerField(blank=True, null=True)
    address     = models.TextField(blank=True, null=True)
    contact     = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)


class Yield(models.Model):
    CUTS = (
        ('heads', 'Heads'),
        ('hearts', 'Hearts'),
        ('tails', 'Tails')
    )
    wash        = models.ForeignKey('Wash', related_name='yield', null=True, blank=True)
    cut         = models.CharField(choices=CUTS, max_length=6)
    amount      = models.DecimalField(max_digits=4, decimal_places=2)
    measurement = models.CharField(choices=IngredientMeasurement.MEASUREMENT_TYPES, max_length=5)

    def __unicode__(self):
        return unicode('%s%s of %s' % (self.amount, self.measurement, self.cut))
