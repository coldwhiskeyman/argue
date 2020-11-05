# Generated by Django 3.1.3 on 2020-11-05 11:35

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
            name='Argue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание')),
                ('opened', models.DateTimeField(default=None, null=True, verbose_name='Спор открыт')),
                ('closed', models.DateTimeField(default=None, null=True, verbose_name='Спор разрешен')),
                ('active', models.BooleanField(default=True, verbose_name='Активно')),
                ('answerer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='argues', to=settings.AUTH_USER_MODEL, verbose_name='Вызываемый')),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_argues', to=settings.AUTH_USER_MODEL, verbose_name='Вызывающий')),
            ],
        ),
    ]