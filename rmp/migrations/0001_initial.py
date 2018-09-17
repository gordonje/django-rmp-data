# Generated by Django 2.1.1 on 2018-09-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccChem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accchem_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('accident_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('chemical_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('quantity_lbs', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('percent_weight', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('num_acc_flam', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('cas', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('chemical_type', models.BooleanField()),
            ],
            options={
                'db_table': 'rmp_acc_chem',
            },
        ),
        migrations.CreateModel(
            name='AccFlam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flammixchem_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('accchem_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('chemical_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
            ],
            options={
                'db_table': 'rmp_acc_flam',
            },
        ),
        migrations.CreateModel(
            name='ChemCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemical_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('chemical_name', models.CharField(max_length=92)),
                ('cas2', models.CharField(blank=True, max_length=10, null=True)),
                ('threshold', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('chemical_type', models.BooleanField(blank=True, null=True)),
                ('cbi_flag', models.BooleanField()),
                ('chemical_owner', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'rmp_chem_cd',
            },
        ),
        migrations.CreateModel(
            name='DeregCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dereg', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('dereg_tr', models.CharField(max_length=62)),
            ],
            options={
                'db_table': 'rmp_dereg_cd',
            },
        ),
        migrations.CreateModel(
            name='DochanCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dochan', models.CharField(max_length=1)),
                ('dochan_tr', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'rmp_dochan_cd',
            },
        ),
        migrations.CreateModel(
            name='DoctypCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctyp', models.CharField(max_length=1)),
                ('doctyp_tr', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'rmp_doctyp_cd',
            },
        ),
        migrations.CreateModel(
            name='EventsCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.CharField(max_length=1)),
                ('events_tr', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'rmp_events_cd',
            },
        ),
        migrations.CreateModel(
            name='ExecSumLen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rmp_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('byte_count', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('suspect_count', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('line_count', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('edited_yn', models.BooleanField()),
            ],
            options={
                'db_table': 'rmp_exec_sum_len',
            },
        ),
        migrations.CreateModel(
            name='LldescCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lldesc', models.CharField(max_length=2)),
                ('lldesc_tr', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'rmp_lldesc_cd',
            },
        ),
        migrations.CreateModel(
            name='LlmethCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_key', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('llmeth', models.CharField(max_length=2)),
                ('llmeth_tr', models.CharField(max_length=83)),
            ],
            options={
                'db_table': 'rmp_llmeth_cd',
            },
        ),
        migrations.CreateModel(
            name='PhysCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phys', models.CharField(max_length=1)),
                ('phys_tr', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'rmp_phys_cd',
            },
        ),
        migrations.CreateModel(
            name='Prevent2Chem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_key', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('prevent_2_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('procchem_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
            ],
            options={
                'db_table': 'rmp_prevent_2_chem',
            },
        ),
        migrations.CreateModel(
            name='Prevent3Chem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_key', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('prevent_3_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('procchem_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
            ],
            options={
                'db_table': 'rmp_prevent_3_chem',
            },
        ),
        migrations.CreateModel(
            name='ProcChem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procchem_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('process_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('chemical_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('quantity_lbs', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('cbi_flag', models.BooleanField()),
                ('num_alt_flam', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('num_alt_tox', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('num_prevent_2_chem', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('num_prevent_3_chem', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('num_proc_flam', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('num_worst_flam', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('num_worst_tox', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('cas', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('chemical_type', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rmp_proc_chem',
            },
        ),
        migrations.CreateModel(
            name='ProcFlam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flammixchem_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('procchem_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('chemical_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
            ],
            options={
                'db_table': 'rmp_proc_flam',
            },
        ),
        migrations.CreateModel(
            name='ProcNaics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procnaics_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('process_id', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('naics', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('num_prevent_2', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('num_prevent_3', models.DecimalField(decimal_places=65535, max_digits=65535)),
            ],
            options={
                'db_table': 'rmp_proc_naics',
            },
        ),
        migrations.CreateModel(
            name='RejectCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reject', models.CharField(max_length=1)),
                ('reject_tr', models.CharField(max_length=59)),
            ],
            options={
                'db_table': 'rmp_reject_cd',
            },
        ),
        migrations.CreateModel(
            name='ScenCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scen', models.CharField(max_length=1)),
                ('scen_tr', models.CharField(max_length=27)),
            ],
            options={
                'db_table': 'rmp_scen_cd',
            },
        ),
        migrations.CreateModel(
            name='SubmitCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit', models.CharField(max_length=3)),
                ('submit_tr', models.CharField(max_length=101)),
            ],
            options={
                'db_table': 'rmp_submit_cd',
            },
        ),
        migrations.CreateModel(
            name='TopoCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topo', models.CharField(max_length=1)),
                ('topo_tr', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'rmp_topo_cd',
            },
        ),
        migrations.CreateModel(
            name='WindCd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wind', models.CharField(max_length=1)),
                ('wind_tr', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'rmp_wind_cd',
            },
        ),
    ]
