# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_auto_20180713_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(default=25.0, null=True, max_digits=50, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(default=0.085, null=True, max_digits=10, decimal_places=5, blank=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(default=25.0, null=True, max_digits=50, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=25.0, null=True, max_digits=50, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='line_item_total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
