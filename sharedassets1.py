#!/usr/bin/env python3

import json
import pathlib

import bs4

def main() -> None:
	with open('export/sharedassets1.assets.html') as f:
		soup = bs4.BeautifulSoup(f, 'lxml')
	table: bs4.Tag = soup.find('body').find('table').find('tbody') # type: ignore

	ids = {}
	for row in table.find_all('tr'):
		path_id, class_, name = row.find_all('td')
		if class_.text != 'MonoBehaviour' or name.text == 'MonoBehaviour':
			continue
		ids[int(path_id.text)] = name.text

	data_dir = pathlib.Path('data')
	data_dir.mkdir(exist_ok=True)
	with (data_dir / 'ids.json').open('w') as f:
		json.dump(ids, f, indent='\t')

if __name__ == '__main__':
	main()
