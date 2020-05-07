from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from ..students.models import  Course

class Teacher(TimeStampedModel):

    name = models.CharField("Nome do Professor", max_length=255)
    slug = AutoSlugField("Endereço do Professor",
        unique=True, always_update=False, populate_from="name")
    phone = models.CharField("Telefone do Professor", max_length=255)
    email = models.CharField("Email do Professor", max_length=255)
    salary = models.PositiveIntegerField(verbose_name="Salário do Professor")
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    #start_date = models.DateField(verbose_name="Data de Início",auto_now=False, auto_now_add=False)
    start_date = models.DateField(verbose_name="Data de Início",auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        """Return absolute URL to the Teacher Detail page."""
        return reverse(
            'teachers:detail', kwargs={"slug": self.slug}
        )
    
    
