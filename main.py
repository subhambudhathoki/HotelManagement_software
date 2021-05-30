import sqlite3

def connect():
    conn=sqlite3.connect("hotel.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST hotel (id INTEGER PRIMARY KEY , name TEXT , address TEXT , phone_number INTEGER, no_of_days INTEGER , room_type TEXT ,total INTEGER")
    conn.commit()
    conn.close()
def insert(name,address,phone_number,no_of_days,room_type,total):
    from back import calculation
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO hotel VALUE (NULL,?,?,?,?,?,?)"(name,address,phone_number,no_of_days,room_type,calculation(no_of_days,room_type)))





def calculation(no_of_days,room_type):
    if room_type==("normal"):
        total=int(no_of_days)*3000
        return total
    elif room_type==("deluxe"):
        total=int(no_of_days)*4500
        return total
    elif room_type==("suite"):
        total=int(no_of_days)*6000
        return total


