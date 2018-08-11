from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
#app.config['SQLALCHEMY_DATABASE_URI']='postgres://xzakckjeqdklvk:02d4e730ae61227c88af4d341395335e9c89df47e232c4af59bd5710a66b5eb7@ec2-54-225-76-201.compute-1.amazonaws.com:5432/dd7rfkvdooo8li?sslmode=require'
app.config['SQLALCHEMY_BINDS'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120), unique=True)
    height=db.Column(db.Integer)

    def __init__(self, email, height):
        self.email=email
        self.height=height

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        print(email, height)
        if db.session.query(Data).filter(Data.email == email).count()== 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height)).scalar()
            average_height=round(average_height, 1)
            count = db.session.query(Data.height).count()
            send_email(email, height, average_height, count)
            print(average_height)
            return render_template("success.html")
    return render_template('index.html', text="Seems like we got something from that email once!")

if __name__ == '__main__':
    app.debug=True
    app.run()
