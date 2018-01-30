from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, primary_key = True, related_name = "profile", on_delete = models.CASCADE)
	weight = models.DecimalField("Weight", max_digits = 5, decimal_places = 2)
	bf = models.DecimalField("Body Fat", max_digits = 4, decimal_places = 2)

class Goal(models.Model):
	profile = models.OneToOneField(Profile, related_name = "goal", on_delete = models.CASCADE)
	weight = models.DecimalField("Goal Weight", max_digits = 5, decimal_places = 2)
	bf = models.DecimalField("Goal Body Fat", max_digits = 4, decimal_places = 2)	

class Nutrient(models.Model):
	name = models.CharField("Nutrient Name", max_length = 20)
	desc = models.TextField("Description", max_length = 200)

class Nutrient_Goals(models.Model):
	nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
	amount = models.IntegerField("Amount")

class Nutrient_Reg(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateField()
	nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
	amount = models.IntegerField("Amount")

class Meal(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateField()
	text = models.TextField("Meal Description", max_length = 1500)

class Build(models.Model):
	commit = models.CharField(primary_key = True, max_length=128)
	date = models.DateField()