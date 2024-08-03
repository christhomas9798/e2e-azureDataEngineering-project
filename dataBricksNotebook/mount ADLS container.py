# Databricks notebook source
dbutils.secrets.list('e2e-scope')

# COMMAND ----------

# Replace these variables with your specific values
storage_account_name = "e2e123678dl"
container_name = "bronze"
client_id = dbutils.secrets.get('e2e-scope','client-id')
tenant_id = dbutils.secrets.get('e2e-scope','tenant-id')
client_secret = dbutils.secrets.get('e2e-scope','client-secret')

# Configurations
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# Mount the storage
dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

# Verify the mount


# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

dbutils.fs.mount(
    source = f"abfss://silver@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/silver",
    extra_configs = configs)

# COMMAND ----------

dbutils.fs.mount(
    source = f"abfss://gold@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/gold",
    extra_configs = configs)

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

display(dbutils.fs.ls('/mnt/e2e123678dl/bronze/SalesLT'))

# COMMAND ----------

# MAGIC %sh
# MAGIC pwd

# COMMAND ----------


