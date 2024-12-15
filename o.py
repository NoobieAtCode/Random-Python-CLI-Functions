import time,math,random,shutil,sys, os
wait = time.sleep
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
#_---------------------------------------
#Modules 
#_--------------------------------------- 
def loadbar(barlength:int=20, pause1:int=0.1, pauselong:int=0.1,finalwait:int=5,color:str="white",loading_text:str = "Loading",load_finish:str="Done   ",end_cls:bool=False,endl:bool=False):
  from termcolor import colored
  #{"black": "\u001b[30m","red": "\u001b[31m","green": "\u001b[32m", "yellow": "\u001b[33m", "blue": "\u001b[34m","magenta": "\u001b[35m","cyan": "\u001b[36m"}#
  import time
  wait = time.sleep
  loadedbar = "▓";unloadedbar = "░"
  loading = colored(f"{loading_text}", 'white')
  defaultunloadedfullbar = unloadedbar * (barlength - 1)
  for i in range(0, barlength, 1):
    defaultunloadedbar = loadedbar * i + defaultunloadedfullbar[i:barlength - 1]  
    if i == barlength / 2:
      wait(pauselong)
    elif i == barlength-1:
      print(load_finish, colored(defaultunloadedbar,color))
      #print(f"Loaded: {colored(lbar,color)}\n")
      wait(finalwait)
      clear() if end_cls else wait(0.001)
      print("\n") if endl else wait(0.001)
      return ""
    elif i != barlength:
      wait(pause1)
      defaultunloadedbar = colored(defaultunloadedbar, color)
      print(f"{loading} {defaultunloadedbar}", flush=True, end="\r")


def tywr(i:str = "Placeholder",s:int = 20,enable_sys: bool=False):
  if enable_sys:
    sys_print = sys.stdout.write
    for x in i:
      if x == "  ":
        wait(0.0000001/s)
      wait(1/s)
      sys_print(x)
      sys.stdout.flush()
  elif not enable_sys:
    for x in i:
      if x == "  ":
        continue
      wait(1/s)
      print(x,flush=True,end="")
    
  return ""

tywr(enable_sys=True)

def qformula(a, b, c, r):
  p = None
  if a == 0:
    return "'a' cannot be 0"
  d = b**2 - 4*a*c
  if d < 0:
    return "No real solutions exist"
  y = math.sqrt(d)
  x1 = (-b + y) / (2*a)
  x2 = (-b - y) / (2*a)
  
  return int(x1) if r == 1 else p == 0
  return int(x2) if r == 2 else p == 0



#variable modules
r50 = random.randint(1,2)

def timeis(format,tz,hrtype):
  import datetime, pytz
  dt = datetime.datetime
  now=dt.now(pytz.timezone(tz))
  if format.lower() == "normal":
    return now()
  if format.lower() == "data":
    d = {"year": now.year,"month":now.month,"day":now.day,"hour":now.hour,"minute":now.minute,"second":now.second,"milisecond":now.microsecond}
    if int(hrtype) == 12:
      t = now.hour;l="";ap=""
      l = f"{int(t)-12}";ap="pm"
      if int(t)-12>0:
        l = f"{int(t)-12}";ap="pm"  
      if int(t)-12 < 0:
        l = t;ap="am"
      d["hour"] = l
      d['am/pm'] = ap 
  return d

def gcd(x,y):
  r = min(x, y)
  while r:
    if x % r == 0 and y % r == 0:
      break
    r -= 1
  return r
  
def lcm(x,y):
  mn = min(x,y)
  mx = max(x,y)
  while True:
    if mx % mn == 0:
      break
    mx += mx
  return mx



def center(text):
    terminal_width = shutil.get_terminal_size().columns
    return text.center(terminal_width)

def listtostr(lists):
  str_list = ''.join(map(str, lists))
  return str_list
