import os
import subprocess
local_cmd_dir="./.cmd/"
cmd_dir="~/.cmd"
lof=[]
mf=[]
init_status=False

class clr:

  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  GRN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'



def ch_exist():
  if os.path.exists(local_cmd_dir + ".cmd_ign"):
    init_status=True
  if not os.path.exists(local_cmd_dir + ".cmd_ign"):
    print("First init this dir")
    print(clr.BOLD + "\"cmd init \"" + clr.ENDC)


def check(j):
  checklist=list((os.popen("cat " + local_cmd_dir + ".cmd_ign").read()).split("\n"))
  print(checklist)
  if os.path.isfile(j):
    if j in checklist:
      print("in")
    else:
      print("out")




#initialize directory
def init():
  ch_exist
  if not (os.path.exists(local_cmd_dir)):
    os.system("mkdir " + local_cmd_dir)
    os.system("echo .cmd >> " + local_cmd_dir + ".cmd_ign")
  else:
    init_status=True

def comp():

  for x in os.listdir('.'):

    if not (os.path.exists(local_cmd_dir + x)):
      lof.append(x)
    else:
      if (os.popen("diff -q " + x + " " + local_cmd_dir + x).read()):
        mf.append(x)
  if not lof and not mf:
      print("everything's ok")

  else:
      print("\n Some files were " + clr.YELLOW + "modified " + clr.ENDC +" or" + clr.RED + " don't exist " + clr.ENDC + "in distant dir \n")

  for i in lof:

    print(clr.RED + i + clr.ENDC)
  print("\n")
  for j in mf:
    print(clr.YELLOW + j + clr.ENDC)
  print("\n")



def add(fileordir):
  ch_exist()

  if fileordir==".":
    os.system("rsync -a . " + local_cmd_dir + "&")
  else:
    os.system("rsync -a " + fileordir + " " +  local_cmd_dir + "&")


#def set():
#  print("hello")




