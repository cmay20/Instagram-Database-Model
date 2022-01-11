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
# US1: As a Personal User, I want to create a post so that I can share my 
# experiences with friends and family.
#-----------------------------------------------------------------
def show_US1_menu():
    heading("US1 - As a Personal User, I want \
    to create a post so that I can share my experiences with friends and family")
    
    post_type = "picture" # hardcode post type for demonstration
    caption = "yay!" # hardcode new caption for demonstration
    posted_by = 2 # hardcode posted by user id for demonstration
    US1(post_type=post_type, caption=caption, uid=posted_by)

def US1(post_type, caption, uid):
    tmpl = '''
        INSERT INTO Posts(type, caption, uid)
        VALUES (%s, %s, %s);
        SELECT type, caption, uid
        FROM Posts;
    '''
    cmd = cur.mogrify(tmpl, (post_type, caption, uid)) 
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()

    print_table(rows, ['type','caption','uid'])
    
    print("\nUS1: As a Personal User, I want to create a post so that I can share my experiences with friends and family.")
    print("\nDescription: This query is supposed to insert a new post created by a user into the Posts table. We insert the post type, caption and who it was posted by. The post_id is automatically generated since it is a serial type. In this way, the query enables users to share their experiences through posts.\n")
    
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
       
        show_US1_menu() #show user story 1 menu

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))