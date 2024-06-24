from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    message = request.form['message']
    messages.append(message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
