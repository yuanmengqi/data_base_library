# Generated by Django 5.0.6 on 2024-06-12 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_managerment', '0004_alter_book_author_alter_book_catagoery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(null=True, upload_to='static/images', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(max_length=64, null=True, verbose_name='出版日期'),
        ),
    ]
