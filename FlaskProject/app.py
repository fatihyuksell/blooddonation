from flask import Flask , request, redirect,session,url_for
import mysql.connector
from flask import render_template


app = Flask(__name__)



cursor = database.cursor(buffered=True)


@app.route('/')
def main_page():

    print(database.is_connected())
    return render_template("main.html")




@app.route("/register/", methods=["POST","GET"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    else:
        donor_id = request.form["donor_id"]
        donor_pass = request.form["donor_password"]

        donor_name = request.form["donor_name"]
        donor_surname = request.form["donor_surname"]
        donor_sex = request.form["donor_sex"]
        donor_age = request.form['donor_age']
        donor_adress = request.form["donor_adress"]



        print( donor_id, donor_name, donor_surname, donor_sex, donor_age, donor_adress,donor_pass)

        cursor.execute("select * from Donor")

        all_users = cursor.fetchall()
        print(all_users)
        check = True
        for user in all_users:
            if user[0] == donor_id:
                check = False

        if check == True:

            cursor.execute("insert into Donor(donor_id,donor_name,donor_surname,donor_sex,donor_age,donor_adress,donor_password)"
                           "values(%s,%s,%s,%s,%s,%s,%s)",(donor_id,donor_name,donor_surname,donor_sex,donor_age,donor_adress,donor_pass))
            database.commit()


            return redirect("/")

        else:
            return redirect("/register")
        return redirect("/")


@app.route("/login/", methods=["POST","GET"])
def login():
    msg = ''

    if request.method == "GET":
        return render_template("login.html")

    else:

        userid = request.form["user_id"]
        user_password = request.form["user_password"]

        cursor.execute('SELECT * FROM Donor WHERE donor_id = %s AND donor_password= %s', (userid, user_password,))
        oneuser = cursor.fetchone()

        if oneuser:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = oneuser[0]
            session['name'] = oneuser[2]
            # Redirect to home page
            print(1234)
            print(session)
            return render_template('main_after.html')

        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

        # Show the login form with message (if any)






@app.route('/blood_register/', methods=["POST","GET"])
def blood_register():
    # Check if user is loggedin
    if 'loggedin' in session:
        if request.method == "GET":
            return render_template('blood_register.html')
        else:
            print(session['id'])

            blood_type = request.form["blood_type"]
            blood_coding = request.form["blood_coding"]
            blood_donate = session['id']

            cursor.execute("select * from Blood")

            cursor.execute("insert into Blood(blood_type,blood_coding,blood_donate)"
                           "values(%s,%s,%s)", (blood_type, blood_coding,blood_donate))
            database.commit()

            return render_template('main_after.html')


        return render_template('main_after.html')
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))



@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)


   # Redirect to login page
   print(2345)
   return redirect(url_for('main_page'))





@app.route('/register2/',methods=['GET','POST'])
def register2():
    if request.method == "GET":
        return render_template("register2.html")

    else:
        man_id = request.form["man_id"]
        man_name = request.form["man_name"]
        man_phone = request.form["man_phone"]
        man_password= request.form["man_password"]


        print(man_id, man_name, man_phone)


        cursor.execute("select * from BloodManager")
        all_man=cursor.fetchall()
        print(all_man)

        check = True
        for bloodmanager in all_man:
            if bloodmanager[3] == man_id:
                check = False

        if check == True:

            cursor.execute("insert into BloodManager(man_id,man_name,man_phone,man_password)"
                           "values(%s,%s,%s,%s)", (man_id, man_name, man_phone,man_password))
            database.commit()
            print("burada2")
            return redirect("/")
        else:
            return redirect("/register2")



@app.route("/login2/", methods=["POST","GET"])
def login2():
    msg = ''

    if request.method == "GET":
        return render_template("login2.html")

    else:

        userid = request.form["user_id"]
        user_password = request.form["user_password"]

        cursor.execute('SELECT * FROM BloodManager WHERE man_id = %s AND man_password = %s', (userid, user_password,))
        oneuser = cursor.fetchone()

        if oneuser:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = oneuser[0]
            session['name'] = oneuser[2]
            # Redirect to home page
            print(1234)
            print(session)
            return render_template('man_after2.html')

        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

        # Show the login form with message (if any)



@app.route("/hospitals/")
def hospitals():



    cursor.execute("select * from Hospital")
    hospitals = cursor.fetchall()
    hospitals_list = []

    for any in hospitals:
        print(any[2])
        hospitals_list.append(any[0])

    return render_template("hospitals.html", content = hospitals_list)





@app.route("/bloodbanks/")
def Blood_Banks():

    cursor.execute("select * from BloodBank")
    bloodbank = cursor.fetchall()
    bloodbank_list = []

    for any in bloodbank:
        # print(any[2])
        bloodbank_list.append(any)

    return render_template("Blood_Bank.html" , content = bloodbank_list)








@app.route("/register3", methods = ["POST","GET"])
def register3():
    if request.method == "GET":
        return render_template("register3.html")
    else:
        pat_id= request.form["pat_id"]
        pat_name = request.form["pat_name"]
        pat_surname = request.form["pat_surname"]
        pat_age = request.form["pat_age"]
        pat_sex = request.form["pat_sex"]
        pat_blood = request.form["pat_blood"]
        pat_host = request.form["pat_host"]
        pat_password = request.form["pat_password"]

        print(pat_id,pat_name,pat_surname,pat_age,pat_sex,pat_blood,pat_host,pat_password)

        cursor.execute("select * from Patient")
        all_patient = cursor.fetchall()
        print(all_patient)


        check = True
        for patient in all_patient:
            if patient[3] == pat_id:
                check = False

        if check == True:

            cursor.execute("insert into Patient(pat_id,pat_name,pat_surname,pat_age,pat_sex,pat_blood,pat_host,pat_password)"
                           "values(%s,%s,%s,%s,%s,%s,%s,%s)", (pat_id,pat_name,pat_surname,pat_age,pat_sex,pat_blood,pat_host,pat_password))
            database.commit()
            print("burada")
            return redirect("/")
        else:
            return redirect("/register3")








@app.route("/bloods/")
def bloods():
    cursor.execute("select * from Blood")
    blood = cursor.fetchall()
    blood_list = []

    for any in blood:

        blood_list.append(any)

    return render_template("blood.html" , content = blood_list)















