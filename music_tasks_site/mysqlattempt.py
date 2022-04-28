from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector


app = Flask(__name__)


@app.route('/')
def begin():
 return redirect(url_for('listoftasks'))


@app.route('/result')
def reroute():
 return redirect(url_for('listoftasks'))



@app.route('/listoftasks')
def listoftasks():
 my_db = mysql.connector.connect(
    host = 'b500u5coeyqxe74jtgz2-mysql.services.clever-cloud.com',
    user = 'u4guu7kkgslrpafp',
    database = 'b500u5coeyqxe74jtgz2',
    passwd = 'FstTZJ6TJJTxmEChRjMB',
    port = 3306
 ) 
 my_cursor = my_db.cursor(buffered=True,dictionary=True)
 my_cursor.execute("SHOW TABLES")
 my_cursor.execute("SELECT * FROM listoftasks")
 tasksforoutputlist = my_cursor.fetchall()   
 tasksforoutput = str(tasksforoutputlist)
 my_cursor.close()
 my_db.close()
 return render_template("listoftasks.html",listofwords=tasksforoutput) 


@app.route('/main', methods=['POST','GET'])
def main():
 my_db = mysql.connector.connect(
    host = 'b500u5coeyqxe74jtgz2-mysql.services.clever-cloud.com',
    user = 'u4guu7kkgslrpafp',
    database = 'b500u5coeyqxe74jtgz2',
    passwd = 'FstTZJ6TJJTxmEChRjMB',
    port = 3306
 ) 

 my_cursor = my_db.cursor(buffered=True,dictionary=True)
 #my_cursor.execute("SHOW DATABASES")

 #for db in my_cursor:
 #	print(db[0])
 #print(my_cursor)

 #print(my_db)
 #input()

 #my_cursor.execute("CREATE TABLE listoftasks (name VARCHAR(255),task VARCHAR(255),task_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
 my_cursor.execute("SHOW TABLES")
 #for table in my_cursor:
	#print ("your table: " + table[0])

 #inputtask = "INSERT INTO listoftasks (name,task) VALUES (%s,%s)"
 #task1 = ('Гриша','играй гамму до диез мажор')
 #my_cursor.execute(inputtask,task1)
 #my_db.commit()	

 my_cursor.execute("SELECT * FROM listoftasks")
 tasksforoutputlist = my_cursor.fetchall()
 #tasksforoutput = ''.join(tasksforoutputlist)
 tasksforoutput = str(tasksforoutputlist)
 print(tasksforoutput)
 #tasksforoutpu = 'lala'	
 my_cursor.close()
 my_db.close()
 return render_template("get1word.html",listofwords=tasksforoutput)


@app.route('/listoftasks', methods=['POST','GET'])
def deleting():
 my_db = mysql.connector.connect(
    host = 'b500u5coeyqxe74jtgz2-mysql.services.clever-cloud.com',
    user = 'u4guu7kkgslrpafp',
    database = 'b500u5coeyqxe74jtgz2',
    passwd = 'FstTZJ6TJJTxmEChRjMB',
    port = 3306
 ) 
 my_cursor = my_db.cursor(buffered=True,dictionary=True)
 #my_cursor.execute("DELETE * FROM listoftasks WHERE name='Гриша'")
 my_cursor.execute("TRUNCATE TABLE listoftasks")
 my_db.commit()
 my_cursor.execute("SELECT * FROM listoftasks") 
 tasksforoutputlist = my_cursor.fetchall()
 tasksforoutput = str(tasksforoutputlist)
 my_cursor.close()
 my_db.close()      
 return render_template("listoftasks.html",listofwords=tasksforoutput)


@app.route('/get2word', methods=['POST','GET'])
def update():
 wordsindb = request.form['text']
 my_db = mysql.connector.connect(
    host = 'b500u5coeyqxe74jtgz2-mysql.services.clever-cloud.com',
    user = 'u4guu7kkgslrpafp',
    database = 'b500u5coeyqxe74jtgz2',
    passwd = 'FstTZJ6TJJTxmEChRjMB',
    port = 3306
 )
 my_cursor = my_db.cursor(buffered=True,dictionary=True)
 inputname = "INSERT INTO listoftasks (name,task) VALUES (%s,%s)"
 name = (wordsindb,'_')
 my_cursor.execute(inputname,name)
 my_db.commit()
 my_cursor.execute("SELECT * FROM listoftasks")
 tasksforoutputlist = my_cursor.fetchall()
 tasksforoutput = str(tasksforoutputlist)
 my_cursor.close()
 my_db.close() 
 return render_template("get2word.html", listofwords=tasksforoutput)


@app.route('/result', methods=['POST','GET'])
def result():
 wordsindb = request.form['text2']
 my_db = mysql.connector.connect(
    host = 'b500u5coeyqxe74jtgz2-mysql.services.clever-cloud.com',
    user = 'u4guu7kkgslrpafp',
    database = 'b500u5coeyqxe74jtgz2',
    passwd = 'FstTZJ6TJJTxmEChRjMB',
    port = 3306
 )
 my_cursor = my_db.cursor(buffered=True,dictionary=True)
 my_cursor.execute("SELECT MAX(task_id) FROM listoftasks")
 inputtask = "UPDATE listoftasks SET task = %s WHERE task_id = %s"
 task_id_dict = my_cursor.fetchone()
 print(task_id_dict)
 task_id = task_id_dict.get('MAX(task_id)')
 task = (wordsindb,task_id)
 #my_cursor.execute(inputtask,task)
 my_cursor.execute(inputtask,task)
 my_db.commit()
 my_cursor.execute("SELECT * FROM listoftasks")
 tasksforoutputlist = my_cursor.fetchall()
 tasksforoutput = str(tasksforoutputlist)      	
 #tasksforoutput = 'tasks'	
 my_cursor.close()
 my_db.close()
 return render_template("result.html", listofwords=tasksforoutput) 


if __name__ == "__main__":
 app.run()




