from django.db import models


# ADD-14122022
class Employee(models.Model):
    employee_id = models.BigIntegerField(primary_key=True)
    employee_name = models.CharField(max_length=70)
    employee_class = models.CharField(max_length=20)
    employee_gender = models.CharField(max_length=10, choices=[('M', 'male'), ('F', 'female')])
    employee_address = models.CharField(max_length=200)
    employee_phone_number = models.CharField(max_length=15)
    employee_date_of_birth = models.DateField()
    employee_birth_district = models.CharField(max_length=30)


class User(models.Model):
    user_id = models.SmallIntegerField(primary_key=True)
    user_name = models.CharField(max_length=15)
    user_password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=30)
    user_phone_number = models.CharField(max_length=15)
    user_joined_date = models.DateTimeField()
    user_fk_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class LandData(models.Model):
    land_data_id = models.SmallIntegerField(primary_key=True)
    land_data_object_id = models.SmallIntegerField()
    land_data_rainfall = models.CharField(max_length=15)
    land_data_slopes = models.CharField(max_length=15)
    land_data_soil_type = models.CharField(max_length=30)
    land_data_suitability = models.CharField(max_length=90)
    land_data_type = models.CharField(max_length=5, choices=[('TR', 'Train'), ('TE', 'Test')])
    land_data_accuracy = models.FloatField()
    land_data_fk_user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class GuestBook(models.Model):
    guest_id = models.SmallIntegerField(primary_key=True)
    guest_name = models.CharField(max_length=40)
    guest_type = models.CharField(max_length=15)
    guest_instance_purpose = models.CharField(max_length=15, choices=[('PT', 'Pertanahan'), ('TR', 'Tata Ruang')])
    guest_necessary = models.CharField(max_length=250)
    guest_arrival_date = models.DateTimeField()
    guest_fk_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
