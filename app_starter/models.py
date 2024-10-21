from django.db import models
from django.contrib.auth.models import User


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
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# One to many
class ChaiReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chai = models.ForeignKey(
        ChaiVariety, on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.chai.name}"


# Many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name


# One to one
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        ChaiVariety,
        on_delete=models.CASCADE,
        related_name="certificate",
    )
    certificate_number = models.CharField(max_length=50)
    issue_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()

    def __str__(self):
        return f"Certificate for {self.chai.name}"
