workers = 2
worker_class = "gevent"
bind = "0.0.0.0:8000"
errorlog = 'log/gunicorn.error.log'
accesslog = 'log/gunicorn.access.log'
access_log_format = '%(h) -  %(t)s - %(u)s - %(s)s %(H)s'
error_log_format = '%(h) -  %(t)s - %(u)s - %(s)s %(H)s'
daemon = True
workers = 4
# 指定每个工作者的线程数
threads = 2
# 设置最大并发量
worker_connections = 2000
