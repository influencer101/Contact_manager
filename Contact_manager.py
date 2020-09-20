
def create_table(db, tname, **columns):
    c_str = ''
    for c, t in columns.items():
        c_str += '{} {}, '.format(c, t)
    c_str = c_str[:-2]

    try:
        cur = db.cursor()
        cur.execute('create table if not exists {} ({})'.format(
            tname, c_str))
        db.commit()
        return True
    except Exception as e:
        print('error creating the table', tname)
        print(e)
        return False
    pass
#===========================================================================

def add_contact() :
    add_name=input('\tEnter name : ')
    add_num=input('\tEnter number : ')
    try:
        add_num = int(add_num)
    except Exception as e:
        print('Enter valid number')
    try:
        cur = db.cursor()
        cur.execute('insert into Contact values ("{}","{}")'.format(add_name, add_num,))
        db.commit()
        return True
    except Exception as e:
        print('error inserting into the table')
        print(e)
        return False
    pass
#======================================================================

def update_contact():
    sel=input("Select an option \n\t1-Update Name\n\t2-Update Number \n\tEnter code:")
    sel=int(sel)
    if sel==1:
        upd_name1=input("Enter your new name:")
        upd_name2=input("Enter your old name ")
        a=name_check(upd_name2)
        try:
            if a.fetchone()==None:
                print ('Name does not exist')
            else:
                cur = db.cursor()
                cur.execute('update Contact set name="{}" where name="{}"'.format(
                    upd_name1,upd_name2,))
                db.commit()
                print('Conntact Updated')
        except Exception as e:
            print('error while updating in Contact')
            print(e)
            return False
        pass
    elif sel==2:
        upd_name2=input("Enter your  name:")
        upd_number2=input("Enter your new number")
        try:
            upd_number2=int(upd_number2)
        except Exception as e:
            print ('Enter valid number')

        a=name_check(upd_name2)
        try:
            if a.fetchone() == None:
                print('Name does not exist')
            else:
                cur = db.cursor()
                cur.execute('update Contact set number="{}" where name="{}"'.format(
                    upd_number2,upd_name2,))
                db.commit()
                print ('Conntact Updated')
        except Exception as e:
            print('error while updating in Contact')
            print(e)
            return False
        pass
#======================================================

def search_contact():
    sel=input('\n\t1-Search by name\n\t2-Search by number\n\tEnter answer: ')
    sel=int(sel)
    if sel==1:
        search_name=input('\n\tEnter name : ')
        try:
            cur = db.cursor()
            cur.execute('Select * from Contact where name ="{}"'.format(
                search_name,))
            db.commit()
            return cur
        except Exception as e:
            print('error while Searching in Contact')
            print(e)
            return False
        pass
    if sel==2:
        search_num=input('\n\tEnter number : ')
        try:
            search_num=int(search_num)
        except Exception as e:
            print ('Enter valid number')
        try:
            cur = db.cursor()
            cur.execute('Select * from Contact where number ="{}"'.format(
                search_num,))
            db.commit()
            return cur
        except Exception as e:
            print('error while Searching in Contact ')
            print(e)
            return False
        pass
#================================================
def view_all_contacts():
    try:
        cur = db.cursor()
        cur.execute('select * from Contact')
        return cur
    except Exception as e:
        print('error readin values from Contact')
        print(e)
        return None

#==================================================
def delete_contact():
    inp_name=input("\n\tEnter name you want to delete: ")
    try:
        a=name_check(inp_name)
        if a.fetchone()==None:
            print ('Name does not exist')
        else :
            cur=db.cursor()
            cur.execute('Delete from Contact where name="{}"'.format(inp_name,))
            db.commit()
            print('Contact Deleted successfully ')
    except Exception as e:
        print('error Deleting values from Contact')
        print(e)
        return None

#==============================================================
def name_check(x):
    cur = db.cursor()
    cur.execute('Select * from Contact where name ="{}"'.format(
    x,))
    db.commit()
    return cur

def Contact_MANG():
    print("\t**********************************************")
    print("\t***  CONTACT MANAGER  ***")
    print("\t**********************************************")
    cur = db.cursor()
    cur.execute('create table if not exists Contact(name text PRIMARY KEY, number int UNIQUE)')
    exit_opt=True
    while (exit_opt):
        sel1 = (
            '\tPress  \n\t1. ADD CONTACT \n\t2.UPDATE CONTACT\n\t3.SEARCH CONTACT\n\t4.VIEWALL\n\t5.DELETE CONTACT\n\t0.Exit application\n\tEnter number:')
        sel = int(input(sel1))
        if sel == 1:
            try:
                a = add_contact()
                print ('Contact added successfully ')
            except Exception as e:
                print ('Error adding contact')
                print (e)
        elif sel == 2:
            try :
                a = update_contact()
            except Exception as e :
                print ('Update Failed')
                print (e)
        elif sel == 3:
            a = search_contact()
            for i in a:
                print(i)
        elif sel == 4:
            a = view_all_contacts()
            for i in a:
                print(i)
        elif sel == 5:
            a = delete_contact()
        elif sel==0:
            exit_opt=False
            print ('You have exited the application successfully ')
        else:
            print('Kindly enter a valid number')


import sqlite3
import os
db = sqlite3.connect('CONTACT_MANAGE')
cur = db.cursor()
Contact_MANG()
#print(a)
db.close()