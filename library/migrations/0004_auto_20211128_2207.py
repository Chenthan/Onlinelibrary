# Generated by Django 3.2.8 on 2021-11-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_reader_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='Charges',
            field=models.IntegerField(choices=[(100, '100'), (1000, '1000')], default=100),
        ),
        migrations.AlterField(
            model_name='reader',
            name='Subscription',
            field=models.CharField(choices=[('month', 'Monthly'), ('Annual', 'Annually')], default='month', max_length=128),
        ),
    ]
