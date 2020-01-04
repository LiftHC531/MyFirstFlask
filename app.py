from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = "Flask web App"
    #return "<h1>Hello, world</h1><p>Flask is amazing</p>"
    return render_template('index.html', title=title)

if __name__ == '__main__':
    #app.run(port=3000)
    app.run()
