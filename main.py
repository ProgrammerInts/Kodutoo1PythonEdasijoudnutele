import subprocess
import time

print("Käivitan db_setub.py")
subprocess.run(["python", "db_setup.py"])

print("Käivitan API")
api_process = subprocess.Popen(["python", "api.py"])

time.sleep(2)

print("Käivitan veebilehe")
web_process = subprocess.Popen(["python", "app.py"])

try:
    api_process.wait()
    web_process.wait()
except KeyboardInterrupt:
    print("Sulgen jooksvad programmid")
    api_process.terminate()
    web_process.terminate()