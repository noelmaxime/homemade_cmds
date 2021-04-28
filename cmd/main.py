import os
from funcs import *
cmd_line = list((os.environ['cmd_line']).split(" "))
val_args=["status" , "rm" , "push" , "def" , "init", "add"]
param=cmd_line[0]
args=cmd_line[1:-1]


if param not in val_args:

  print(param + " is not a valid argument." + "\n" + "Type 'cmd --help' for help")

else:

  if param=="add":
    fileordir = cmd_line[(cmd_line.index("add")+1)]
    add(fileordir)

  if param=="status":
    comp()

  if param=="init":
    init()
