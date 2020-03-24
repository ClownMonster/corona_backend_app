from flask import Flask, request, url_for
from flask.templating import render_template
from covid import Covid

app = Flask(__name__)
app.static_folder = 'static'
covobj = Covid()
data_req_country = "india"

@app.route('/', methods=['GET', 'POST'])
@app.route('/Home', methods=['GET', 'POST'])
def index():
    counter = covobj.get_status_by_country_name(data_req_country)
    return render_template('index.html',confirmed= counter['confirmed'], active = counter['active'],
                                        Recovered = counter['recovered'], Deaths = counter['deaths'])

if __name__ == '__main__':
    app.run(debug = True)

