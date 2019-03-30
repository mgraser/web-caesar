from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height:120px;
                }

            </style>
        </head>
        <body>
            <form action="/" method="post">
                <label for="rot">Rotate by: </label>
                <input type="text" name="rot" id="rot" value="0">
                <textarea id="text" name="text" rows="4" cols="50"></textarea>
                <input type="submit" value="Submit Query" />

        </body>
    </html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot_element = int(request.form['rot'])
    text_element = request.form['text']

    encrypted_message = rotate_string(text_element, rot_element)
    encrypted_message_return = "<h1>" + encrypted_message + "</h1>"
    return encrypted_message_return


@app.route("/")
def index():
    return form


app.run()