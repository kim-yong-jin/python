from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World'

@app.route('/test')
def test():
    return render_template('post.html')

@app.route('/post',methods=['POST'])
def post():
    value =request.form['test']
    print("value : ",value)
    return render_template('default.html',mytitle=value,mylist=[x+1 for x in range(20)])


if __name__ == "__main__" :
    app.run(host="127.0.0.1",port="9999")