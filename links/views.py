from django.shortcuts import get_object_or_404, redirect

from links.models import ShortenedLink


def unshorten_url(request, shortened):
    link = get_object_or_404(ShortenedLink, shortened=shortened)
    return redirect(link.url)
