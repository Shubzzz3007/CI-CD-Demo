from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, CI/CD World! , Making Some changes'

if __name__ == '__main__':
    app.run(debug=True)
