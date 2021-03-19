# Generated by Django 3.1.4 on 2021-01-23 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creat',
            fields=[
                ('Create_Id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Create_Name', models.CharField(max_length=100)),
                ('C_description', models.CharField(max_length=500)),
                ('Create_By', models.CharField(max_length=100)),
                ('Create_By_mail', models.CharField(default='', max_length=100)),
                ('CreationDate', models.DateTimeField(blank=True, null=True)),
                ('C_FinishedDate', models.DateTimeField(blank=True, null=True)),
                ('C_PaymentProvided', models.CharField(max_length=50)),
                ('Create_city', models.CharField(default='', max_length=500)),
            ],
            options={
                'db_table': 'creat',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_Id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('emp_profilePic', models.FileField(default='', upload_to='emp/')),
                ('emp_Fname', models.CharField(max_length=30)),
                ('emp_Lname', models.CharField(max_length=30)),
                ('emp_Email', models.CharField(max_length=100)),
                ('emp_Password', models.CharField(max_length=100)),
                ('emp_Phone', models.IntegerField(blank=True, null=True)),
                ('emp_AadharCard', models.FileField(upload_to='emp/')),
                ('emp_JoinAs', models.CharField(max_length=20)),
                ('emp_Address', models.CharField(max_length=100)),
                ('emp_City', models.CharField(max_length=100)),
                ('emp_State', models.CharField(max_length=50)),
                ('emp_ZipCode', models.IntegerField(blank=True, null=True)),
                ('emp_Company', models.CharField(default='Not Working', max_length=50)),
                ('emp_RegisterDate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='FlexiAdmin',
            fields=[
                ('admin_Id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('admin_Name', models.CharField(max_length=40)),
                ('admin_Email', models.CharField(max_length=80, unique=True)),
                ('admin_Phone', models.IntegerField(blank=True, null=True)),
                ('admin_Password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'flexiadmin',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('P_sno', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('P_user_Id', models.IntegerField(null=True, unique=True)),
                ('P_user_Email', models.CharField(max_length=100)),
                ('P_PaymentStatus', models.CharField(max_length=5)),
                ('P_Applied', models.CharField(default='', max_length=10)),
                ('P_Project_Id', models.IntegerField(null=True, unique=True)),
                ('P_ProjectName', models.CharField(default='', max_length=30)),
                ('P_ProjectCreateBy', models.CharField(max_length=30)),
                ('P_StartingDate', models.DateTimeField(blank=True, null=True)),
                ('P_EndingDate', models.DateTimeField(blank=True, null=True)),
                ('P_description', models.CharField(default='', max_length=10)),
                ('P_paymentProvide', models.CharField(default='', max_length=10)),
                ('P_Create_city', models.CharField(default='', max_length=10)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('user_Id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('user_profilePic', models.FileField(default='', upload_to='')),
                ('user_Fname', models.CharField(max_length=30)),
                ('user_Lname', models.CharField(max_length=30)),
                ('user_Email', models.CharField(max_length=100)),
                ('user_Password', models.CharField(max_length=100)),
                ('user_Phone', models.IntegerField(blank=True, null=True)),
                ('user_AadharCard', models.FileField(upload_to='')),
                ('user_JoinAs', models.CharField(max_length=20)),
                ('user_Address', models.CharField(max_length=500)),
                ('user_City', models.CharField(max_length=100)),
                ('user_State', models.CharField(max_length=50)),
                ('user_ZipCode', models.IntegerField(blank=True, null=True)),
                ('user_Company', models.CharField(max_length=50)),
                ('user_RegisterDate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'register',
            },
        ),
        migrations.CreateModel(
            name='Applied',
            fields=[
                ('Appliedid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('ProjectName', models.CharField(max_length=30)),
                ('AppliedBy', models.CharField(max_length=50)),
                ('A_user_phone', models.IntegerField(blank=True, null=True)),
                ('A_Email', models.CharField(max_length=50)),
                ('A_Create_By_mail', models.CharField(default='', max_length=100)),
                ('AppliedDate', models.DateTimeField(blank=True, null=True)),
                ('A_Applied', models.CharField(default='No', max_length=50)),
                ('user_location', models.CharField(default='', max_length=500)),
                ('ProjectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlexiWorkForce.creat')),
            ],
            options={
                'db_table': 'Applied',
            },
        ),
    ]
