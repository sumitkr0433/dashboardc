from django.db import models
from django.conf import settings


class Profile(models.Model):
	GENDER=(('male','Male'),('female','Female'),)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	months = models.CharField(max_length=250)
	year = models.CharField(max_length=250)
	mobile = models.CharField(max_length=250)
	photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
	currency_type=models.CharField(blank=True, null=True)
	gender=models.CharField(max_length=10,choices=GENDER,default='male')
	nickname = models.CharField(max_length=250)
	website = models.CharField(max_length=250)
	street_address = models.CharField(max_length=250)
	city = models.CharField(max_length=250)
	state = models.CharField(max_length=250)
	pincode = models.CharField(max_length=250)
	country = models.CharField(max_length=250)
	business_title = models.CharField(max_length=250)
	business_desc = models.CharField(max_length=250)
	busniess_country = models.CharField(max_length=250)
	business_category = models.CharField(max_length=250)
	total_income = models.CharField(max_length=250)
	currency_type = models.CharField(max_length=250)
	ownership_type = models.CharField(max_length=250)
	logo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
	blog = models.CharField(max_length=250)
	faxnumber = models.CharField(max_length=250)
	twitter = models.CharField(max_length=250)
	youtube = models.CharField(max_length=250)
	msn = models.CharField(max_length=250)
	business_tag = models.CharField(max_length=250)
	company_founded_months = models.CharField(max_length=250)
	company_founded_year = models.CharField(max_length=250)
	skype = models.CharField(max_length=250)
	local_time = models.CharField(max_length=250)
	company_email = models.CharField(max_length=250)
	categories = models.CharField(max_length=250)
	Pintertest = models.CharField(max_length=250)
	language=models.CharField(max_length=250)
	designation=models.CharField(max_length=250)
	annual_turn_over=models.CharField(max_length=250)
	year_of_estd=models.CharField(max_length=250)
	keywords=models.CharField(max_length=250)
	linkldn=models.CharField(max_length=250)
	sector = models.CharField(max_length=250)
	
	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

class p_country(models.Model):
	country_id= models.CharField(primary_key=True,max_length=250)
	sort_name = 	models.CharField(max_length=250)
	country = 	models.CharField(max_length=250)

	def __str__(self):
		return self.country

class p_state(models.Model):
	state_id= models.CharField(primary_key=True,max_length=250)
	state =  models.CharField(max_length=250)
	#One foreign Key relation
	country = models.ForeignKey(p_country,on_delete=models.CASCADE,)

	def __str__(self):
		return self.state

class p_city(models.Model):
	city_id= models.CharField(primary_key=True,max_length=250)
	#with country foreign Key relation
	country = models.ForeignKey(p_country,on_delete=models.CASCADE,)
	#with state relation
	state =  models.ForeignKey(p_state,on_delete=models.CASCADE,)
	#p_city location
	city=models.CharField(max_length=250)

	def __str__(self):
		return self.city

class p_location(models.Model):
	location_id= models.CharField(primary_key=True,max_length=250)
	#with country foreign Key relation
	country = models.ForeignKey(p_country,on_delete=models.CASCADE,)
	#with state relation
	state =  models.ForeignKey(p_state,on_delete=models.CASCADE,)
	#with relation with p_city foreignKey
	city =  models.ForeignKey(p_city,on_delete=models.CASCADE,)
	#p_city location
	location=models.CharField(max_length=250)

	def __str__(self):
		return self.location

class person(models.Model):
	person_id= models.CharField(primary_key=True,max_length=250)
	#with country foreign Key relation
	country = models.ForeignKey(p_country,on_delete=models.CASCADE,)
	#with state relation
	state =  models.ForeignKey(p_state,on_delete=models.CASCADE,)
	#with relation with p_city foreignKey
	city =  models.ForeignKey(p_city,on_delete=models.CASCADE,)
	#p_city location
	location =  models.ForeignKey(p_location,on_delete=models.CASCADE,)

	def __str__(self):
		return self.person_id
