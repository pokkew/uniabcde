from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField

class Course(TimeStampedModel):
    name = models.CharField("Nome do Curso", max_length=255)
    slug = AutoSlugField("Endereço do Curso",
        unique=True, always_update=False, populate_from="name")
    mensalidade = models.IntegerField("Valor da mensalidade", ) # ajustar esse field em pt-br depois

    def __str__(self):
        return self.name

class Student(TimeStampedModel):

    # class Course(models.TextChoices):
    #     ENG_COMP = "Eng. da Computação", "Eng. da Computação"
    #     DIREITO = "Direito", "Direito"
    #     PEDAGOGIA = "Pedagogia", "Pedagogia"

    name = models.CharField("Nome do Aluno", max_length=255)
    slug = AutoSlugField("Endereço do Aluno",
        unique=True, always_update=False, populate_from="name")
    phone = models.CharField("Telefone do Aluno", max_length=255)
    email = models.CharField("Email do Aluno", max_length=255)
    art = models.CharField("Registro Acadêmico do Aluno", max_length=255)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        """Return absolute URL to the Student Detail page."""
        return reverse(
            'students:detail', kwargs={"slug": self.slug}
        )

