# Generated by Django 4.0.4 on 2022-05-31 20:55

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=250)),
                ('name_ru', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=250)),
                ('name_ru', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.region')),
            ],
            bases=(models.Model, main.models.TranslateHelperMixin),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=250)),
                ('name_ru', models.CharField(max_length=250)),
                ('text_uz', models.TextField()),
                ('text_ru', models.TextField()),
                ('number', models.CharField(max_length=250)),
                ('telegram', models.CharField(max_length=250)),
                ('vaqt', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('img', models.ImageField(upload_to='images/')),
                ('maydon_soni', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.district')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.region')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.region'),
        ),
    ]
