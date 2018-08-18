import graphene
from graphene_django.types import DjangoObjectType

from .models import Image

class ImageType(DjangoObjectType):
    class Meta:
        model = Image

class Query(object):
    images = graphene.List(
            ImageType,
            category=graphene.String())
    image = graphene.Field(
            ImageType,
            category=graphene.String(),
            name=graphene.String())

    def resolve_images(self, info, **kwargs):
        category = kwargs.get('category')

        if category is not None:
            return Image.objects.filter(category=category)
        else:
            return Image.objects.all().order_by('-publish_date')

    def resolve_image(self, info, **kwargs):
        category = kwargs.get('category')
        name = kwargs.get('name')

        if all([category, name]):
            return Image.objects.get(category__exact=category, name__exact=name)
