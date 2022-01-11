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
# US9 - As a Content Creator, I want to be able to see which post has
#  the most likes to see how effective the Instagram promotion feature is.
#-----------------------------------------------------------------
def show_US9_menu():
    heading("US9 - As a Content Creator, I want to be able to see which of my posts has the most likes to see how effective the Instagram promotion feature is")
    
    my_uid = 1 # hardcode personal user id for demonstration 
    US9(uid_1=my_uid)


def US9(uid_1):
    tmpl = '''SELECT s1.post_id 
                FROM (SELECT post_id, COUNT(liked_by) as cnt
                        FROM Likes
                       WHERE post_id = (SELECT p.post_id
                                          FROM Users as u
                                               JOIN Posts as p ON p.uid = u.uid
                                         WHERE u.uid = %s)
                       GROUP BY post_id
                       ORDER BY cnt DESC
                       LIMIT 1) as s1;
    '''


    cmd = cur.mogrify(tmpl, ([uid_1]))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_table(rows, ['post_id'])
    
    print("\nUS9 - As a Content Creator, I want to be able to see which post has the most likes to see how effective the Instagram promotion feature is.")
    print("\nDescription: This query is supposed to lookup the user's post with the most number of likes by joining the following tables: User, Like, and Posts. The query calculates the post with the most likes by counting each post's likes and ordering by descending so the max is on top with a limit of 1. Then, the query gets the post_id that is in that list of 1 post_id and its count. In this way, a user can determine which post is most liked to see how effective the Instagram promotions feature is for them. \n")
    



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

        show_US9_menu() 

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))