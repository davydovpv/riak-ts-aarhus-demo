#
#
#Will iterate through the demo-data-extract csv file and put into Riak in batches of 100
#SMDE 29/4/16

from riak import RiakClient
from datetime import datetime
import calendar
import csv
def changetime(stime):
            dt=datetime.strptime(stime,'%Y-%m-%dT%H:%M:%S')
            #print dt
            return calendar.timegm(datetime.timetuple(dt))*1000
            
c=RiakClient()
c.ping()


#to load data in the table

totalcount=0
batchcount=0
batchsize=100
ds=[]
t=c.table('aarhus')
print t


with open('./demo-data-extract.csv', 'rU') as infile:
    r=csv.reader(infile)
    for l in r:
		if l[0]!='status':
			newl=[l[0],str(l[3]),datetime.strptime(l[5],'%Y-%m-%dT%H:%M:%S'),int(l[1]),int(l[2]),int(l[4]),int(l[6])]
			totalcount=totalcount+1
			#print count
			ds.append(newl)
			batchcount=batchcount+1
			if batchcount==batchsize:
				#add the records to the table
				print "Count at  ", totalcount
				to=t.new(ds)
				print "Created ts object"
				print "Storage result:  ",to.store()
				batchcount=0
				ds=[]       
infile.close()
print "Input file closed"
to=t.new(ds)
if ds:
	print "Storage result:  ",to.store()
	print totalcount
