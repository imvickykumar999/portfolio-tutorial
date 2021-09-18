from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():

    vid = request.args.get('vid')

    return render_template('portfolio.html',
                           name = 'Vicky Kumar',
                           vid = vid,
                           )

if __name__ == '__main__':
    app.run(debug=True)
