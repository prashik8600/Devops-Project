import psutil
from flask import Flask ,render_template

app=Flask(__name__)

@app.route("/")
def index():
    CPU_percent=psutil.cpu_percent()
    Mem_percent=psutil.virtual_memory().percent
    Message=None

    if CPU_percent>80 or Mem_percent>80:
        Message=("High CPU or memory Usage Detected. Please check the resources")
    return render_template("index.html",CPU_percent=CPU_percent, Mem_percent=Mem_percent, message=Message)

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
