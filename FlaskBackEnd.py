import flask
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nooky.com</title>
    <style>
        img {
        width: 300px;
        }

        a{
        font-weight: bold;
        color: pink;
        font-size: 30px;
        font-family: "Lucida Console", "Courier New", monospace;



      body {
        background: #156;
        color: green;


      iframe {

        width: 50px;






    </style>
</head>
<body>
<IMG SRC="images/HIYA.JPEG">
<a> Man o man What a sunset! Bask in the beauty with John Pork</a>


<IMG SRC="images/john-pork-just-imagine.gif">

<iframe width="420" height="315"
        src="https://www.youtube.com/embed/VAiHHUMUp-4">
</iframe>



</body>
</html>"""

if __name__  == "__main__":
    app.run(debug=True)

