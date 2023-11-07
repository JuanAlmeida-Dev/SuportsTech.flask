from flask import Flask

app = Flask(__name__)
app.secret_key = b'52fb96da04fe19cb18b8a5831459be41c7dabf7dd3253e2b7609032579'

from controllers import *

if __name__ == '__main__':
    app.run(debug=True)
