from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('portfolio.html', name = 'Vicky Kumar')

if __name__ == '__main__':
    app.run(debug=True)
