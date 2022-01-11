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
# US5 - As a Business, I want to see the number of content creators from each category 
# so I can determine which category of creators would be least exposed to 
# competitiveness in a branded partnership.


#-----------------------------------------------------------------
def show_US5_menu():
    heading("US5 - As a Business, I want to see the number of content creators from each category so I can determine which category of creators would be least exposed to competitiveness in a branded partnership")
    
    US5()


def US5():
    tmpl = ''' SELECT category, COUNT(uid) as cnt
                 FROM Content_Creator
                GROUP BY category
                ORDER BY category ASC;
    '''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_table(rows, ['category','cnt'])
    
    print("\nUS5 - As a Business, I want to see the number of content creators from each category so I can determine which category of creators would be least exposed to competitiveness in a branded partnership.")
    print("\nDescription: This query is supposed to lookup the total number of content creators of each category in the Content_Creator table and order in ascending order. In this way, a business gets a clean list of categories and their number of creators with the least on top and most at the bottom. A business can use this information to determine the category of creator they want in a branded partnership that would offer either low or high competitiveness with other creators.\n")
    



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

        show_US5_menu() 

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))