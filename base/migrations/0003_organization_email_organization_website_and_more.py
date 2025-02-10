# Generated by Django 5.1.6 on 2025-02-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_paymentmethod_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='method',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('wallet', 'Wallet'), ('mobile_banking', 'Mobile Banking')], max_length=100, null=True, unique=True),
        ),
    ]
