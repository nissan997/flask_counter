from flask import Flask,jsonify
from multiprocessing import Value

try:
    with open('count.txt','r') as w:
        count= int(w.read())
except:
    with open('count.txt','w') as w:
	w.write('0')
    with open('count.txt','r') as w:
        count=int(w.read())

counter = Value('i',count)

app = Flask(__name__)
@app.route('/')
def index():
	with counter.get_lock():
		counter.value +=1
		out = counter.value
		with open('count.txt', 'w') as w:
			w.write(str(out))
	return jsonify(count=out)
if __name__=="__main__":
    app.run(debug=True)
