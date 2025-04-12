from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    author = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name="posts",
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name="post")
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.category.slug, self.slug])

    def get_recipes(self):
        return self.recipes.all()

    def get_comments(self):
        return self.comment.all()

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(
        Post,
        related_name="recipes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'Рецепты'


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name="автор"
    )
    message = models.TextField(
        max_length=500,
        blank=False,
        verbose_name="сообщение"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="дата создания"
    )
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name="пост"
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']  # новые комментарии сверху

    def __str__(self):
        return f"Комментарий от {self.author.username} ({self.created_at})"
