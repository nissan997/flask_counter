from flask import Flask,jsonify
from multiprocessing import Value
with open('count.txt','r') as w:
	prev_count= w.read()
	count = int(prev_count)
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