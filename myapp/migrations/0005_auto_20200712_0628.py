# Generated by Django 3.0.8 on 2020-07-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200712_0518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
