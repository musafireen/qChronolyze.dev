from . import byPos

def retStrObj(suAyPos):
  strL = byPos(suAyPos)["striDLs"]
  strObj = None
  if len(strL) > 0:
    if len(strL) == 1:
      strObj = strL[0]
    else:
      lemFound = False
      for strObj2 in strL:
        if strObj2["strTyp"] == "lem":
          strObj = strObj2
          lemFound = True
          break
      if not lemFound:
          strObj = strL[0]
  return strObj