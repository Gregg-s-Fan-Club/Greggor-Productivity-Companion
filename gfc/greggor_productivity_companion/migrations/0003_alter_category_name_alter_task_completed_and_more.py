# Generated by Django 4.1.3 on 2024-03-09 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greggor_productivity_companion', '0002_category_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=520, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=520, unique=True),
        ),
        migrations.CreateModel(
            name='WorkPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('points', models.IntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greggor_productivity_companion.task')),
            ],
        ),
    ]
