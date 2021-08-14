# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllSsqdata(models.Model):
    red01 = models.IntegerField(blank=True, null=True)
    red02 = models.IntegerField(blank=True, null=True)
    red03 = models.IntegerField(blank=True, null=True)
    red04 = models.IntegerField(blank=True, null=True)
    red05 = models.IntegerField(blank=True, null=True)
    red06 = models.IntegerField(blank=True, null=True)
    blue01 = models.IntegerField(blank=True, null=True)
    allnum=models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'all_ssqdata'
class MidAllSsqdata(models.Model):
    all_ssq = models.ForeignKey(AllSsqdata, models.DO_NOTHING, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'mid_all_ssqdata'

class AnalyzeIndex(models.Model):
    all_ssq = models.ForeignKey(AllSsqdata, models.DO_NOTHING, blank=True, null=True)
    odd_even_ratio = models.FloatField(blank=True, null=True)
    big_small_ratio = models.FloatField(blank=True, null=True)
    prime_number_count = models.IntegerField(blank=True, null=True)
    sum_value = models.IntegerField(blank=True, null=True)
    loose_value = models.IntegerField(blank=True, null=True)
    ac_value = models.IntegerField(blank=True, null=True)
    one_section = models.IntegerField(blank=True, null=True)
    two_section = models.IntegerField(blank=True, null=True)
    three_section = models.IntegerField(blank=True, null=True)
    consective_num_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'analyze_index'


class AnalyzeIndexSection(models.Model):
    one_section = models.IntegerField(blank=True, null=True)
    two_section = models.IntegerField(blank=True, null=True)
    three_section = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'analyze_index_section'


class BlueLosingLottery(models.Model):
    termnum = models.CharField(max_length=8, blank=True, null=True)
    num_01 = models.IntegerField(blank=True, null=True)
    num_02 = models.IntegerField(blank=True, null=True)
    num_03 = models.IntegerField(blank=True, null=True)
    num_04 = models.IntegerField(blank=True, null=True)
    num_05 = models.IntegerField(blank=True, null=True)
    num_06 = models.IntegerField(blank=True, null=True)
    num_07 = models.IntegerField(blank=True, null=True)
    num_08 = models.IntegerField(blank=True, null=True)
    num_09 = models.IntegerField(blank=True, null=True)
    num_10 = models.IntegerField(blank=True, null=True)
    num_11 = models.IntegerField(blank=True, null=True)
    num_12 = models.IntegerField(blank=True, null=True)
    num_13 = models.IntegerField(blank=True, null=True)
    num_14 = models.IntegerField(blank=True, null=True)
    num_15 = models.IntegerField(blank=True, null=True)
    num_16 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'blue_losing_lottery'


class LongDhr(models.Model):
    num = models.IntegerField(blank=True, null=True)
    appear_1 = models.IntegerField(blank=True, null=True)
    appear_2 = models.IntegerField(blank=True, null=True)
    appear_3 = models.IntegerField(blank=True, null=True)
    appear_4 = models.IntegerField(blank=True, null=True)
    appear_5 = models.IntegerField(blank=True, null=True)
    dhr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'long_dhr'


class PairNum(models.Model):
    pair_num = models.CharField(max_length=10, blank=True, null=True)
    pair_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pair_num'


class RedLosingLottery(models.Model):
    termnum = models.CharField(max_length=8, blank=True, null=True)
    num_01 = models.IntegerField(blank=True, null=True)
    num_02 = models.IntegerField(blank=True, null=True)
    num_03 = models.IntegerField(blank=True, null=True)
    num_04 = models.IntegerField(blank=True, null=True)
    num_05 = models.IntegerField(blank=True, null=True)
    num_06 = models.IntegerField(blank=True, null=True)
    num_07 = models.IntegerField(blank=True, null=True)
    num_08 = models.IntegerField(blank=True, null=True)
    num_09 = models.IntegerField(blank=True, null=True)
    num_10 = models.IntegerField(blank=True, null=True)
    num_11 = models.IntegerField(blank=True, null=True)
    num_12 = models.IntegerField(blank=True, null=True)
    num_13 = models.IntegerField(blank=True, null=True)
    num_14 = models.IntegerField(blank=True, null=True)
    num_15 = models.IntegerField(blank=True, null=True)
    num_16 = models.IntegerField(blank=True, null=True)
    num_17 = models.IntegerField(blank=True, null=True)
    num_18 = models.IntegerField(blank=True, null=True)
    num_19 = models.IntegerField(blank=True, null=True)
    num_20 = models.IntegerField(blank=True, null=True)
    num_21 = models.IntegerField(blank=True, null=True)
    num_22 = models.IntegerField(blank=True, null=True)
    num_23 = models.IntegerField(blank=True, null=True)
    num_24 = models.IntegerField(blank=True, null=True)
    num_25 = models.IntegerField(blank=True, null=True)
    num_26 = models.IntegerField(blank=True, null=True)
    num_27 = models.IntegerField(blank=True, null=True)
    num_28 = models.IntegerField(blank=True, null=True)
    num_29 = models.IntegerField(blank=True, null=True)
    num_30 = models.IntegerField(blank=True, null=True)
    num_31 = models.IntegerField(blank=True, null=True)
    num_32 = models.IntegerField(blank=True, null=True)
    num_33 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'red_losing_lottery'


class SelectedSsqdata(models.Model):
    id = models.AutoField(primary_key=True)
    red01 = models.IntegerField(blank=True, null=True)
    red02 = models.IntegerField(blank=True, null=True)
    red03 = models.IntegerField(blank=True, null=True)
    red04 = models.IntegerField(blank=True, null=True)
    red05 = models.IntegerField(blank=True, null=True)
    red06 = models.IntegerField(blank=True, null=True)
    blue01 = models.IntegerField(blank=True, null=True)
    termnum = models.CharField(db_column='termNum', max_length=10, blank=True, null=True)
    def __init__(self, red01, red02,red03,red04,red05,red06,blue01,termnum):
        super().__init__()
        self.red01=red01
        self.red02=red02
        self.red03=red03
        self.red04=red04
        self.red05=red05
        self.red06=red06
        self.blue01=blue01
        self.termnum=termnum

    def __str__(self):
        return u"%s, %s, %s,%s, %s, %s,%s, %s" % (self.red01, self.red02, self.red03,self.red04,self.red05,self.red06,self.blue01,self.termnum)
    class Meta:
        managed = True
        db_table = 'selected_ssqdata'


class Ssqdata(models.Model):
    opendate = models.DateField(db_column='openDate', blank=True, null=True)  # Field name made lowercase.
    termnum = models.CharField(db_column='termNum', max_length=10, blank=True, null=True)  # Field name made lowercase.
    red01 = models.IntegerField(blank=True, null=True)
    red02 = models.IntegerField(blank=True, null=True)
    red03 = models.IntegerField(blank=True, null=True)
    red04 = models.IntegerField(blank=True, null=True)
    red05 = models.IntegerField(blank=True, null=True)
    red06 = models.IntegerField(blank=True, null=True)
    blue01 = models.IntegerField(blank=True, null=True)
    hashcode = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ssqdata'


class ThripleNum(models.Model):
    thriple_num = models.CharField(max_length=100, blank=True, null=True)
    thriple_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'thriple_num'
