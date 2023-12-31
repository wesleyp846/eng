# Generated by Django 3.2.23 on 2023-12-31 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)])),
                ('transporte', models.CharField(choices=[('M', 'Metrô'), ('O', 'Ônibus'), ('I', 'Intermunicipal'), ('T', 'Trem'), ('B', 'Bilhete Único')], max_length=1)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('origem', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
            ],
        ),
    ]