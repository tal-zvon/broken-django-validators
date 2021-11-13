from django.db import models
from mysite.validators import global_file_validator
from .validators import local_file_validator

class Test(models.Model):
    file = models.FileField(validators=[global_file_validator, local_file_validator])
