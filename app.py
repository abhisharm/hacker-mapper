from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
import psycopg2
from werkzeug import generate_password_hash, check_password_hash
import add_to_latlng, get_dist
app = Flask(__name__)

mysql = MySQL()

 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ql#1Arbiter4578my'
app.config['MYSQL_DATABASE_DB'] = 'test_schema'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/showSignUp")
def showSignUp():
	return render_template('signup.html')

@app.route("/showLogIn")
def showLogIn():
	return render_template('login.html')

# @app.route('/logIn',methods=['POST'])
# def logIn():
# 	# read the posted values from the UI
# 	_address = request.form['inputEmail']
# 	_password = request.form['inputPassword']
# 	mysql.init_app(app) 
# 	conn = mysql.connect()
# 	cursor = conn.cursor()
# 	#_hashed_password = generate_password_hash(_password)
# 	cursor.callproc('sp_authUser',(_address,_password))
# 	data = cursor.fetchall()
#     print(data)
# 	if len(data) is 0:
# 		return json.dumps({'error':'user not found'})
# 	elif len(data[0] == len(_password)) :
# 		return json.dumps({'html':str(data[0])})

@app.route('/dashboard')
def dashboard():
	return render_template("/dashboard.html")

@app.route('/map',methods=['POST'])
def map():
	_location = request.form['inputCity']
	_contact = request.form['inputPhone']
	conn = mysql.connect()
	cursor = conn.cursor()
	print(_location)
	query3 = "select DISTINCT First_Name,user_username,Location FROM tbl_test GROUP BY Location='"+_location+"'"
	cursor.execute(query3)
	data1 = cursor.fetchall()
	lat_lng_loc = add_to_latlng.addToLatLng(_location)
	for x in data1:
		lat_lng_target = add_to_latlng.addToLatLng(x[2])
		x.append(str(get_dist.getDriveTime(lat_lng_loc,lat_lng_target)))
	return render_template('design.html', result = data1)

	#return(json.dumps({'html': str(data1)}))

@app.route('/signUp',methods=['POST'])
def signUp(): 
		# read the posted values from the UI
	_address = request.form['inputEmail']
	_password = request.form['inputPassword']
	mysql.init_app(app) 
	conn = mysql.connect()
	cursor = conn.cursor()
	# print("Address: "+_address)

	#_hashed_password = generate_p-assword_hash(_password)
	# cursor.callproc('sp_createUser',(_address,_password))
	# print("SELECT * FROM test_table WHERE user_username = ""+_address+"" ")
	#x=conn.query("SELECT * FROM test_table WHERE user_username = "+_address+" ")
	# print(cursor.execute("SELECT * FROM test_table WHERE user_username = ""+_address+"""))

	# query = "SELECT * from test_table where user_username= dhruvmalik133\@gmail.com "
	# cursor.query(query)
	# print("SELECT * FROM test_table WHERE user_username = ""+_address+"" ")
	query2 = "SELECT * FROM test_table WHERE user_username = '"+_address+"'"
	cursor.execute(query2)
	data1 = cursor.fetchall()
	if len(data1) is 0:
		query = "INSERT into test_table (user_username, user_password) VALUES ('"+_address+"','"+_password+"')"
		cursor.execute(query)
		return render_template("/list.html")
	elif len(data1) >= 1:
		return render_template("/list.html")
		
if __name__ == "__main__":
	app.run()