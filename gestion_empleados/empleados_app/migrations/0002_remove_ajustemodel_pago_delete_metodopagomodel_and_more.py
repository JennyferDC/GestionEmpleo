# Generated by Django 5.2.3 on 2025-07-04 13:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ajustemodel',
            name='pago',
        ),
        migrations.DeleteModel(
            name='MetodoPagoModel',
        ),
        migrations.RemoveField(
            model_name='pagomodel',
            name='nomina',
        ),
        migrations.RemoveField(
            model_name='reportemodel',
            name='empleado',
        ),
        migrations.DeleteModel(
            name='TipoEmpleadoModel',
        ),
        migrations.AlterModelOptions(
            name='notificacionmodel',
            options={'ordering': ['-fecha_envio']},
        ),
        migrations.AlterModelOptions(
            name='pagomodel',
            options={'ordering': ['-fecha_pago']},
        ),
        migrations.RemoveField(
            model_name='empleadomodel',
            name='salario_fijo',
        ),
        migrations.RemoveField(
            model_name='empleadomodel',
            name='salario_hora',
        ),
        migrations.RemoveField(
            model_name='empleadomodel',
            name='tarifa_proyecto',
        ),
        migrations.RemoveField(
            model_name='pagomodel',
            name='monto_base',
        ),
        migrations.RemoveField(
            model_name='pagomodel',
            name='total_pagado',
        ),
        migrations.AddField(
            model_name='empleadomodel',
            name='pago_contrato',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='empleadomodel',
            name='salario_mensual',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='empleadomodel',
            name='tarifa_hora',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pagomodel',
            name='fecha_pago',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagomodel',
            name='monto_pagado',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleadomodel',
            name='horas_trabajadas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empleadomodel',
            name='tipo_empleado',
            field=models.CharField(choices=[('tiempo_completo', 'tiempo_completo'), ('medio_tiempo', 'medio_tiempo'), ('contratista', 'contratista')], max_length=20),
        ),
        migrations.AlterField(
            model_name='notificacionmodel',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to='empleados_app.empleadomodel'),
        ),
        migrations.AlterField(
            model_name='pagomodel',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='empleados_app.empleadomodel'),
        ),
        migrations.DeleteModel(
            name='AjusteModel',
        ),
        migrations.DeleteModel(
            name='NominaModel',
        ),
        migrations.DeleteModel(
            name='ReporteModel',
        ),
    ]
