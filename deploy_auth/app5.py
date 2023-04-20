# is for blueprint and linking multiple files

from flask import Flask, render_template,Blueprint,request,url_for,redirect,session

from pyrebase import pyrebase  #imporrted through  pip install Pyrebase4



app5 = Flask(__name__, static_folder='static', template_folder='template')


config = {
    "apiKey": "AIzaSyCBJcsAZ4rNFCwERDp7fLGqX-5XQVaSdYg",
    "authDomain": "first-22545.firebaseapp.com",
    "projectId": "first-22545",
    "storageBucket": "first-22545.appspot.com",
    "messagingSenderId": "457245833938",
    "appId": "1:457245833938:web:de0d16ba7cb53074d10b0b",
"measurementId": "G-9LE5QCR3RJ",
	"databaseURL":" "

}

#mesurementId is only enabled when your project in Firebase is linked to google analytics
# databaseURL is left empty as we dont have a database linked but is included in config as the   classs  'firebase' in pyrebase.py
# assigns the value to a class property

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

@app5.route("/", methods=['GET', 'POST'])

def basic():

	unsuccessful = 'Please check your credentials'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			user = auth.sign_in_with_email_and_password(email, password)
			print(user)
			auth.send_email_verification(user['idToken'])  # will send authentication email
			#session['authenticated'] = True

			return render_template('video.html')

		except:
			auth.send_password_reset_email(email)

			return render_template('signIn.html', us=unsuccessful)

	return render_template('signIn.html')


@app5.route("/home")
def fun():
    return f'<h1> first home  </h1>'

if __name__ == "__main__":
    app5.run(debug=True,host='0.0.0.0', port=5000)
