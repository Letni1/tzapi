NBU_STAT_URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'

SECRET_KEY = '0b7d8a6df726145a0228b990e8c444347b53baa55883ada8934debadf63b0582'
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
API_V1_STR = "/api/v1"

REDIS_PASS = 'admin'
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_DBNUM = 0
REDIS_URL = f'redis://:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DBNUM}'

BROKER_USER = 'guest'
BROKER_PASS = 'guest'
BROKER_HOST = 'localhost'
BROKER_PORT = '5672'
BROKER_VHOST = 'vhost'
BROKER_URL = f'amqp://{BROKER_USER}:{BROKER_PASS}@{BROKER_HOST}:{BROKER_PORT}/{BROKER_VHOST}'

POSTGRES_SERVER = 'postgres'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'postgres'
POSTGRES_DB = 'nbu'
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
)
USERS_OPEN_REGISTRATION = True

MONGO_USER = 'admin'
MONGO_PASS = 'admin'
MONGO_HOST = 'localhost'
MONGO_PORT = '27017'
MONGO_DB = 'stats'
MONGO_AUTH = 'admin'

MONGODB_URL = f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource={MONGO_AUTH}'

mongo_db_name = MONGO_DB
exchange_collection_name = 'exchange'
