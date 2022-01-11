#-----------------------------------------------------------------
# Working with psycopg2
#-----------------------------------------------------------------

import psycopg2
import sys
from prettytable import PrettyTable

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')    

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_table(rows, columnsArray):
    table = PrettyTable(columnsArray)
    for row in rows:
        table.add_row(row)
    print(table)
    print()


#-----------------------------------------------------------------
# US6 - As a Business, I want to know the average cost of ads so 
# that I can budget marketing expenses.
#-----------------------------------------------------------------
def show_US6_menu():
    heading("US6 - As a Business, I want to know the average cost of ads so that I can budget marketing expenses")
    uid = 5 # hardcode business user id for demonstration 
    US6(b_uid=uid)


def US6(b_uid):
    tmpl = ''' SELECT ROUND(AVG(ad_cost),2) as avg
                 FROM Advertisement
                WHERE b_uid = %s;
    '''
    cmd = cur.mogrify(tmpl, ([b_uid]))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_table(rows, ['avg'])
    
    print("\nUS6 - As a Business, I want to know the average cost of ads so that I can budget marketing expenses.")
    print("\nDescription: This query is supposed to lookup the average cost of advertisements in the Advertisement table for a business to be able to budget marketing expenses. \n ")
    



if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'instagram', 'isdb'
        # you may have to adjust the user 
        # python a4-socnet-sraja.py a4_socnet postgres
        if len(sys.argv) >= 2:
            db = sys.argv[1]
        if len(sys.argv) >= 3:
            user = sys.argv[2]
        # by assigning to conn and cur here they become
        # global variables.  Hence they are not passed
        # into the various SQL interface functions
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()

        show_US6_menu() 

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))