from random import randrange
from random import random
from random import shuffle
from faker import Faker
from barnum import gen_data
import csv
fake = Faker()
d={}
i=0
with open('large_nodups.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    writer.writerow(['rownum'] +['dunno'] + ['CC'] + ['Employer'] + ['Custemail'] + ['name'] \
	+ ['occupation'] + ['address_street'] + ['DOB']+['previous address_city_state_zip']+ ['altcustomer_name'] \
	+ ['altcustomer_occupation']   + ['altcustomer_dob'] + ['ssn'] + ['phone']  + \
	['AccountID'] + ['PepFlag'] + ['altcustomerssn'] + ['demarketed_customer_flag'] + \
	['SAR_flag'] + ['nolonger_a_customer'] + ['closed_account'] +['High_risk_flag'] +['Risk_rating'])
    while i < 50000000:
		#Pick an account number and store it in acct 
		acct=randrange(100000,100000000,1)
		#if the account hasn't been already generated then generate a record with all fields
		if d.has_key(str(acct)) == False:
			row = [i] + [10] + [gen_data.cc_number()]+[gen_data.create_company_name()] + \
			[gen_data.create_email()]+[gen_data.create_name()] +[gen_data.create_job_title()] + \
			[gen_data.create_city_state_zip()] + [gen_data.create_birthday(min_age=2, max_age=85)] + \
			[gen_data.create_city_state_zip()] + [fake.name()] + [gen_data.create_job_title()] + \
			[gen_data.create_birthday(min_age=2, max_age=85)]  +\
			[(randrange(101,1000,1),randrange(10,100,1),randrange(1000,10000,1))] +  \
			[(randrange(101,1000,1),randrange(101,999,1),randrange(1000,10000,1))] + \
			[acct] + \
			[max((randrange(0,101,1)-99),0)] + \
			[(randrange(101,1000,1),randrange(10,100,1),randrange(1000,10000,1))] + \
			[max((randrange(0,101,1)-99),0)] + [max((randrange(0,101,1)-99),0)] + \
			[max((randrange(0,101,1)-99),0)] 	+ [max((randrange(0,101,1)-90),0)] + \
			[max((randrange(0,101,1)-99),0)] +  [max((randrange(0,101,1)-99),0)]
			d[str(acct)]=acct
			i=i+1
			writer.writerow(row)
