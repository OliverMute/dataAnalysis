from django.db import models


# Create your models here.
class Pollutant(models.Model):
    """Pollution model for airpollution app"""
    name = models.CharField(max_length=10, primary_key=True)
    removed = models.BooleanField(default=False)
    """instead of delete actual entry in database, we set to true, so we 
    can filter it out. This way we don't remove data"""

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'pollutants'
        """tells Django that the plural of pollutant is pollutants"""


class Country(models.Model):
    """Country model for airpollution app"""
    name = models.CharField(max_length=100, unique=True)
    removed = models.BooleanField(default=False)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    altitude = models.FloatField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'
        """tells Django that the plural of country is countries"""


class PollutantEntry(models.Model):
    """PollutantEntry model for airpollution app"""
    pollutant = models.ForeignKey(Pollutant, on_delete=models.CASCADE, related_name='entries')
    """ pollutant, give me all your entries. Ex: pollutant PM10, give me all the entries that are 
    assigned to you"""
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='entries')
    year = models.IntegerField()
    city = models.CharField(max_length=50, default='', blank=True)
    """max_length = 50 -> look in Excel file to see the longest cities names."""
    station_code = models.CharField(max_length=20,default='', blank=True)
    station_name= models.CharField(max_length=100, default='', blank=True)
    pollution_level = models.IntegerField()
    units = models.CharField(max_length=10, default='', blank=True)
    station_type = models.CharField(max_length=20, default='',blank=True)
    station_area = models.CharField(max_length=20, default='', blank=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    altitude = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.pollutant.name} {self.year}'

    class Meta:
        verbose_name_plural = 'pollutant entries'

# Country
# City
# AirQualityStationEoICode
# AQStationName
# AirPollutant
# AirPollutionLevel
# UnitOfAirpollutionLevel
# AirQualityStationType
# AirQualityStationArea
# Longitude
# Latitude
# Altitude
