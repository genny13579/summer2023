from curses import window
#from turtle import onclick
from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def top_blurb():
   text = ""
   #maybe make it a dropdown or other feature VVV
   text += """
   <script>function clickfunction(){
      projTitle = window.prompt("what project are you working on") 
      window.alert (projTitle)
      }</script>
      """
   #n = int(request.args.get("num"))
   #word = request.args.get("word")
   #for i in range(n):
   #   text += f'<h1 style=color:#75dae6;font-size:80px;background-color:#4d4d4d;text-align:center>{word}</h1>'
   #
   text += '<h1 style=color:#75dae6;font-size:80px;background-color:#4d4d4d;text-align:center>Welcome</h1>'
   text += '<p style=color:#098491;font-size:30px>Info about this thing goes here :)</p>'
   text += '<h2>log your work time!</h2>'
   text += f'<button onclick=clickfunction()>log time here</button>'
   return text

#def button():

if __name__ == '__main__':
   app.run(port = 5001)
