from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
    """
    Class that contains location details of the image posted
    """
    location = models.CharField(max_length = 15)
    # description = models.TextField()

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def del_location(self):
        self.delete()
    def update_location(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)     


    

class Category(models.Model):
    """
    Class that contains the category details of the image posted
    """
    category = models.CharField(max_length = 15)
    # description = models.TextField()

    def __str__(self):
        return self.category

    def save_cat(self):
        self.save()

    def del_cat(self):
        self.delete()
    def update_location(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)      



class Image(models.Model):
    """
    Class that contains details concerning the image itself
    """
    
    photo = models.ImageField(upload_to = 'gallery/')
    name = models.CharField(max_length = 25)
    description = models.TextField()
    locate = models.ForeignKey(Location)
    categ = models.ForeignKey(Category)
    # up_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.save()
    def update_location(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)    

    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(id=id)
        return image

    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(id=id)
        return image

    @classmethod
    def filter_by_location(cls, id):
        image = Image.objects.filter(location_id=id).all()
        return image

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def search_by_category(cls,seacrh_input):
        images = cls.objects.filter(name=name)
        return images
    def location (cls, id):
        image = Image.objects.filter(name).all()
        return image
    @classmethod   
    def category (cls, id):
        image = Image.objects.get(name)
        return image 