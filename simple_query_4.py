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
# US4 - As a Content Creator, I want to know the branded partnership 
# that costs the most money so that I know who not to partner with again in the future.
#-----------------------------------------------------------------
def show_US4_menu():
    heading("US4 - As a Content Creator, I want to know the branded partnership that costs the most money so that I know who not to partner with again in the future")
    
    my_uid = 1 # hardcode content creator user id for demonstration 
    US4(uid_1=my_uid)


def US4(uid_1):
    tmpl = ''' SELECT b_uid, MAX(partnership_cost) as max
                 FROM Partners_With
                WHERE cc_uid = %s
                GROUP BY b_uid;
    '''
    cmd = cur.mogrify(tmpl, ([uid_1]))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_table(rows, ['b_uid','max'])
    
    print("\nUS4 - As a Content Creator, I want to know the branded partnership that costs the most money so that I know who not to partner with again in the future.")
    print("\nDescription: This query is supposed to lookup the businesses in the Partners_With table that a partnership with would cost the most. In this way, users can use this query to budget their partnerships and help them decide who to partner with again.\n")
    



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

        show_US4_menu() 

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))