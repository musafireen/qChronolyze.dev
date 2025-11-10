from . import retStrObj

def qryObj(suAyPos):
  strObj = retStrObj(suAyPos)
  qryKeys = ["stri","strTyp"] if strObj["strTyp"] == "lem" else ["stri","strObj","frm","poSp"]
  qryObj = {key:strObj[key] for key in qryKeys}
  return qryObj