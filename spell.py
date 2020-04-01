class Spell:

	def __init__(self, name: str = 'Spell', damage: float = 0, mana_cost: float = 0, cast_range: float = 0):
		self.name = name
		self.damage = damage
		self.mana_cost = mana_cost
		self.cast_range = cast_range
