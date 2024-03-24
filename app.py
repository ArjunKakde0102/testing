
# importing all the packages
from flask import Flask,render_template ,  redirect, request, flash,url_for
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import hashlib
from urllib.parse import quote_plus

#connecting with mysql


username =   'freedb_Arjun'
password = '9@z5*KK&eFcj3ed'
hostname = 'sql.freedb.tech'
port = 3306
database_name = 'freedb_Authentication'


connection_string = f"mysql+pymysql://{hostname}:{port}/{database_name}"

engine = create_engine(connection_string, connect_args={'user': username, 'password': password})



#engine = create_engine('mysql+pymysql://sql.freedb.tech:CWctm%YHDud4@QY@freedb_Arjun:3306/freedb_Authontication')




#Password hash



app = Flask(__name__)

app.secret_key = '12334'

@app.route('/')
def index():
    return "h"



#Register url
@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        register_password = hashlib.sha256(password.encode()).hexdigest() #password hashing
        mobile = request.form['mobile']
        email = request.form['email']
        vehicle_type  = request.form['vehicle-type']
        vehicle_number = request.form['vehicle-number']
        purchase_date = request.form['purchase-date']


        register_data = {'name' : [name],'register_password':[register_password], 'mobile' : [mobile], 'email':[email], 'vehicle_type' : [vehicle_type], 'vehicle_number': [vehicle_number], 'purchase_date': [purchase_date]}
        register_dataframe = pd.DataFrame(register_data)
        register_dataframe.to_sql(name= 'register_page' , con = engine, if_exists='append', index=False)
        return redirect('/login')
    return render_template("register.html")


#login url
@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        login_password = request.form['password']
        

        login_data =  {'user_id' : [username], 'login_passkey': [login_password]}
        login_dataframe = pd.DataFrame(login_data)
        login_dataframe.to_sql(name= 'login_page' ,con = engine, if_exists='append',  index=False)

        dataframe_password = pd.read_sql_query('select register_password from register_page',con=engine)
        hash_login_password = hashlib.sha256(login_password.encode()).hexdigest()
    

        if  hash_login_password in dataframe_password['register_password'].values :
            return redirect('/dashboard')
        




        
    return render_template("login.html")


#after login
@app.route('/dashboard', methods =["GET", "POST"])
def dashboard():
    return "login successfull"

if __name__ == "__main__":
    app.run(debug= True)
