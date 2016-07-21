# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 11:08
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
            name='InterestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True)),
                ('approval_date', models.DateField()),
                ('interest', models.FloatField()),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('start', models.DateField(blank=True, null=True)),
                ('expected_end', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('guaranteed_by', models.ManyToManyField(blank=True, related_name='loans_guaranteed', to=settings.AUTH_USER_MODEL)),
                ('interest_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='loans.InterestType')),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True)),
                ('application_date', models.DateField()),
                ('proposed_amount', models.IntegerField()),
                ('proposed_start', models.DateField()),
                ('proposed_end', models.DateField()),
                ('approved', models.BooleanField()),
                ('approved_at', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('approved_by', models.ManyToManyField(blank=True, related_name='loans_approved', to=settings.AUTH_USER_MODEL)),
                ('guaranteed_by', models.ManyToManyField(blank=True, related_name='loan_applications_guaranteed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplicationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Loan Application Statuses',
            },
        ),
        migrations.CreateModel(
            name='LoanCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Loan Categories',
            },
        ),
        migrations.CreateModel(
            name='LoanPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='loans.Loan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_payments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Loan Statuses',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('days', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.LoanApplicationStatus'),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.LoanCategory'),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_applications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_application',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='loans.LoanApplication'),
        ),
        migrations.AddField(
            model_name='loan',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.LoanStatus'),
        ),
        migrations.AddField(
            model_name='loan',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.LoanCategory'),
        ),
        migrations.AddField(
            model_name='loan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interesttype',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.Period'),
        ),
    ]