# Generated by Django 5.0.4 on 2024-05-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalApp', '0006_annonce_date_de_don_max'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='numerotelephone',
            field=models.IntegerField(null=True),
        ),
    ]
