from django.db import models


# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KL", "KIWI"),
        ("PL", "PLAIN"),
        ("PL", "PLAIN"),
        ("EL", "ELAICHI"),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="chai_images/")
    date_added = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default="PL")

    def __str__(self):
        return self.name
