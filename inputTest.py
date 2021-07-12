from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
	return 'welcome %s' % name

@app.route('/testform',methods = ['POST', 'GET'])
def test(): 
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('hello',name = user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('hello',name = user))

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080)