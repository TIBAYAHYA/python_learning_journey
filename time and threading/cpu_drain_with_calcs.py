"""funny program that can drain your computer's cpu and eventually shut It off
"""
# are you confident on your computer's cpu? or just to drain your computer cpu for reasons I shouldnt know, insert a very big number on the input
#and patiently wait for the bomb to tick
bomb = input("insert the bomb value\n")
import subprocess,threading

def open_calculator():
    calculator_popen = subprocess.Popen(r"C:\Windows\System32\calc.exe")
    calculator_popen.wait()

for x in range(bomb):
    threadin_obj = threading.Thread(target=open_calculator)
    threadin_obj.start()