#Michael Ruvinshteyn
#SoftDev1 pd7
#HW 04 -- Fill Up Yer Flask
#2017 - 9 - 21

import random
from flask import Flask
app = Flask(__name__)

html = '''<h1>Behind one of these doors is a functional set of python code. Behind the other two are actual pythons. (randomized)</h1>

          <p><a href = "\d1">Door 1</a></p><br>
          <p><a href = "\d2">Door 2</a></p><br>
          <p><a href = "\d3">Door 3</a></p><br>
'''

@app.route("/")
def hello_world():
    return html

#each door runs the same code block, but each door has the same chances for the same outcomes, giving an average result as specified in the main page
@app.route("/d1")
def d1():
    if random.randint(0,2) == 0:
        return '''You get to pass SoftDev! <br><br>
                  <img src = http://www.discoveryplayground.com/files/8413/0446/4704/python-shell-3-2-hello-world.png width=660 height=371><br><br>
                  <a href="\..">Go back</a>'''
    else:
        return '''How are those hospital bills looking?<br><br>
                  <img src=https://ichef.bbci.co.uk/news/660/cpsprodpb/070C/production/_95940810_gettyimages-98396986.jpg><br><br>
                  <a href="\..">Go back</a>'''

@app.route("/d2")
def d2():
    if random.randint(0,2) == 0:
        return '''You get to pass SoftDev! <br><br>
                  <img src = http://www.discoveryplayground.com/files/8413/0446/4704/python-shell-3-2-hello-world.png width=660 height=371><br><br>
                  <a href="\..">Go back</a>'''
    else:
        return '''How are those hospital bills looking?<br><br>
                  <img src=https://ichef.bbci.co.uk/news/660/cpsprodpb/070C/production/_95940810_gettyimages-98396986.jpg><br><br>
                  <a href="\..">Go back</a>'''

@app.route("/d3")
def d3():
    if random.randint(0,2) == 0:
        return '''You get to pass SoftDev! <br><br>
                  <img src = http://www.discoveryplayground.com/files/8413/0446/4704/python-shell-3-2-hello-world.png width=660 height=371><br><br>
                  <a href="\..">Go back</a>'''
    else:
        return '''How are those hospital bills looking?<br><br>
                  <img src=https://ichef.bbci.co.uk/news/660/cpsprodpb/070C/production/_95940810_gettyimages-98396986.jpg><br><br>
                  <a href="\..">Go back</a>'''

if __name__ == "__main__":
    app.debug = True
    app.run()
