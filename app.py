from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def dashboard():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    battery = psutil.sensors_battery()

    return render_template('dashboard.html', cpu=cpu, memory=memory, disk=disk, battery=battery)

if __name__ == '__main__':
    app.run(debug=True)
