# Generated by Django 2.0.1 on 2020-03-05 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('location_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='p_city',
            fields=[
                ('city_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='p_country',
            fields=[
                ('country_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('sort_name', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='p_state',
            fields=[
                ('state_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=250)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.p_country')),
            ],
        ),
        migrations.AddField(
            model_name='p_city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.p_country'),
        ),
        migrations.AddField(
            model_name='p_city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.p_state'),
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.p_city'),
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.p_country'),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.p_state'),
        ),
    ]
