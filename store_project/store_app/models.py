from django.db import models

class ListStore(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('RubricStore', null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика', related_name='entry')


    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-published']


class RubricStore(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


