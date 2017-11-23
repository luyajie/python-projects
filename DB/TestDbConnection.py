#!/usr/bin/python3.5

import pypyodbc
import pandas as pd
import datetime


print ('-------------------------------------')
print ('Checking DB connectivity\n\n')

database_host = 'server-name.full.domain'
database_name = 'TestPrices'
driver_name = 'Driver={SQL Server Native Client 11.0}'

today_str = datetime.date.today()

# windows
# output_file_path = 'E:\\writeshare\\Test_{0}.csv'.format(today_str)

# linux
output_file_path = os.path.expanduser('~/Documents/data/files/Test_{0}.csv'.format(today_str))


sql_str = '''select * from
Genesis
where 
      UNDERLYING_ID > 0
  and SECURITY_TYP in ('ETP', 'Common Stock')
order by BBG_TICKER'''


connect_str = '{0};Server={1};Database={2};trusted_connection=yes'.format(driver_name, database_host, database_name)
cnxn = pypyodbc.connect(connect_str)
df = pd.read_sql_query(sql_str, cnxn)
# df.columns = [x.upper() for x in df.columns]
df.columns = map(str.upper, df.columns)
df.to_csv(output_file_path, sep=',', header=True, index=False)

print('Output file created at: {0}'.format(output_file_path ))

cnxn.close()
print ('-------------------------------------')
