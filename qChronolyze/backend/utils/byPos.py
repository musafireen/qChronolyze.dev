def byPos(suAyPos):
  from pathlib import Path

  import json

  data = Path(__file__).parent.parent.parent / "data"
#   data = f"{base_folder}data"

  with open(f"{data}/surAyPosStrAdvWrdMD.json") as f:
    sAPSD = json.loads(f.read())

  su, Ay, Pos = suAyPos.split(":")

  wrdD = sAPSD[su][Ay][Pos]
  return wrdD

byPos("6:74:4")