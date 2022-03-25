# Generated by Django 3.2.12 on 2022-03-25 16:28

from django.db import migrations
from django.template.defaultfilters import slugify


def assign_slug(apps, schema_editor):
    Posts = apps.get_model('Posts', 'Posts')
    posts = Posts.objects.all()
    for post in posts:
        slug = slugify(post.title)
        post.slug = slug if len(slug) <= 255 else slug[:255]
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_add_slug'),
    ]

    operations = [
        migrations.RunPython(assign_slug)
    ]