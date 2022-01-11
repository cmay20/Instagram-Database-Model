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
# US2 - As a Personal User, I want to communicate directly 
# with other users so that I can develop a relationship with them.

#-----------------------------------------------------------------
def show_US2_menu():
    heading("US2 - As a Personal User, I want to communicate directly \
    with other users so that I can develop a relationship with them")
    
    p_to = 2 # hardcode posted to user id for demonstration 
    p_by = 4 # hardcode posted by user id for demonstration 
    message = "hello" # hardcode message text for demonstration 
    US2(posted_to=p_to, posted_by=p_by, message_text=message)

def US2(posted_to, posted_by, message_text):
    tmpl = '''
        INSERT INTO Messages (posted_to,posted_by,message_text,time_sent)
        VALUES (%s, %s, %s, now());
        SELECT posted_to,posted_by,message_text,time_sent
        FROM Messages;
    '''
    cmd = cur.mogrify(tmpl, (posted_to, posted_by, message_text))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_table(rows, ['posted_to','posted_by','message','time_sent'])

    print("\nUS2 - As a Personal User, I want to communicate directly with other users so that I can develop a relationship with them.")
    print("\nDescription: This query is supposed to insert a new message that one user sent to another into the Messages table. We input a message by inserting the user id of who posted the message, the user id of who its posted by, the actual message text, and the current time. In this way, the query enables users to communicate directly with each other to build relationships.\n")

    


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

        show_US2_menu() #show user story 2 menu

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))