from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'

@app.route('/whereami')
def whereami():
    return 'Ghana'

@app.route('/foo')
def foo():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
