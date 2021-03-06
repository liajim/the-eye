# Generated by Django 4.0.1 on 2022-01-15 18:51

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_session_options_alter_event_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='data',
            field=events.models.DataPayloadField(verbose_name='Payload of data'),
        ),
        migrations.AlterField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(validators=[events.models.no_future], verbose_name='Timestamp'),
        ),
    ]
