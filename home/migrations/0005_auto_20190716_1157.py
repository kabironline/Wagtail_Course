# Generated by Django 2.2.3 on 2019-07-16 06:27

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190716_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_subtitle',
            field=wagtail.core.fields.RichTextField(default='Test text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
