from rest_framework import status
from rest_framework.test import APITestCase

from links.models import ShortenedLink


class ShortenedLinkTests(APITestCase):
    def setUp(self):
        self.shortened_link = ShortenedLink(url="http://example.org")
        self.shortened_link.save()

    def test_shortening_works(self):
        self.assertIsNotNone(self.shortened_link.shortened)

    def test_hit_increment(self):
        """
        Just make sure db logic works here
        """
        hits = self.shortened_link.record_view()
        self.assertEqual(1, hits)
        self.assertEqual(1, ShortenedLink.objects.get(pk=self.shortened_link.id).hits)

    def test_unicode_urls(self):
        url = "https://twitter.com"
        response = self.client.post("/links/", {"url": url}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ShortenedLink.objects.count(), 1)
        self.assertTrue(ShortenedLink.objects.filter(url=url).exists())

    def test_querystring_encodes_properly(self):
        pass
