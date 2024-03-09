from django.db import models

class GreggorTypes(models.TextChoices):
    """ENUM for greggor logo types"""
    NORMAL: str = "normal"
    DISTRAUGHT: str = "distraught"
    SAD: str = "sad"
    SLEEPY: str = "sleepy"
    PARTY: str = "party"
    CUPID: str = "cupid"
    GRAD: str = "grad"