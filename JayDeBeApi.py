#reference : https://pypi.org/project/JayDeBeApi/
#import JayDeBeApi module
import jaydebeapi
import pandas as pd
import os

DriverPath = 'C:/suraj/<some_jdbc>.jar'
ClassName = 'com.<some>.connect.jdbc.driver'
jdbcUrl = 'jdbc:<someclient>://<server_name>:<port>/api'
UsrID = '<suraj>'
Pwd = '<***>'

columns = '*'
SrcTable = 'Employee'
Filter = 'Where true'
selectQuery = 'select {} from {} {}'.format(columns, SrcTable, Filter)

tgtDir = 'C:/'
tgtFiel = 'test1.csv'
NoRows = 20000

#Check if directory exists
if not os.path.exists(tgtDir):
  os.mkdir(tgtDir)

#Check if file exists and delete
if os.path.isfile(tgtDir+tgtFile):
  os.remove(tgtDir+tgtFile)
  Print('Deleted file : {}'.format(tgtFile))

 
with jaydebeapi.connect(ClassName, jdbcUrl,
                       {'user': UsrID, 'passowrd' : Pwd}, DriverPath) as Con:
   with Con.cusror() as cur:
      cur.execute(selectQuery)
      colNames = [i[0] for i in curs.description]
      b1 = pd.DataFrame(columns = colNames)
      b1.to_csv(tgtDir+tgtFile , mode='a', index=False)
      while True:
        try:
          b2 = pd.DataFrame(cur.fetchmany(size=NoRows))
          b2.to_csv(tgtDir+tgtFile, mode='a', index=False, header=False)
          if b2.empty:
            break
        except Exception as e:
          raise Exception('Failed to extract data to file {}'.format(str(e))

            
