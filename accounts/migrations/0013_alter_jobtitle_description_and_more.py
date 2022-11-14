# Generated by Django 4.1.2 on 2022-11-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0012_user_organization"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobtitle",
            name="description",
            field=models.TextField(
                blank=True,
                default=1,
                help_text="Description of the job title",
                verbose_name="Description",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="address_line_2",
            field=models.CharField(
                blank=True,
                default=1,
                help_text="The address line 2 of the user",
                max_length=100,
                verbose_name="Address Line 2",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="bio",
            field=models.TextField(
                blank=True,
                default=1,
                help_text="The bio of the user",
                verbose_name="Bio",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="phone",
            field=models.CharField(
                blank=True,
                default=1,
                help_text="The phone number of the user",
                max_length=15,
                verbose_name="Phone Number",
            ),
            preserve_default=False,
        ),
    ]