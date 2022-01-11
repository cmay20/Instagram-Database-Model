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
# US10 - As a Content Creator, I want to see all of my followers that are also 
# Content Creators with similar interests so that I can determine who might want to 
# collaborate with me. (NEW FEATURE)

#-----------------------------------------------------------------
def show_US10_menu():
    heading("US10 - As a content creator, I want to see all of my followers that are also content creators with similar interests so that I can determine who might want to collaborate with me (NEW FEATURE)")
    
    my_uid = 1 # hardcode personal user id for demonstration 
    my_category = "blogger" # hardcode category for demonstration
    US10(uid_1=my_uid, category=my_category)

#Note: uid_1 is person being followed, uid_2 is person following uid_1

def US10(uid_1,category):
    tmpl = ''' SELECT f.uid_2 as followers
                 FROM Users as u
  		              JOIN Followers as f ON u.uid = f.uid_1 
		              JOIN Content_Creator as c ON f.uid_2 = c.uid
                WHERE u.uid = %s AND c.category = %s
    '''


    cmd = cur.mogrify(tmpl, (uid_1,category))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_table(rows, ['followers'])
    
    print("\nUS10 - As a content creator, I want to see all of my followers that are also content creators with similar interests so that I can determine who might want to collaborate with me. (NEW FEATURE)")
    print("\nDescription: This query is supposed to lookup a user's followers that are also content creators with the same category. To do this, the query joins the following tables: User,Followers,Content_Creator. In this way, a creator can determine who to collaborate with. This is a new feature for Instagram. Currently, Instagram is unable to display this list of possible collaborators based on followers, user type, and creator category.\n")
    



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

        show_US10_menu() 

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))