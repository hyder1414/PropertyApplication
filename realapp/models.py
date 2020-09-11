# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Firm(models.Model):
    firmid = models.IntegerField(db_column='FirmID', primary_key=True)  # Field name made lowercase.
    firmname = models.CharField(db_column='FirmName', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Firm'


class Manager(models.Model):
    emplid = models.IntegerField(db_column='EmplID', primary_key=True)  # Field name made lowercase.
    bonus = models.DecimalField(db_column='Bonus', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Manager'


class Salesoffice(models.Model):
    officeid = models.IntegerField(db_column='OfficeID', primary_key=True)  # Field name made lowercase.
    officestreet = models.CharField(db_column='OfficeStreet', max_length=30)  # Field name made lowercase.
    officecity = models.CharField(db_column='OfficeCity', max_length=30)  # Field name made lowercase.
    officestate = models.CharField(db_column='OfficeState', max_length=2)  # Field name made lowercase.
    officezip = models.CharField(db_column='OfficeZip', max_length=9)  # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    firmid = models.ForeignKey(Firm, models.DO_NOTHING, db_column='FirmID')  # Field name made lowercase.
    managerid = models.ForeignKey(Manager, models.DO_NOTHING, db_column='ManagerID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SalesOffice'
    def __str__(self):
        return ("%s, %s, %s" %(self.officeid, self.officestreet,self.officecity))
class Employee(models.Model):
    emplid = models.IntegerField(db_column='EmplID', primary_key=True)  # Field name made lowercase.
    empllastname = models.CharField(db_column='EmplLastName', max_length=35)  # Field name made lowercase.
    emplfirstname = models.CharField(db_column='EmplFirstName', max_length=20)  # Field name made lowercase.
    officeid = models.ForeignKey('Salesoffice', models.DO_NOTHING, db_column='OfficeID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Employee'


class Property(models.Model):
    propertyid = models.IntegerField(db_column='PropertyID', primary_key=True)  # Field name made lowercase.
    propaddress = models.CharField(db_column='PropAddress', max_length=35)  # Field name made lowercase.
    propcity = models.CharField(db_column='PropCity', max_length=30)  # Field name made lowercase.
    propstate = models.CharField(db_column='PropState', max_length=2)  # Field name made lowercase.
    propzip = models.CharField(db_column='PropZip', max_length=9, blank=True, null=True)  # Field name made lowercase.
    listingdate = models.DateField(db_column='ListingDate', blank=True, null=True)  # Field name made lowercase.
    solddate = models.DateField(db_column='SoldDate', blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    officeid = models.ForeignKey('Salesoffice', models.DO_NOTHING, db_column='OfficeID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Property'

class Propertyowner(models.Model):
    ownerid = models.IntegerField(db_column='OwnerID', primary_key=True)  # Field name made lowercase.
    ownerlastname = models.CharField(db_column='OwnerLastName', max_length=30)  # Field name made lowercase.
    ownerfirstname = models.CharField(db_column='OwnerFirstName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PropertyOwner'


class Propertyownership(models.Model):
    propownershipid = models.AutoField(db_column='PropOwnershipID', primary_key=True)  # Field name made lowercase.
    propertyid = models.ForeignKey(Property, models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    ownerid = models.ForeignKey(Propertyowner, models.DO_NOTHING, db_column='OwnerID')  # Field name made lowercase.
    percentowned = models.DecimalField(db_column='PercentOwned', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PropertyOwnership'




class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed =  False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed =  False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed =  False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed =  False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed =  False
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
