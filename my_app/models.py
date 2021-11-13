from django.db import models
from mysite.validators import global_file_validator
from .validators import local_file_validatorX

class Test(models.Model):
    file = models.FileField(validators=[global_file_validator, local_file_validatorX])
    #file = models.FileField(validators=[local_file_validatorX])
