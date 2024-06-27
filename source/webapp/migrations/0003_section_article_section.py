# Generated by Django 5.0.6 on 2024-06-27 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_article_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Секция',
                'verbose_name_plural': 'Секции',
                'db_table': 'sections',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='articles', to='webapp.section', verbose_name='Секция'),
        ),
    ]
