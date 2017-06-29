###### ACME BILLING SYSTEM #######
''' Invoice Generator '''
import sys
import random
import datetime

custInfoMap = {}

''' Function to load up customer info in a global data structure.
    We obtain the list of uuids that *do not yet have an invoice*
    generated for the current month in our database. 
    In order to obtain this list of uuids, we get the list of uuids
    that exist in our customer info table but do not have an invoice generated and emailed for this month '''

def loadCustInfo(currentMonth,currentYear):
    
   query = "SELECT * from CUSTOMER_INFO_TABLE WHERE UUID NOT IN (SELECT UUID FROM INVOICE_TABLE WHERE MONTH="+currentMonth+" AND YEAR="+currentYEAR +")"
   #run query on DB
   #let's assume for the purpose of this assigment that the query results are a list of comma separated strings
   #in the format uuid,name,email,address,city,state,zip.

   for line in testinput:
    tokens = line.split(',') #format uuid,name,email,address,city,state,zip
    uuid = tokens[0]
    custInfoMap[uuid] = {
                         'name':tokens[1],
                         'email':tokens[2],
                         'address':tokens[3],
                         'city':tokens[4],
                         'zip':tokens[5]
                         }
                         

''' Function to get amount due from REST API.
    Simulating for the purpose of this assignment '''
def getAmountDue(uuid,month,year):
    url = "http://api.acme.fake/due/"+uuid+"/"+month+"/"+year
    #Assume REST API call is made here using the above url and the response below is returned
    #We set error code to 0 if API call was a success, otherwise it's set to 1
    response = {'amount_due':random.randint(0,10000),'error_code':random.randint(0,1)}
    return response

''' Function to log and report errors '''
def logAndReportError(uuid,month,year):
    #call to logging/error reporting system
    return

''' Function to get invoice message string '''
def getInvoiceMessageString(uuid, month, amount_due):
    msg = "Dear " + custInfoMap[uuid]['name'] + ",\nThank you for using Acme Water for your address at " +
          custInfoMap[uuid]['address'] + " " + custInfoMap[uuid]['city'] + ", " + custInfoMap[uuid]['state'] + " " +
          custInfoMap[uuid]['zip'] + ". Your amount due for the month of " + month + " is $" + amount_due + "."
    return msg
    
''' Simulated Function to send email '''
def emailInvoice(uuid,msg):
    #send 'msg' to custInfoMap[uuid]['emai']
    err_code = random.randint(0,1)
    return err_code

''' Simulated Function to save invoice to database '''
def saveInvoiceToDB(uuid,month,year,invoiceMessage):
    query = "INSERT into invoiceTable(uuid,month,year,invoice) VALUES("+uuid+","+month+","+year+","+invoiceMessage+")"
    #run query and return error code of 0 for success, 1 for failure
    err_code = random.randint(0,1)
    return err_code

''' Function to generate billing statement for a given uuid'''
def generateBillingStatementUUID(uuid,month,year):
    
    response = getAmountDue(uuid,month,year)
    
    if response.error_code == 0 : #success
        invoiceMessage = getInvoiceMessageString(uuid, month, response['amount_due'])
        #persist in database - save <uuid,month,year,invoiceMessage>
        sret = saveInvoiceToDB(uuid,month,year,invoiceMessage)
        
        if sret != 0:
            #log/report error
            return 1
            
        eret = emailInvoice(uuid,invoiceMessage)
        if eret != 0:
            #log/report error
            #DELETE ABOVE INVOICE FROM DB. We only store successfully generated AND emailed invoices.
            return 1
        
        return 0 #success
    else:
        return 1 #failed!!!
       
''' Function to run billing statements for all customers '''
def generateAllBillingStatements(currentMonth,currentYear):
    
    for uuid in custInfoMap:
        retc = generateBillingStatementUUID(uuid,currentMonth,currentYear)
        
        if retc != 0 : #success
            logAndReportError(uuid,currentMonth,currentYear)
    
def main(argv):
    
  #Get date
  todayDate = datetime.datetime.now()
  currentMonth = todayDate.month
  currentYear = todayDate.year
 
  loadCustInfo(currentMonth,currentYear)
  generateAllBillingStatements(currentMonth,currentYear)
  
if __name__ == "__main__":
  main('test')
  