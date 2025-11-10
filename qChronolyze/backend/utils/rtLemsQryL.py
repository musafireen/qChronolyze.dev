from . import rtLemsQry

def rtLemsQryL(rt):
  LemObjL = rtLemsQry(rt)
  LemQryL = [
    [
        {
            "strL": [strObj]
        }
    ]
    
    for strObj in rtLemsQry(rt)
  ]
  return LemQryL