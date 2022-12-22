# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppGuestbook(models.Model):
    id = models.BigAutoField(primary_key=True)
    guest_id = models.CharField(max_length=100)
    guest_name = models.CharField(max_length=40)
    guest_type = models.CharField(max_length=15)
    guest_instance_purpose = models.CharField(max_length=15)
    guest_necessary = models.CharField(max_length=250)
    guest_arrival_date = models.DateTimeField()
    guest_fk_user_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'app_guestbook'


class AppGuestbookformservice(models.Model):
    guestbook_ptr = models.OneToOneField(AppGuestbook, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'app_guestbookformservice'


class AppLsdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    ls_id = models.CharField(max_length=100)
    ls_type = models.CharField(max_length=10)
    ls_location = models.CharField(max_length=50)
    ls_rainfall = models.CharField(max_length=20)
    ls_slopes = models.CharField(max_length=20)
    ls_soil_type = models.CharField(max_length=30)
    ls_suitability = models.CharField(max_length=100)
    ls_fk_user_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'app_lsdata'


class AppUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_phone_number = models.CharField(max_length=30)
    user_email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'app_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
