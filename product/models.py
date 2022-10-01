from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    desc = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    desc = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category="color", is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category="size", is_active=True)


variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)


class Variation(models.Model):
    product = models.ManyToManyField(Product)
    variation_category = models.CharField(
        max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)


    objects = VariationManager()

    def __str__(self):
        return self.variation_value
