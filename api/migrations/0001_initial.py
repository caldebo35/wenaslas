# Generated by Django 4.2.5 on 2023-10-02 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('idBodega', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de la bodega')),
                ('capacidad', models.IntegerField(verbose_name='Capacidad de la bodega')),
                ('area', models.FloatField(verbose_name='Area (m²)')),
                ('volumen', models.FloatField(verbose_name='Volumen (m³)')),
                ('altura', models.FloatField(verbose_name='Altura (m)')),
                ('largo', models.FloatField(verbose_name='Largo (m)')),
                ('ancho', models.FloatField(verbose_name='Ancho (m)')),
            ],
            options={
                'verbose_name': 'Bodega',
                'verbose_name_plural': 'Bodegas',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idVehiculo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del vehiculo')),
                ('capacidad', models.IntegerField(verbose_name='Capacidad del vehiculo')),
                ('volumen_carga', models.FloatField(verbose_name='Volumen de carga (m³)')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
            },
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('idObjeto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del objeto')),
                ('largo', models.FloatField(verbose_name='Largo (m)')),
                ('ancho', models.FloatField(verbose_name='Ancho (m)')),
                ('alto', models.FloatField(verbose_name='Alto (m)')),
                ('volumen', models.FloatField(blank=True, null=True, verbose_name='Volumen (m³)')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria')),
            ],
            options={
                'verbose_name': 'Objeto',
                'verbose_name_plural': 'Objetos',
            },
        ),
        migrations.CreateModel(
            name='Calculo',
            fields=[
                ('idCalculo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('volumen_Total', models.FloatField(verbose_name='Volumen Total (m³)')),
                ('idBodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bodega')),
                ('idVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehiculo')),
                ('objetos', models.ManyToManyField(to='api.objeto')),
            ],
            options={
                'verbose_name': 'Calculo',
                'verbose_name_plural': 'Calculos',
            },
        ),
    ]
