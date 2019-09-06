# Generated by Django 2.2.3 on 2019-09-04 17:04

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("response", "0003_auto_20190904_1349")]

    operations = [
        migrations.AlterField(
            model_name="timelineevent",
            name="metadata",
            field=jsonfield.fields.JSONField(
                help_text="Additional fields that can be added by other event types",
                null=True,
            ),
        )
    ]
