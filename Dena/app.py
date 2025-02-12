from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/informasi_kesehatan')
def informasi_kesehatan():
    return render_template('informasi_kesehatan.html')

@app.route('/berita')
def berita():
    return render_template('berita.html')

if __name__ == '__main__':
    app.run(debug=True)