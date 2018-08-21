import graphene
from graphene_django.types import DjangoObjectType

from .models import Category, Image

class ImageType(DjangoObjectType):
    class Meta:
        model = Image

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class Query(object):
    images = graphene.List(
            ImageType,
            category=graphene.String())

    categories = graphene.List(
            CategoryType
    )

    def resolve_images(self, info, **kwargs):
        category = kwargs.get('category')

        if category is not None:
            return Image.objects.filter(category__name=category)
        else:
            return Image.objects.all().order_by('-publish_date')

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()
