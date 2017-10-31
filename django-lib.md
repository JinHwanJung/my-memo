# simple-history 
- pip install django-simple-history
- usage : from_history.models import HistoricalRecords
- docs : https://django-simple-history.readthedocs.io/en/latest/\

# json
- from json import loads as json_loads

# copy
- from copy import deepcopy

# djang settings 
- from django.conf import settings

# django contrib postgres
- from django.contrib.postgres.fields import JSONField <br/>
: JSON 인코딩된 데이터를 저장하는 필드.
- from django.contrib.postgres.search import SearchVectorField, SearchVector

# django db models
- from django.db.models import CharField, DateTimeField, IntegerField, BooleanField, SmallIntegerField, F, Model, \
    ForeignKey, PROTECT, ManyToManyField, BigIntegerField, EmailField, CASCADE, UUIDField, TextField

# django db models fields related_descriptors     
- from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor

# django db utils
from django.db.utils import IntegrityError

# django utils
from django.utils.timezone import now

# django db
from django.db import transaction
