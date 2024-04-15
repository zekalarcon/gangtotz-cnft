from distutils.command.upload import upload
from io import BytesIO
from django.db import models
from PIL import Image
from django.core.files import File

class Nft(models.Model):

    minted = models.BooleanField(default=False)
    ipfs_CID = models.CharField(max_length=300, default='', null=False)
    name= models.CharField(max_length=300, null=False, blank=False)
    background = models.CharField(max_length=300, null=False, blank=False)
    head = models.CharField(max_length=300, null=False, blank=False)
    tone = models.CharField(max_length=300, null=False, blank=False)
    gang = models.CharField(max_length=300, null=False, blank=False)
    expression = models.CharField(max_length=300, null=False, blank=False)
    hair = models.CharField(max_length=300, null=False, blank=False)
    hair_color = models.CharField(max_length=300, null=False, blank=False)
    shoes = models.CharField(max_length=300, blank=True, null=True)
    right_hand = models.CharField(max_length=300, blank=True, null=True)
    left_hand = models.CharField(max_length=300, blank=True, null=True)
    ear_style = models.CharField(max_length=300, blank=True, null=True)
    neck_style = models.CharField(max_length=300, blank=True, null=True)
    chest_style = models.CharField(max_length=300, blank=True, null=True)
    face_style = models.CharField(max_length=300, blank=True, null=True)
    mark = models.CharField(max_length=300, blank=True, null=True)
    total_features = models.IntegerField(default=0, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='')

    class Meta:
        ordering = ('name',)

    def _str_(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
 
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300,300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail