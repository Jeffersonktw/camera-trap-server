# Generated by Django 3.2.2 on 2021-07-16 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taicat', '0017_remove_contact_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
        migrations.CreateModel(
            name='ProjectMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('system_admin', '系統管理員'), ('organization_admin', '計畫總管理人'), ('project_admin', '個別計畫承辦人'), ('uploader', '資料上傳者'), ('general', '一般使用者')], max_length=1000, null=True)),
                ('members', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taicat.contact')),
                ('projects', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taicat.project')),
            ],
        ),
    ]
