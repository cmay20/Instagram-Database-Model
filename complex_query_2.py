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
# US8 - As a Personal User, I want to see who likes my posts 
# so that I know who is enjoying my content.
#-----------------------------------------------------------------
def show_US8_menu():
    heading("US8 - As a Personal User, I want to see who likes my posts so that I know who is enjoying my content")
    
    my_uid = 2 # hardcode personal user id for demonstration 
    my_post_id = 1 # hardcode post id for demonstration
    US8(uid_1=my_uid, post_id=my_post_id)


def US8(uid_1, post_id):
    tmpl = ''' SELECT l.liked_by as liked_by
                 FROM Users as u
   		              JOIN Posts as p ON u.uid=p.uid
		              JOIN Likes as l ON l.post_id=p.post_id
                WHERE u.uid = %s AND p.post_id = %s; 
    '''
    cmd = cur.mogrify(tmpl, (uid_1, post_id))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_table(rows, ['liked_by'])
    
    print("\nUS8 - As a Personal User, I want to see who likes my posts so that I know who is enjoying my content.")
    print("\nDescription: This query is supposed to lookup all the people who liked a specific user's post by joining the following three tables: User, Like, and Posts. \
            In this way, a specific user can find the people who liked one of their specific posts. \n")
    



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

        show_US8_menu() 

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))