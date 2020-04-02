class Spell:

	def __init__(self, name: str = 'Spell', damage: int = 0, mana_cost: int = 0, cast_range: int = 0):
		self.name = name
		self.damage = damage
		self.mana_cost = mana_cost
		self.cast_range = cast_range
