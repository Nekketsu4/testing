from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField, ArrayField, HStoreField
from django.contrib.postgres.fields import JSONField, CICharField


class PGSRoomReserving(models.Model):
    name = models.CharField(max_length=20, verbose_name='Помещение')
    reserving = DateTimeRangeField(verbose_name='Время резервирования')
    cancelled = models.BooleanField(default=False, verbose_name='Отменить'
                                                                'резервирование')


class PGSRubric(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    tags = ArrayField(base_field=models.CharField(max_length=20),
                      verbose_name='Теги')

    class Meta:
        indexes = [
            models.Index(fields=('name', 'description'),
                         name='i_pgsrubric_name_description',
                         opclasses=('varchar_pattern_ops',
                                    'bpchar_patter_ops'))
        ]


class PGSProject(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    platforms = ArrayField(base_field=ArrayField(
        models.CharField(max_length=20)),
    verbose_name='Использование платформы')


class PGSProject2(models.Model):
    nam = models.CharField(max_length=40, verbose_name='Название')
    platforms = HStoreField(verbose_name='Использование платформы')


class PGSProject3(models.Model):
    name = CICharField(max_length=40, verbose_name='Название')
    data = JSONField()


class ListStoreManager(models.Manager):
    '''переопределили диспетчер записей
    простыми словами если мы в контроллере напишем запрос типа:
    goods = ListStore.objects.all() - он теперь не просто выдаст список
    данных по увеличению id(по умолчанию именно так и идет),
     а сперва отсортирует по цене
    '''
    def get_queryset(self):
        return super().get_queryset().order_by('price')


class ListStore(models.Model):
    '''нужно явно объявить об переопределении диспетчера записей'''
    objects = ListStoreManager()

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


class Clothes(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')

    '''Делаем модель абстрактной
    говоря простыми словами мы родителя делаем временным, не настоящим
    и теперь все данные передаются на ее производную модель ChildClothes
    '''
    # class Meta:
    #     abstract = True


class ChildClothes(Clothes):
    '''Наследование модели от базовой Clothes'''
    content = models.TextField(null=True, blank=True, verbose_name='Описание товара')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')

    '''Прокси модель - своего рода временная модель которая работает на свою
    базовую модель Clothes(отдельно для этой модели в БД не создается таблица)
    '''
    # class Meta:
    #     proxy = True


class Firms(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название фирмы')
    clothes_firms = models.ManyToManyField(Clothes, through='JoinTheseModels',
                                           through_fields=('firm', 'clothes'))


class JoinTheseModels(models.Model):
    firm = models.ForeignKey(Firms, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)



