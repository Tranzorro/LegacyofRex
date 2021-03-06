import json
import sqlite3

def get_room(id, dbfile):
	ret = None

	con = sqlite3.connect(dbfile)

	for row in con.execute("select json from rooms where id=?",(id,)):

		jsontext = row[0]
		d = json.loads(jsontext)
		d['id'] = id
		ret = Room(**d)
		break

	con.close()

	return ret


class Room():
	def __init__(self, id=0, name="A Room", description="An empty room", neighbors={}):
		self.id = id
		self.name = name
		self.description = description
		self.neighbors = neighbors

	def _neighbor(self, direction):
		if direction in self.neighbors:
			return self.neighbors[direction]
		else:
			return None

	def north(self):
		return self._neighbor('north')

	def east(self):
		return self._neighbor('east')

	def south(self):
		return self._neighbor('south')

	def west(self):
		return self._neighbor('west')