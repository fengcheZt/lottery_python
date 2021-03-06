# Generated by Django 2.2.3 on 2020-06-25 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllSsqdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red01', models.IntegerField(blank=True, null=True)),
                ('red02', models.IntegerField(blank=True, null=True)),
                ('red03', models.IntegerField(blank=True, null=True)),
                ('red04', models.IntegerField(blank=True, null=True)),
                ('red05', models.IntegerField(blank=True, null=True)),
                ('red06', models.IntegerField(blank=True, null=True)),
                ('blue01', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'all_ssqdata',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AnalyzeIndexSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_section', models.IntegerField(blank=True, null=True)),
                ('two_section', models.IntegerField(blank=True, null=True)),
                ('three_section', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'analyze_index_section',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BlueLosingLottery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termnum', models.CharField(blank=True, max_length=8, null=True)),
                ('num_01', models.IntegerField(blank=True, null=True)),
                ('num_02', models.IntegerField(blank=True, null=True)),
                ('num_03', models.IntegerField(blank=True, null=True)),
                ('num_04', models.IntegerField(blank=True, null=True)),
                ('num_05', models.IntegerField(blank=True, null=True)),
                ('num_06', models.IntegerField(blank=True, null=True)),
                ('num_07', models.IntegerField(blank=True, null=True)),
                ('num_08', models.IntegerField(blank=True, null=True)),
                ('num_09', models.IntegerField(blank=True, null=True)),
                ('num_10', models.IntegerField(blank=True, null=True)),
                ('num_11', models.IntegerField(blank=True, null=True)),
                ('num_12', models.IntegerField(blank=True, null=True)),
                ('num_13', models.IntegerField(blank=True, null=True)),
                ('num_14', models.IntegerField(blank=True, null=True)),
                ('num_15', models.IntegerField(blank=True, null=True)),
                ('num_16', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'blue_losing_lottery',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LongDhr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, null=True)),
                ('appear_1', models.IntegerField(blank=True, null=True)),
                ('appear_2', models.IntegerField(blank=True, null=True)),
                ('appear_3', models.IntegerField(blank=True, null=True)),
                ('appear_4', models.IntegerField(blank=True, null=True)),
                ('appear_5', models.IntegerField(blank=True, null=True)),
                ('dhr', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'long_dhr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PairNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair_num', models.CharField(blank=True, max_length=10, null=True)),
                ('pair_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pair_num',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RedLosingLottery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termnum', models.CharField(blank=True, max_length=8, null=True)),
                ('num_01', models.IntegerField(blank=True, null=True)),
                ('num_02', models.IntegerField(blank=True, null=True)),
                ('num_03', models.IntegerField(blank=True, null=True)),
                ('num_04', models.IntegerField(blank=True, null=True)),
                ('num_05', models.IntegerField(blank=True, null=True)),
                ('num_06', models.IntegerField(blank=True, null=True)),
                ('num_07', models.IntegerField(blank=True, null=True)),
                ('num_08', models.IntegerField(blank=True, null=True)),
                ('num_09', models.IntegerField(blank=True, null=True)),
                ('num_10', models.IntegerField(blank=True, null=True)),
                ('num_11', models.IntegerField(blank=True, null=True)),
                ('num_12', models.IntegerField(blank=True, null=True)),
                ('num_13', models.IntegerField(blank=True, null=True)),
                ('num_14', models.IntegerField(blank=True, null=True)),
                ('num_15', models.IntegerField(blank=True, null=True)),
                ('num_16', models.IntegerField(blank=True, null=True)),
                ('num_17', models.IntegerField(blank=True, null=True)),
                ('num_18', models.IntegerField(blank=True, null=True)),
                ('num_19', models.IntegerField(blank=True, null=True)),
                ('num_20', models.IntegerField(blank=True, null=True)),
                ('num_21', models.IntegerField(blank=True, null=True)),
                ('num_22', models.IntegerField(blank=True, null=True)),
                ('num_23', models.IntegerField(blank=True, null=True)),
                ('num_24', models.IntegerField(blank=True, null=True)),
                ('num_25', models.IntegerField(blank=True, null=True)),
                ('num_26', models.IntegerField(blank=True, null=True)),
                ('num_27', models.IntegerField(blank=True, null=True)),
                ('num_28', models.IntegerField(blank=True, null=True)),
                ('num_29', models.IntegerField(blank=True, null=True)),
                ('num_30', models.IntegerField(blank=True, null=True)),
                ('num_31', models.IntegerField(blank=True, null=True)),
                ('num_32', models.IntegerField(blank=True, null=True)),
                ('num_33', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'red_losing_lottery',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SelectedSsqdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red01', models.IntegerField(blank=True, null=True)),
                ('red02', models.IntegerField(blank=True, null=True)),
                ('red03', models.IntegerField(blank=True, null=True)),
                ('red04', models.IntegerField(blank=True, null=True)),
                ('red05', models.IntegerField(blank=True, null=True)),
                ('red06', models.IntegerField(blank=True, null=True)),
                ('blue01', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'selected_ssqdata',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ssqdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opendate', models.DateField(blank=True, db_column='openDate', null=True)),
                ('termnum', models.CharField(blank=True, db_column='termNum', max_length=10, null=True)),
                ('red01', models.IntegerField(blank=True, null=True)),
                ('red02', models.IntegerField(blank=True, null=True)),
                ('red03', models.IntegerField(blank=True, null=True)),
                ('red04', models.IntegerField(blank=True, null=True)),
                ('red05', models.IntegerField(blank=True, null=True)),
                ('red06', models.IntegerField(blank=True, null=True)),
                ('blue01', models.IntegerField(blank=True, null=True)),
                ('hashcode', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'ssqdata',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ThripleNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thriple_num', models.CharField(blank=True, max_length=100, null=True)),
                ('thriple_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'thriple_num',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AnalyzeIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odd_even_ratio', models.FloatField(blank=True, null=True)),
                ('big_small_ratio', models.FloatField(blank=True, null=True)),
                ('prime_number_count', models.IntegerField(blank=True, null=True)),
                ('sum_value', models.IntegerField(blank=True, null=True)),
                ('loose_value', models.IntegerField(blank=True, null=True)),
                ('ac_value', models.IntegerField(blank=True, null=True)),
                ('one_section', models.IntegerField(blank=True, null=True)),
                ('two_section', models.IntegerField(blank=True, null=True)),
                ('three_section', models.IntegerField(blank=True, null=True)),
                ('consective_num_index', models.IntegerField(blank=True, null=True)),
                ('all_ssq', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='get_the_num.AllSsqdata')),
            ],
            options={
                'db_table': 'analyze_index',
                'managed': True,
            },
        ),
    ]
