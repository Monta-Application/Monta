# -*- coding: utf-8 -*-
# Generated by Django 4.1.2 on 2022-11-02 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0006_alter_depotdetail_address_line_1_and_more"),
        ("accounts", "0005_alter_profile_title_alter_profile_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Profile",
            new_name="UserProfile",
        ),
        migrations.RenameIndex(
            model_name="userprofile",
            new_name="accounts_us_created_2ea57d_idx",
            old_name="accounts_pr_created_f4382c_idx",
        ),
    ]