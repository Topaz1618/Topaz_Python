# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-08 08:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('interval', models.IntegerField(default=300, verbose_name='告警间隔(s)')),
                ('recover_notice', models.BooleanField(default=True, verbose_name='故障恢复后发送通知消息')),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActionOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('step_from', models.IntegerField(verbose_name='Step from')),
                ('step_to', models.IntegerField(verbose_name='Step to')),
                ('action_type', models.CharField(choices=[('email', 'Email'), ('sms', 'SMS'), ('script', 'RunScript')], default='email', max_length=64, verbose_name='动作类型')),
                ('msg_format', models.TextField(default='Host({hostname},{ip}) service({service_name}) has issue,msg:{msg}', verbose_name='消息格式')),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_calc_func', models.CharField(choices=[('avg', 'Average'), ('max', 'Max'), ('hit', 'Hit'), ('last', 'Last')], max_length=64, verbose_name='数据处理方式')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('operator_type', models.CharField(choices=[('eq', '='), ('lt', '<'), ('gt', '>')], max_length=32, verbose_name='运算符')),
                ('threshold', models.IntegerField(verbose_name='阈值')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('host_alive', models.IntegerField(default=30, verbose_name='主机存活状态监测')),
                ('enabled', models.BooleanField(default=True)),
                ('status', models.IntegerField(choices=[(1, 'Online'), (2, 'Down'), (3, 'Unreachable'), (4, 'Offline'), (5, 'Problem')], default=1)),
                ('host_group', models.ManyToManyField(blank=True, to='monitor.Host')),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('interval', models.IntegerField(default=60, verbose_name='监控间隔')),
                ('monitored_by', models.CharField(choices=[('agent', 'Agent'), ('snmp', 'SNMP'), ('wget', 'WGET')], max_length=64)),
                ('data_type', models.CharField(choices=[('int', 'int'), ('float', 'float'), ('str', 'str')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('item', models.ManyToManyField(blank=True, to='monitor.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('severity', models.IntegerField(choices=[(0, 'Not classified'), (1, 'Information'), (2, 'Warning'), (3, 'Average'), (4, 'High'), (5, 'Disaster')], default=2)),
                ('enable', models.BooleanField(default=True, verbose_name='已启用')),
            ],
        ),
        migrations.CreateModel(
            name='TriggerExpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logic_type', models.CharField(blank=True, choices=[('or', 'OR'), ('and', 'AND')], max_length=32, null=True, verbose_name='与一个条件的逻辑关系')),
                ('function', models.ManyToManyField(to='monitor.Function')),
                ('keys', models.ManyToManyField(to='monitor.Key')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='trigger',
            name='expression',
            field=models.ManyToManyField(max_length=64, to='monitor.TriggerExpression'),
        ),
        migrations.AddField(
            model_name='item',
            name='keys',
            field=models.ManyToManyField(to='monitor.Key'),
        ),
        migrations.AddField(
            model_name='host',
            name='template',
            field=models.ManyToManyField(blank=True, to='monitor.Template'),
        ),
        migrations.AddField(
            model_name='actionoperation',
            name='send_to_user',
            field=models.ManyToManyField(blank=True, to='monitor.UserProfile', verbose_name='通知对象'),
        ),
        migrations.AddField(
            model_name='action',
            name='operations',
            field=models.ManyToManyField(to='monitor.ActionOperation', verbose_name='报警动作'),
        ),
        migrations.AddField(
            model_name='action',
            name='triggers',
            field=models.ManyToManyField(blank=True, help_text='想让哪些trigger触发当前报警动作', to='monitor.Trigger'),
        ),
    ]