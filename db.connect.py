#Python Database connectiviity.

import pymysql
import sys

#import datetime
#import decimal
#from dateutil.relativedelta import *
#import calendar
#from datetime import timedelta
#from sets import Set
## from datadog import statsd
#import json
#from print import print

db = pymysql.connect(host="localhost", # your host, usually localhost
port=3310,
user="root", # your username
passwd="paytm@123", # your password
db="wallet") # name of the data base

print ("Connection established!")

cur = db.cursor()

#cur.execute("select m.id , m.merchant_order_id ,m.payee_id ,m.txn_type, m.create_timestamp from (select id, merchant_order_id, is_settled,payee_id, txn_amount, txn_type, txn_status, create_timestamp, txn_message from new_system_txn_request where (payer_id='9234570080' or payee_id='2325')  order by create_timestamp) m where m.txn_type=1 and m.create_timestamp <(select s.create_timestamp from new_system_txn_request s where s.merchant_order_id='nishant1') order by m.create_timestamp desc limit 1;")

cur.execute("select phone_no,cust_id from user where sso_id = '9234583761'")

# fetch all of the rows from the query
#data = cur.fetchall ()

row = cur.fetchone ()

print(row)

while row is not None:
            print("row is **************************")
            for x in row:
               print(x)
            row = cur.fetchone()
# print the rows
#for row in data :
#print (row[0], row[1])

# close the cursor object
cur.close ()
# aux_cur = aux_db.cursor()
