from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, Settings
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something-super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\projects\\myCameraApp\\database.db'
Bootstrap(app)
db = SQLAlchemy(app)

class Setting(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	power = db.Column(db.Boolean)
	speed = db.Column(db.Float)
	

@app.route('/', methods=['GET', 'POST'])
def index():
	con = sql.connect("database.db")
	cur = con.cursor()
	
	cur.execute('select power from setting order by id desc limit 1;')
	power = cur.fetchall()

	cur.execute('select speed from setting order by id desc limit 1;')
	speed = cur.fetchall()

	con.close()
	

	form = LoginForm()
	error = None
	if form.validate_on_submit():
		if form.username.data != 'admin' or form.password.data != '12345678':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('dashboard'))
	return render_template("index.html", form=form, error=error, power=power, speed=speed)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
	form = Settings()
	message = ''
	if form.validate_on_submit():		
		new_setting = Setting(power=form.power.data, speed=form.speed.data)
		db.session.add(new_setting)
		db.session.commit()
		message = "Configurations have been changed."
		
	return render_template("dashboard.html", form=form, message=message)


@app.route('/logout')
def logout():
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)