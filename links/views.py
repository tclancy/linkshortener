from django.shortcuts import get_object_or_404, redirect
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from links.models import ShortenedLink
from links.serializers import ShortenedLinkSerializer


def unshorten_url(request, shortened):
    link = get_object_or_404(ShortenedLink, shortened=shortened)
    link.record_view()
    return redirect(link.url)


class ShortenedLinkList(APIView):
    def get(self, request, format=None):
        ShortenedLinks = ShortenedLink.objects.all()
        serializer = ShortenedLinkSerializer(ShortenedLinks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShortenedLinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShortenedLinkDetail(APIView):
    def get_object(self, pk):
        try:
            return ShortenedLink.objects.get(pk=pk)
        except ShortenedLink.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sl = self.get_object(pk)
        serializer = ShortenedLinkSerializer(sl)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sl = self.get_object(pk)
        serializer = ShortenedLinkSerializer(sl, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        return Response(status=status.HTTP_400_BAD_REQUEST)
