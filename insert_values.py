import sqlite3 as sql

def add_data():  
  try:
    print("success")
    # Connecting to database
    con = sql.connect('ngos.db')
    # Getting cursor
    c = con.cursor() 
    print('success')
    # Adding data
    print('{}'.format('222'))
    #c.execute("SELECT * FROM Member")
    c.execute("INSERT INTO Member (id, mobile, mobile_device_id, name, email, password) VALUES (1, 999999999, 9596 4569 9455 5, A Name, email@email.com, null)")
    # Applying changes")
    con.commit() 
    print(c)
  except:
    print("An error has occured")

add_data()