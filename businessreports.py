########### ACME BILLING SYSTEM ############
''' Code for monthly business admin reports '''
import sys

def get_totals(month):
    #run queries on DB
    
    #get total # of successfully generated and emailed invoices
    query = "SELECT count(*) from INVOICE_TABLE where month="+month;
    
    #get total amount for the month
    query = "SELECT SUM(amount_due) from INVOICE_TABLE where month="+month;
    
    #run on DB and print
    
def main(argv):
    get_totals(argv[0]) # month is sent as a command line argument
    
    
if __name__ == "__main__":
    main(sys.argv[1:])