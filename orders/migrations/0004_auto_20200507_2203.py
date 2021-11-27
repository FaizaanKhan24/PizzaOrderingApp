# Generated by Django 2.1.5 on 2020-05-07 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderslist_extras'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderslist',
            name='isOrderPlaced',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderslist',
            name='extras',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='subs',
            name='small_sub_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]