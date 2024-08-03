# Databricks notebook source
# MAGIC %md
# MAGIC display(dbutils.fs.ls('/mnt/e2e123678dl/bronze/SalesLT'))

# COMMAND ----------

# MAGIC %md
# MAGIC df=spark.read.format("parquet").load('/mnt/e2e123678dl/bronze/SalesLT/Address/')

# COMMAND ----------

# MAGIC %md
# MAGIC display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC df=df.withColumn("ModifiedDate",df["ModifiedDate"].cast("date"))

# COMMAND ----------

# MAGIC %md
# MAGIC display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC df.columns

# COMMAND ----------

# MAGIC %md
# MAGIC address_df=df

# COMMAND ----------

from pyspark.sql.functions import col,length,expr,substring
table_names=[]
for i in dbutils.fs.ls('/mnt/e2e123678dl/bronze/SalesLT'):
    table_names.append(i.name[:-1])

# COMMAND ----------

print(table_names)

# COMMAND ----------

for i in table_names:
    df=spark.read.format('parquet').load(f'/mnt/e2e123678dl/bronze/SalesLT/{i}/')
    for j in df.columns:
        if "date" in j or "Date" in j:
            df=df.withColumn(j,df[j].cast("date"))
    df.write.format('delta').mode('overwrite').save(f'/mnt/e2e123678dl/silver/SalesLT/{i}/')


# COMMAND ----------

# MAGIC %md
# MAGIC display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC df=spark.read.format('delta').load('/mnt/e2e123678dl/silver/SalesLT/Address')

# COMMAND ----------

# MAGIC %md 
# MAGIC display(df)
