__author__ = 'vivek.gour'



import pymssql

conn = pymssql.connect(server='175.41.138.226:3784', user='CEVA_READER', password='fe3A7deF4889a', database='live_billingrating', as_dict=True)
cursor = conn.cursor()
cursor.execute("Select top 10 * from invoicebilling")
row = cursor.fetchone()

while row:
    print "Invoice = %s, Amount = %s" % (row['InvoiceNumber'],row['BillingAmount'])
    row = cursor.fetchone()

conn.close()