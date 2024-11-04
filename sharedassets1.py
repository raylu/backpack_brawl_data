#!/usr/bin/env python3

import csv
import pathlib

import bs4

def main():
	with open('export/sharedassets1.assets.html') as f:
		soup = bs4.BeautifulSoup(f, 'lxml')
	table: bs4.Tag = soup.find('body').find('table').find('tbody') # type: ignore

	data_dir = pathlib.Path('data')
	data_dir.mkdir(exist_ok=True)
	with (data_dir / 'ids.csv').open('w') as f:
		writer = csv.writer(f, lineterminator='\n')
		for row in table.find_all('tr'):
			path_id, class_, name = row.find_all('td')
			if class_.text != 'MonoBehaviour' or name.text == 'MonoBehaviour':
				continue
			writer.writerow([path_id.text, name.text])

if __name__ == '__main__':
	main()
