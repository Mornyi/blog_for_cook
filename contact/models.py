from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    # """ Класс модели обратной связи"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    # website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'
    
    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'Контакты'



class About(models.Model):
    # """ Класс модели страницы о нас """
    name = models.CharField(max_length=50, default='')
    text = RichTextField()
    mini_text = RichTextField()

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        return self.about_images.order_by('id')[1:]
    
    class Meta:
        verbose_name = 'информацию о нас'
        verbose_name_plural = 'информацию о нас'


class ImageAbout(models.Model):
    # """ Класс модели изображений страницы о нас """
    image = models.ImageField(upload_to="about/")
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_images")
    alt = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'Изображения'


class Social(models.Model):
    # """ Класс модели соцю сетей страницы о нас """
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)
    link = models.URLField()

    class Meta:
        verbose_name = 'Социальную сеть'
        verbose_name_plural = 'Социальные сети'









