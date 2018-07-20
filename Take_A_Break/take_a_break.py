import webbrowser
import time

print("The reminder script started on " + time.ctime())
for i in range(3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=jaRsJvZgg2s")
