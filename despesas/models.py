from django.db import models

import uuid

class Despesa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    saida = models.DecimalField(max_digits=10, decimal_places=2)

