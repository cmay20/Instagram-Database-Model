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
# US3 - As a Personal User, I want to see how many followers 
# I have so that I can see how many people interact with me on Instagram.

#-----------------------------------------------------------------
def show_US3_menu():
    heading("US3 - As a Personal User, I want to see how many followers I have so that I can see how many people interact with me on Instagram")
    
    my_uid = 3 # hardcode personal user id for demonstration 
    US3(uid_1=my_uid)

#Note: uid_1 is person being followed, uid_2 is person following uid_1

def US3(uid_1):
    tmpl = ''' SELECT COUNT(uid_2) as cnt
                 FROM Followers
                WHERE (uid_1 = %s);
    '''
    cmd = cur.mogrify(tmpl, (uid_1,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    colArray = ['cnt']
    print_table(rows, colArray)

    print("\nUS3 - As a Personal User, I want to see how many followers I have so that I can see how many people interact with me on Instagram.")
    print("\nDescription: This query is supposed to lookup the number of followers that the user currently has in the Followers table. In this way, users can use this query to see how many people follow their content on Instagram.\n")
    

    # ^ Don't print rows unless we do a select


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

        show_US3_menu() #show user story 3 menu

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))