from flask import *
from myspider.main import *
from myspider.myspider.Global import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get', methods=['POST'])
def get():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        Glovar.stuid = username
        # Here makes file to download
        # runScrapy(username, password)
        dictionary = os.getcwd() + '\download'
        return send_from_directory(dictionary, username + '.docx')
    else:
        return redirect(url_for(''))


if __name__ == '__main__':
    app.debug = True
    app.run()
