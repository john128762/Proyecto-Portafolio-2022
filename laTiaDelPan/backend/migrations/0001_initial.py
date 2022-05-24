# Generated by Django 4.0.4 on 2022-05-24 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('BOL_NUMERO', models.AutoField(primary_key=True, serialize=False)),
                ('BOL_FECHA_VENTA', models.DateTimeField()),
                ('BOL_SUBTOTAL', models.DecimalField(decimal_places=3, max_digits=10)),
                ('BOL_IVA', models.DecimalField(decimal_places=3, max_digits=10)),
                ('BOL_VIGENCIA', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('CAT_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CAT_NOMBRE', models.CharField(max_length=20)),
                ('CAT_DESCRIPCION', models.CharField(max_length=100)),
                ('CAT_ESTADO', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Fact_Proveedor',
            fields=[
                ('FAC_NUMERO', models.AutoField(primary_key=True, serialize=False)),
                ('FAC_FECHA_VENTA', models.DateTimeField()),
                ('FAC_TOTAL', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('PROV_RUT', models.IntegerField(primary_key=True, serialize=False)),
                ('PROV_DV', models.CharField(max_length=1)),
                ('PROV_NOMBRE', models.CharField(max_length=40)),
                ('PROV_CONTACTO', models.CharField(max_length=40)),
                ('PROV_ESTADO', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('USU_RUT', models.IntegerField(primary_key=True, serialize=False)),
                ('USU_DV', models.CharField(max_length=1)),
                ('USU_USERNAME', models.CharField(max_length=20)),
                ('USU_NOMBRES', models.CharField(max_length=40)),
                ('USU_APELLIDOS', models.CharField(max_length=40)),
                ('USU_PASSWORD', models.CharField(max_length=40)),
                ('USU_VIGENCIA', models.BooleanField()),
                ('USU_ADMINISTRADOR', models.BooleanField()),
                ('USU_FECHA_INGRESO', models.DateTimeField()),
                ('USU_FECHA_MODIFICACION', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('PROD_CODIGO', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('PROD_NOMBRE', models.CharField(max_length=40)),
                ('PROD_VALOR', models.DecimalField(decimal_places=3, max_digits=10)),
                ('PROD_STOCK', models.IntegerField()),
                ('PROD_ESTADO', models.BooleanField()),
                ('CAT_ID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.categoria')),
                ('PROV_RUT', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DET_CANTIDAD', models.IntegerField()),
                ('DET_VALOR', models.DecimalField(decimal_places=3, max_digits=10)),
                ('BOL_NUMERO', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.boleta')),
                ('PROD_CODIGO', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Det_Fact_Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DFT_CANTIDAD', models.IntegerField()),
                ('DFT_VALOR', models.DecimalField(decimal_places=3, max_digits=10)),
                ('FAC_NUMERO', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.fact_proveedor')),
                ('PROD_CODIGO', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.producto')),
            ],
        ),
        migrations.AddField(
            model_name='boleta',
            name='USU_RUT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.usuario'),
        ),
    ]
