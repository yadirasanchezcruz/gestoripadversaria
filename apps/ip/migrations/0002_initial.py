# Generated by Django 4.2 on 2023-05-05 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpais',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldireccionip',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldireccionip',
            name='pais',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ip.pais'),
        ),
        migrations.AddField(
            model_name='direccionip',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ip.pais'),
        ),
    ]
