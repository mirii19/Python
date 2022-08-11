from tkinter import Variable
import os
Variable= int(os.environ['entorno'])
print(Variable)

os.environ ['entorno']='1'
variable= int(os.environ['entorno'])
print(variable)
