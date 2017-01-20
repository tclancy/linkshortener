from django.test import TestCase

from links.models import ShortenedLink


class ShortenedLinkTests(TestCase):
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
        pass

    def test_querystring_encodes_properly(self):
        pass
