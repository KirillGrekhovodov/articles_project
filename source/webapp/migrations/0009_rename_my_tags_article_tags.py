# Generated by Django 5.0.6 on 2024-08-22 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_remove_article_tags_article_my_tags_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='my_tags',
            new_name='tags',
        ),
    ]