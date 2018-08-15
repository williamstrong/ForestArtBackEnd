from django.db import models

def file_path(instance, filename):
    return Image.file_path(instance, filename)

class Image(models.Model):
    """Model for images on the site.

    Images will automatically be uploaded to S3 as defined in the project settings.
    Name is derived from title and will be created in the clean method.

    The name and category fields define the file_path. When Either of these change the
    file_path needs to change as well.
    """

    title = models.CharField(max_length=100, help_text="Title of Image")
    name = models.CharField(
            max_length=100,
            editable=False,
            help_text="Name of Image"
    )
    category = models.CharField(
            max_length=100,
            default = 'other',
            help_text="Category of Image"
    )

    source_standard = models.ImageField(
            upload_to=file_path,
            help_text="URL of the image location (S3... etc.)"
    )
    source_small = models.ImageField(
            upload_to=file_path,
            blank=True,
            help_text="URL of the image location (S3... etc.)"
    )
    source_large = models.ImageField(
            upload_to=file_path,
            blank=True,
            help_text="URL of the image location (S3... etc.)"
    )

    description = models.TextField(
            help_text="Description of the image. Used for alt text if no alt text is provided."
    )
    alt_text = models.TextField(help_text="Alt text")

    creation_date = models.DateTimeField('date created', auto_now_add=True)
    publish_date = models.DateTimeField('date published', auto_now_add=True)

    file_path = lambda instance, filename: 'images/{0}/{1}'.format(instance.category, instance.name)

    def clean(self):
        self.name = self.title.replace(' ', '_').lower()

    def __str__(self):
        return '{0} at S3 path {1}/{2}'.format(self.title, self.category, self.name)
