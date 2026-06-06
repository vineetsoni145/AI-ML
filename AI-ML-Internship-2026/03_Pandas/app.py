from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':

        loyalty = request.form.get('loyalty')
        gender = request.form.get('gender')
        cusdata = pd.read_csv('customers.csv')
        data = cusdata[(cusdata['loyalty_tier'] == loyalty) &(cusdata['gender'] == gender)]
        l = len(data)
        return render_template('index.html', loyalty=l)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)