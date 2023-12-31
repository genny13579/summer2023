from curses import window
import time
#from turtle import onclick
from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def homePage():
   #top: its pretty
   text = ""
   text += '<h1 style=color:#75dae6;font-size:80px;background-color:#4d4d4d;text-align:center>Welcome</h1>'
   text += '<p style=color:#098491;font-size:30px>Info about this thing goes here :)</p>'
   text += '<h2>log your work time!</h2>'
   #this is the form, gets some data
   text += """<form method=POST action=/log> 
   <br>
   Project name: <input name=projName> 
   <br>
   Status: <select name=action>
   <option value=Start> Start
   <option value=Break> Break
   <option value=Stop> Stop
   <option value=Update> Update
   </select>
   <br>
   Progress: <input name=projPercentProgress> 
   <br>
   Comment: <input name=comment> 
   <br>
   <input type=submit>
   </form>
   """
   #the form is over now

   #lets print the data!
   with open('log.txt', 'r') as f:
      workTimeTotal = 0
      contents = f.read()
      text += f'<pre>{contents} </pre>'
      lines = contents.split('\n')
      for line in lines:
         if line == '':
            continue
         dataVals = line.split(';;')
         if dataVals[1] == 'Start':
            #record most recent start of work
            begun = float(dataVals[4])
            currPercent = int(dataVals[2])
         if dataVals[1] == 'Break':
            #stop adding time
            pause = float(dataVals[4])
            timeDiff = (pause - begun) 
            workTimeTotal += timeDiff
            currPercent = int(dataVals[2])
         if dataVals[1] == 'Stop':
            #stop adding time
            endTemp = float(dataVals[4])
            timeDiff = (endTemp - begun) 
            workTimeTotal += timeDiff
            currPercent = int(dataVals[2])
         if dataVals[1] == 'Update':
            currPercent = int(dataVals[2])
      workTimeProjected = workTimeTotal/(currPercent/100)
      workTimeLeft = workTimeProjected - workTimeTotal


      text += f'Work time so far in hours: {(workTimeTotal/3600):.2f}'
      text += f'<br>Total hours to complete full project: {(workTimeProjected/3600):.2f}<br>Hours left till completion: {(workTimeLeft/3600):.2f}'


   return text

@app.route('/log', methods=['POST'])
def log():
   project=request.form.get('projName', default='unkown', type=str)
   status=request.form.get('action', default='unkown', type=str)
   progress=request.form.get('projPercentProgress', default=-1, type=int)
   comment=request.form.get('comment', default='', type=str)
   currTime=time.time()

   with open('log.txt', 'a') as f:
      f.write(f'{project};;{status};;{progress};;{comment};;{currTime}\n')

   return f'logged: <br>proj: {project}, stat: {status}, prog: {progress}, comm: {comment}, time: {currTime}'

#maybe make it a dropdown or other feature VVV
   #
   #text += """
   #<script> function clickfunction(){
   #   projTitle = window.prompt("what project are you working on") 
   #   window.alert (projTitle)
   #   }</script>
   #   """
   #n = int(request.args.get("num"))
   #word = request.args.get("word")
   #for i in range(n):
   #   text += f'<h1 style=color:#75dae6;font-size:80px;background-color:#4d4d4d;text-align:center>{word}</h1>'
   #
   #text += f'<button onclick=clickfunction()>log time here</button>'
if __name__ == '__main__':
   app.run(port = 5001)
