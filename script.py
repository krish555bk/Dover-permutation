# importing csv module
import csv
import os
import whois


os.system('python permutation.py')
filename = "input1.csv"
 
fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)     
    for row in csvreader:
        rows.append(row)


filename = "output.csv"
fields = ['Domain name','Creation','ID','Location','IP','Expiration']
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

    for row in rows:
   	for col in row:
		try:
			x=whois.whois(col)
			csvwriter.writerow([(x.domain_name),
			(x.creation_date),
			(x.registry_domain_id),
			(x.state),
			(x.registrar),
			(x.expiration_date)])
		except(whois.parser.PywhoisError):
			print('\n')
	print('\n')


