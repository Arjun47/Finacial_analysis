from django.db import models

# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStampMixin):
    category = models.CharField(max_length=100)

    def __repr__(self):
        return self.category

    def __str__(self):
        return self.category
    

class Tr_type(models.Model):
    tr_type = models.CharField(max_length=10)

    def __repr__(self):
        return self.tr_type

    def __str__(self):
        return self.tr_type
    

class Transaction(TimeStampMixin):
    description = models.TextField(blank=True)
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    trans_type = models.ForeignKey(Tr_type, on_delete=models.RESTRICT)
