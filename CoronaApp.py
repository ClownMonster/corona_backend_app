from flask import Flask
from flask.templating import render_template
from covid import Covid

app = Flask(__name__)
app.static_folder = 'static'
covobj = Covid()


@app.route('/')
@app.route('/Home')
def index():
    counter = covobj.get_status_by_country_name('italy')
    return render_template('index.html',confirmed= counter['confirmed'], active = counter['active'],
                                        Recovered = counter['recovered'], Deaths = counter['deaths'])




if __name__ == '__main__':
    app.run(debug = True)

