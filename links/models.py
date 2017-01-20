from __future__ import unicode_literals

from django.db import models
from django.db.models import F
from django.utils.timezone import now as tz_now

# set to a ShortURL object below
SHORTENER = None


class ShortenedLink(models.Model):
    url = models.URLField(db_index=True, max_length=255)
    mobile_url = models.URLField(blank=True, max_length=255)
    tablet_url = models.URLField(blank=True, max_length=255)
    shortened = models.CharField(max_length=20, unique=True, db_index=True, blank=True, null=True)
    created = models.DateTimeField(default=tz_now)
    hits = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.url

    def record_view(self):
        """
        Update hit count in database, increment locally to reflect change without having to requery
        """
        self.hits = F("hits") + 1
        self.save()
        self.hits += 1

    def save(self, *args, **kwargs):
        """
        Create a shortened hash based on the database id after saving. To be able to do it after the initial save
         while still enforcing uniqueness we need to change blank to NULL to work around the CharField restriction
        """
        if self.shortened == "":
            self.shortened = None
        super(ShortenedLink, self).save(*args, **kwargs)
        if not self.shortened:
            self.shortened = SHORTENER.encode(self.id)
            super(ShortenedLink, self).save(*args, **kwargs)


# ShortURL (https://github.com/delight-im/ShortURL)
# Copyright (c) delight.im (https://www.delight.im/)
# Licensed under the MIT License (https://opensource.org/licenses/MIT)

class ShortURL(object):
    """
    ShortURL: Bijective conversion between natural numbers (IDs) and short strings

    ShortURL.encode() takes an ID and turns it into a short string
    ShortURL.decode() takes a short string and turns it into an ID

    Features:
    + large alphabet (51 chars) and thus very short resulting strings
    + proof against offensive words (removed 'a', 'e', 'i', 'o' and 'u')
    + unambiguous (removed 'I', 'l', '1', 'O' and '0')

    Example output:
    123456789 <=> pgK8p
    """

    _alphabet = '23456789bcdfghjkmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ-_'
    _base = len(_alphabet)

    def encode(self, number):
        string = ''
        while number > 0:
            string = self._alphabet[number % self._base] + string
            number //= self._base
        return string

    def decode(self, string):
        number = 0
        for char in string:
            number = number * self._base + self._alphabet.index(char)
        return number

SHORTENER = ShortURL()
