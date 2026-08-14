from django.db import models


DIFFICULTY_CHOICES = [
    ("easy", "Easy"),
    ("moderate", "Moderate"),
    ("hard", "Hard"),
    ("expert", "Expert"),
]


class Trail(models.Model):
    name = models.CharField(max_length=200)
    distance_km = models.DecimalField(max_digits=6, decimal_places=2)
    elevation_gain = models.IntegerField()

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
    )

    is_open = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)

    park = models.ForeignKey(
        "Park",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Park(models.Model):
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

    def __str__(self):
        return self.name