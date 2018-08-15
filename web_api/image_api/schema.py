import graphene
from graphene_django.types import DjangoObjectType

from .models import Image

class ImageType(DjangoObjectType):
    class Meta:
        model = Image

class Query(object):
    all_images = graphene.List(ImageType)

    def resolve_all_images(self, info, **kwargs):
        return Image.objects.all()
