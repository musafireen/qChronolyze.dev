def rtLemsQry(rt):
  import json
  from pathlib import Path
  data = Path(__file__).parent.parent.parent / "data"
#   data = f"qChronolyze/data"
  # data = f"{base_folder}data"
  with open(f"{data}/rtToLem.json") as f:
    rtToLem = json.loads(f.read())
  lemQryL = rtToLem[rt]
  return lemQryL