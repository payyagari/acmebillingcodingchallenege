######## ACME BILLING SYSTEM ########
''' Ingester for reading in customer information and storing in our database. Please see DB schema provided '''

import sys
import datetime

def ingestCustInfo(filename):
    
   custInfoFile = open(filename,"r")
  
   for line in custInfoFile.readlines():
       
        tokens = line.split(',') #format uuid,name,email,address,city,state,zip
        uuid = tokens[0];
        name = tokens[1];
        email = tokens[2];
        address = tokens[3];
        city = tokens[4];
        zipcode = tokens[5];
        
        # Insert data into database
        query = "INSERT INTO CUSTOMER_INFO_TABLE(uuid,name,email,address,city,state,zip,date_updated) VALUES ("
                + uuid + ",'" + name + "','" + email + "','"+address+"','"+city+"','"+state+"',"+zipcode + ")"
                
        #### run query here and report any errors ####
        
   custInfoFile.close()
    
def main(argv):
    ingestCustInfo(argv[0])
    
if __name__ == "__main__":
    main(sys.argv[1:])
                         
                         
