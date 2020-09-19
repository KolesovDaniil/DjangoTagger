# Generated by Django 3.1.1 on 2020-09-16 20:29

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
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('creation_dt', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('last_update_dt', models.DateTimeField(null=True, verbose_name='Дата последнего редактирования')),
                ('tags', models.TextField(verbose_name='Тэги')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
