from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, template_folder="templates")
API_URL = "http://127.0.0.1:5000/kohvikud"

@app.route('/')
def index():
    response = requests.get(API_URL)
    kohvikud = response.json() if response.status_code == 200 else []
    return render_template('index.html', kohvikud=kohvikud)


@app.route('/filter', methods=['POST'])
def filter_kohvikud():
    open_time = request.form.get('open_time')
    close_time = request.form.get('close_time')

    if not open_time or not close_time:
        return redirect(url_for('index'))

    response = requests.get(f"{API_URL}/avamisaeg?start={open_time}&end={close_time}")
    kohvikud = response.json() if response.status_code == 200 else []

    return render_template('index.html', kohvikud=kohvikud)

@app.route('/add', methods=['POST'])
def add_kohvik():
    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "provider": request.form['provider'],
        "time_open": request.form['time_open'],
        "time_closed": request.form['time_closed']
    }
    requests.post(API_URL, json=data)
    return redirect(url_for('index'))

@app.route('/update/<int:cafe_id>', methods=['POST'])
def update_kohvik(cafe_id):
    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "provider": request.form['provider'],
        "time_open": request.form['time_open'],
        "time_closed": request.form['time_closed']
    }
    requests.put(f"{API_URL}/{cafe_id}", json=data)
    return redirect(url_for('index'))

@app.route('/delete/<int:cafe_id>', methods=['POST'])
def delete_kohvik(cafe_id):
    requests.delete(f"{API_URL}/{cafe_id}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
