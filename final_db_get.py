import json
import pickledb

db = pickledb.load('youtube.db', False) 

print db.dgetall("2")