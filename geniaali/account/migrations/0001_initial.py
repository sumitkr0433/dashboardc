# Generated by Django 2.0.1 on 2020-03-05 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('months', models.CharField(max_length=250)),
                ('year', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=250)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('nickname', models.CharField(max_length=250)),
                ('website', models.CharField(max_length=250)),
                ('street_address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('pincode', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('business_title', models.CharField(max_length=250)),
                ('business_desc', models.CharField(max_length=250)),
                ('busniess_country', models.CharField(max_length=250)),
                ('business_category', models.CharField(max_length=250)),
                ('total_income', models.CharField(max_length=250)),
                ('currency_type', models.CharField(max_length=250)),
                ('ownership_type', models.CharField(max_length=250)),
                ('logo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('blog', models.CharField(max_length=250)),
                ('faxnumber', models.CharField(max_length=250)),
                ('twitter', models.CharField(max_length=250)),
                ('youtube', models.CharField(max_length=250)),
                ('msn', models.CharField(max_length=250)),
                ('business_tag', models.CharField(max_length=250)),
                ('company_founded_months', models.CharField(max_length=250)),
                ('company_founded_year', models.CharField(max_length=250)),
                ('skype', models.CharField(max_length=250)),
                ('local_time', models.CharField(max_length=250)),
                ('company_email', models.CharField(max_length=250)),
                ('categories', models.CharField(max_length=250)),
                ('Pintertest', models.CharField(max_length=250)),
                ('language', models.CharField(max_length=250)),
                ('designation', models.CharField(max_length=250)),
                ('annual_turn_over', models.CharField(max_length=250)),
                ('year_of_estd', models.CharField(max_length=250)),
                ('keywords', models.CharField(max_length=250)),
                ('linkldn', models.CharField(max_length=250)),
                ('sector', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]