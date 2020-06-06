# Generated by Django 3.0.6 on 2020-05-31 03:32

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0003_field_fix_and_editable'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationStaffGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='auth.Group')),
                ('organization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='org_staff_groups', serialize=False, to='organizations.Organization')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organizations', models.ManyToManyField(related_name='org_perm', to='organizations.Organization', verbose_name='Organizations')),
                ('permissions', models.ManyToManyField(to='auth.Permission', verbose_name='Permissions')),
            ],
            options={
                'verbose_name': 'Organization permission',
                'verbose_name_plural': 'Organization permissions',
            },
        ),
    ]
