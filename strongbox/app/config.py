import os
configs = {"SECRET_KEY": "90e714e15f86badc25dd703620d8151d", "salt": "S3cr3t!", }
db_config = {"database": os.getenv('POSTGRES_DB'), "host":"postgres","user": os.getenv('POSTGRES_USER'), "password": os.getenv('POSTGRES_PASSWORD'), "port": "5432"}
print(db_config)
