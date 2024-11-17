from django.db import models

# Model for search1 in the default database
class Search1(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated primary key
    item = models.CharField(max_length=255)  # Character field for 'item'

    class Meta:
        managed = False  # Django won't create or modify this table
        db_table = 'search1'  # Ensure it matches the actual table name


# Model for search2 in db2
class Search2(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated primary key
    item = models.CharField(max_length=255)  # Character field for 'item'

    class Meta:
        managed = False  # Django won't create or modify this table
        db_table = 'search2'  # Ensure it matches the actual table name


# Model for search3 in db3
class Search3(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated primary key
    item = models.CharField(max_length=255)  # Character field for 'item'

    class Meta:
        managed = False  # Django won't create or modify this table
        db_table = 'search3'  # Ensure it matches the actual table name
