from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def redirect():
    return "go to /health route"


@app.route('/health')
def health():
    ok_response = str(200)
    return '{"status: "' + ok_response + '"}'


if __name__ == '__main__':
    app.run(debug=True)
