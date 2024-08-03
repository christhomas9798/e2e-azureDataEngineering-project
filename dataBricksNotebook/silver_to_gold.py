# Databricks notebook source
# MAGIC %md
# MAGIC df=spark.read.format('delta').load('/mnt/e2e123678dl/silver/SalesLT/Address/')

# COMMAND ----------

# MAGIC %md
# MAGIC display(df)

# COMMAND ----------

table_names=[]
for t in dbutils.fs.ls('mnt/e2e123678dl/silver/SalesLT/'):
    table_names.append(t.name[:-1])

# COMMAND ----------

print(table_names)

# COMMAND ----------

for t in table_names:
    df=spark.read.format('delta').load(f'/mnt/e2e123678dl/silver/SalesLT/{t}/')
    for i in df.columns:
        k=i[0].lower()
        for j in range(1,len(i)):
            if i[j].isnumeric():
                k=k+i[j]
                continue
            if i[j-1].isupper():
                k=k+i[j].lower()
                continue
            if i[j].islower():
                k=k+i[j]
                continue
            if i[j].isupper():
                k=k+'_'+i[j].lower()
        #print(k)
        df=df.withColumnRenamed(i,k)
    df.write.format('delta').mode('overwrite').save(f'/mnt/e2e123678dl/gold/SalesLT/{t}/')



# COMMAND ----------

# MAGIC %md
# MAGIC display(df)
