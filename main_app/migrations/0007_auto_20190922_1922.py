# Generated by Django 2.2.5 on 2019-09-22 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20190922_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Equipment Name')),
                ('description', models.TextField(max_length=2000, verbose_name='Equipment Description')),
                ('type', models.CharField(choices=[('W', 'Weapon'), ('A', 'Armor'), ('M', 'Magic Item')], default='W', max_length=1, verbose_name='Equipment Type')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Hero')),
            ],
        ),
        migrations.DeleteModel(
            name='Quest',
        ),
    ]
