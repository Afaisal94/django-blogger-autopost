# Generated by Django 4.0.2 on 2022-02-27 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(max_length=255)),
                ('email_post', models.EmailField(max_length=255, unique=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.mail')),
                ('batch', models.IntegerField()),
                ('url_blogger', models.CharField(max_length=255)),
            ],
        ),
    ]
