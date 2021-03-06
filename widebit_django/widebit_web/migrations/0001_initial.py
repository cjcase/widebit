# Generated by Django 2.0.1 on 2018-01-30 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('commit', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Goal Weight')),
                ('bf', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Goal Body Fat')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('text', models.TextField(max_length=1500, verbose_name='Meal Description')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nutrient Name')),
                ('desc', models.TextField(max_length=200, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient_Goals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('nutrient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widebit_web.Nutrient')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient_Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('nutrient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widebit_web.Nutrient')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Weight')),
                ('bf', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Body Fat')),
            ],
        ),
        migrations.AddField(
            model_name='nutrient_reg',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widebit_web.Profile'),
        ),
        migrations.AddField(
            model_name='meal',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='widebit_web.Profile'),
        ),
        migrations.AddField(
            model_name='goal',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='goal', to='widebit_web.Profile'),
        ),
    ]
