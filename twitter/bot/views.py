from django.shortcuts import render
from django.http import HttpResponse
from sqlalchemy import create_engine, false, null
from sqlalchemy import text
import json

user="root"
passw="123456"
host="172.17.0.2"
port="3306"
db="Twitter"


# This engine just used to query for list of databases
mysql_engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}'.format(user, passw, host, port))

# Query for existing databases
mysql_engine.execute("CREATE DATABASE IF NOT EXISTS {0} ".format(db))

# Go ahead and use this engine
#
db_engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(user, passw, host, port,db))


def index(request):
    return HttpResponse("Hello world!")
