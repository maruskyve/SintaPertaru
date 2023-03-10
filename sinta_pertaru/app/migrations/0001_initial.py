# Generated by Django 4.1 on 2022-12-14 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=70)),
                ('employee_class', models.CharField(max_length=20)),
                ('employee_gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=10)),
                ('employee_address', models.CharField(max_length=200)),
                ('employee_phone_number', models.CharField(max_length=15)),
                ('employee_date_of_birth', models.DateField()),
                ('employee_birth_district', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('guest_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('guest_name', models.CharField(max_length=40)),
                ('guest_type', models.CharField(max_length=15)),
                ('guest_instance_purpose', models.CharField(choices=[('PT', 'Pertanahan'), ('TR', 'Tata Ruang')], max_length=15)),
                ('guest_necessary', models.CharField(max_length=250)),
                ('guest_arrival_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GuestBookFormService',
            fields=[
                ('guestbook_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.guestbook')),
            ],
            bases=('app.guestbook',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=15)),
                ('user_password', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=30)),
                ('user_phone_number', models.CharField(max_length=15)),
                ('user_joined_date', models.DateTimeField()),
                ('user_fk_employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='LandData',
            fields=[
                ('land_data_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('land_data_object_id', models.SmallIntegerField()),
                ('land_data_rainfall', models.CharField(max_length=15)),
                ('land_data_slopes', models.CharField(max_length=15)),
                ('land_data_soil_type', models.CharField(max_length=15)),
                ('land_data_suitability', models.CharField(max_length=50)),
                ('land_data_accuracy', models.FloatField()),
                ('land_data_fk_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.AddField(
            model_name='guestbook',
            name='guest_fk_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
    ]
