# Generated by Django 4.1 on 2022-08-18 07:00

import base.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('descript', models.TextField(max_length=500)),
                ('is_visible', models.BooleanField(default=False)),
                ('photo', models.ImageField(upload_to=base.models.AboutUs.get_file_name)),
            ],
            options={
                'ordering': ('is_visible',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('position', models.SmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('position', 'is_visible'),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ev', models.DateField(auto_created=True)),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('descript', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_visible', models.BooleanField(default=False)),
                ('photo', models.ImageField(upload_to=base.models.Event.get_file_name)),
            ],
            options={
                'ordering': ('is_visible', 'date_ev'),
            },
        ),
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=base.models.Galery.get_file_name)),
                ('descript', models.CharField(max_length=300)),
                ('is_visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone in format xxx xxx xxxx', regex='^(\\d{3}[- .]?){2}\\d{4}$')])),
                ('person', models.PositiveSmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=400)),
                ('plan_date', models.DateField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('in_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date', '-in_processed'),
            },
        ),
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('descript', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100)),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('ingrid', models.CharField(max_length=200)),
                ('descript', models.TextField(default=True, max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('special_dish', models.BooleanField(default=False)),
                ('position', models.SmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to=base.models.Menu.get_file_name)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category')),
            ],
            options={
                'ordering': ('is_visible', 'position'),
                'index_together': {('id', 'slug')},
            },
        ),
    ]