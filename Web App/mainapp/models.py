from django.db import models

class Category(models.Model):

    category_name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return 'Category Name: {0} '.format(self.category_name)

class Item(models.Model):

    category_name = models.CharField(max_length=200, blank=False)
    item_name = models.CharField(max_length=200, blank=False)
    item_description = models.CharField(max_length=10000, blank=False)
    founder_name = models.CharField(max_length=200, blank=False)
    founder_number = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return 'Category Name: {0} Item Name: {1}'.format(self.category_name, self.item_name)
