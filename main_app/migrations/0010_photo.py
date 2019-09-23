# Generated by Django 2.2.5 on 2019-09-23 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_hero_quests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Hero')),
            ],
        ),
    ]
