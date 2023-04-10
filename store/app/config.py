import os
configs = {"SECRET_KEY": "test213", "salt": "S3cr3t!", "sqlite_db":"passwords.hb", }
db_config = {"database": os.getenv('POSTGRES_DB'), "host":"postgres","user": os.getenv('POSTGRES_USER'), "password": os.getenv('POSTGRES_PASSWORD'), "port": "5432"}
print(db_config)
