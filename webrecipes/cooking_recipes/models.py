from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'ctg_slug': self.slug})


class Recipes(models.Model):
    recipe_id = models.AutoField(primary_key=True, verbose_name="Номер рецепта")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = AutoSlugField(populate_from='title', max_length=255, unique=True, db_index=True, verbose_name='URL')
    recipe_description = models.TextField(max_length=255, blank=True, verbose_name="Краткое описание")
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Изображение')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')

    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'rec_slug': self.slug})


class Steps(models.Model):
    step_id = models.AutoField(primary_key=True, verbose_name="Номер шага")
    step_description = models.TextField(max_length=255, blank=True, verbose_name="Шаг рецепта")

    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True, verbose_name="Номер комментария")
    comment_text = models.TextField(max_length=255, blank=False, verbose_name="Комментарий")

    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
