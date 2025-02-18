bind = "unix:/tmp/vestuar_bancos.sock"
workers = 3
errorlog = "/var/log/gunicorn/vestuar_bancos_error.log"
accesslog = "/var/log/gunicorn/vestuar_bancos_access.log"
loglevel = "info"
raw_env = ["DJANGO_SETTINGS_MODULE=core.settings"]
