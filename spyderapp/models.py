from django.db import models

# Create your models here.
class Patron(models.Model):
	patron_id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=100, verbose_name="First Name")
	last_name = models.CharField(max_length=100, verbose_name="Last Name")
	date_of_birth = models.DateField()
	age = models.IntegerField(null=False)
	contact_number = models.CharField(max_length=100, verbose_name="Contact Number")
	current_address = models.TextField()
	email_id = models.EmailField(max_length=254)
	associated_names = models.TextField()
	previous_addresses = models.TextField()
	possible_relatives = models.TextField()
	possible_associates = models.TextField()
	possible_businesses = models.TextField()
	cases = models.TextField()
	links =  models.TextField()

	def __str__(self):
		return self.first_name

class Associates(models.Model):
	patron = models.ForeignKey('Patron', on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100, verbose_name="First Name")
	last_name = models.CharField(max_length=100, verbose_name="Last Name")
	date_of_birth = models.DateField()
	age = models.IntegerField(null=False)
	contact_number = models.CharField(max_length=100, verbose_name="Contact Number")
	current_address = models.TextField()
	email_id = models.EmailField(max_length=254)
	associated_names = models.TextField()
	previous_addresses = models.TextField()
	possible_relatives = models.TextField()
	possible_associates = models.TextField()
	possible_businesses = models.TextField()
	cases = models.TextField()
	links =  models.TextField()

	def __str__(self):
		return self.first_name
