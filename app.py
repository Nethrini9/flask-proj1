from flask import *
from  empdata import  Emp
from  hrdata import  HR

app=Flask(__name__)

e = []
h=[]

@app.route('/')

@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/getempdata')
@app.route('/readempdatata',methods = ['POST', 'GET'])
def readempdatata():
def getem():
	return render_template('getemp.html')

@app.route('/emplogin')
def emplogin():
	return render_template('emplogin.html')

	ename = request.form['ename']
	mobile = request.form['mobile']
	psd = request.form['psd']
	e.append(Emp(ename,mobile,psd))
	return  redirect(url_for('home'))

@app.route('/Checkemplogin', methods=['POST', 'GET'])
def Checkemplogin():
	ename1 = request.form['ename']
	psd1 = request.form['psd']

	for i in e:

		if i.ename==ename1 and i.psd==psd1:
			#return "Found "
			#return render_template("leave.html", en=ename1,p=psd1)
			return render_template("leave.html")

		else:
			return "Not found "



		#return "in Emp log in "+str(ename1)+str(psd1)

@app.route('/empleave', methods=['POST', 'GET'])
def empleave():
		email1 = request.form['email']
		msg1 = request.form['cmc1']
		#return render_template("result.html", result=result)
		# return redirect(url_for('home'))
		h.append(HR(email1,msg1))

		return "Leave Granted "



		'''
   		if request.method == 'POST':
      	result = request.form
      	return render_template("result.html",result = result)
    	'''



@app.route('/showemp')
def showemp():
	return render_template("show.html", e=e)
	#return "this is emp show"

if __name__=="__main__":
	app.run(debug=True)
