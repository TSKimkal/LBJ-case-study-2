from flask import Flask, redirect, url_for, render_template, request, flash
import csv
import pandas as pd


filename="students.csv"

def entry():
	field=["student_id","name","gender","DateOfBirth","City","State","EmailId","Qualification","Stream"]
	with open(filename,'w',newline='') as csvfile:
		csvwriter=csv.writer(csvfile)
		csvwriter.writerow(field)

student_id=0
name=""
gender=""
DateOfBirth=''
City=''
State=''
EmailId=''
Qualification=''
Stream=''
filename="students.csv"
csvfile=open(filename,'a+',newline='')
csvwriter=csv.writer(csvfile)


app= Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=["POST","GET"])
def home():
	return render_template("index.html")

@app.route('/new_entry',methods=["POST","GET"])
def route1():
	if request.method =="POST":
		student_id=request.form["s_id"]
		name=request.form["s_name"]
		gender=request.form["gender"]
		DateOfBirth=request.form["date"]
		City=request.form["city"]
		State=request.form["state"]
		EmailId=request.form["email"]
		Qualification=request.form["quali"]
		Stream=request.form["stream"]
		data=[]
		data.append(student_id);
		data.append(name)
		data.append(gender)
		data.append(DateOfBirth)
		data.append(City)
		data.append(State)
		data.append(EmailId)
		data.append(Qualification)
		data.append(Stream)
		print(data)
		with open(filename,'a+',newline='') as csvfile:
			csvwriter=csv.writer(csvfile)
			csvwriter.writerow(data)
		return render_template("add-student.html")
	else:
		return render_template("add-student.html")

    

@app.route('/display')
def route2():
	fields = [] 
	rows = [] 
	  
	with open(filename, 'r') as csvfile: 
	    csvreader = csv.reader(csvfile) 
	    fields = next(csvreader)
	    rows.append(fields) 
	    for row in csvreader: 
	        rows.append(row)   
	# print(fields)
	# print(rows)
	fields=pd.DataFrame(fields)
	rows=pd.DataFrame(rows)
	return render_template("display-student.html",data=rows.to_html(header=False,index=False))

@app.route('/search',methods=["POST","GET"])
def route3():
	data_send=[]
	rows=[]
	if request.method =="POST":
		s_id=request.form["search"]
		csvfile=open(filename,newline='')
		data=csv.DictReader(csvfile)
		for row in data:
			if row["student_id"]==s_id:
				for key,value in row.items():
					data_send.append(value)
			else:
				flash('Looks like you have changed your name!')
		with open(filename, 'r') as csvfile: 
		    csvreader = csv.reader(csvfile) 
		    fields = next(csvreader)
		    rows.append(fields)
		    rows.append(data_send)
	rows=pd.DataFrame(rows)
	return render_template("search-student.html",data=rows.to_html(header=False,index=False))

if __name__ == "__main__": 
	app.run(debug=True)




