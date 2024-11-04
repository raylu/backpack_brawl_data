#!/usr/bin/env python3
from __future__ import annotations

import dataclasses
import json
import pathlib

def main() -> None:
	for path in pathlib.Path('export/MonoBehaviour').glob('*Recipes.json'):
		if recipes := extract_recipes(path):
			with (pathlib.Path('data') / path.name).open('w') as f:
				json.dump([dataclasses.asdict(recipe) for recipe in recipes], f, indent='\t')

def extract_recipes(path: pathlib.Path) -> list[Recipe] | None:
	with path.open() as f:
		structure = json.load(f)['m_Structure']
	if (combinations := structure.get('combinations')) is None:
		return
	
	recipes = []
	for recipe in combinations:
		inputs = [recipe['primary'], *recipe['secondaries']]
		assert all(item['m_Collection'] == 'sharedassets1.assets' for item in inputs)
		recipes.append(Recipe(
			inputs=[item['m_PathID'] for item in inputs],
			output=recipe['result']['m_PathID'],
		))
	return recipes

@dataclasses.dataclass
class Recipe:
	inputs: list[int]
	output: int

if __name__ == '__main__':
	main()
