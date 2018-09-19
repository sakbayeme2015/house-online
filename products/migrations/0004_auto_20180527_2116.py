# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productionimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'products/')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='productionimage',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductionImage',
        ),
    ]
