ALLOWED_HOSTS = ["*"]
DEBUG = True

DATABASES = {
    "default" : {
        "ENGINE" : "django.db.backends.postgresql",
        "NAME" : "euc",
        "USER" : "rahmatkulov",
        "PASSWORD" : "admin",
        "HOST" : "localhost",
        "PORT" : "5432",
        "ATOMIC_REQUEST" : True,
    }
}

HOST = "https://localhost:8000"

