### Hexlet tests and linter status:
[![Actions Status](https://github.com/ilnarkz/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/ilnarkz/python-project-lvl2/actions)

<a href="https://codeclimate.com/github/ilnarkz/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/5f67c29840ad19e57a09/maintainability" /></a>

[![hexlet-check](https://github.com/ilnarkz/python-project-lvl2/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ilnarkz/python-project-lvl2/actions/workflows/hexlet-check.yml)

<a href="https://codeclimate.com/github/ilnarkz/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/5f67c29840ad19e57a09/test_coverage" /></a>

Пакет "Вычислитель различий" позволяет вычислять разницу между двумя файлами. 
Вычислитель различий может принимать файлы в форматах: '.json', '.yml' и '.yaml'. 
Вывод производится в форматтерах:
1. stylish (словарь)
2. plain (текстовый формат)
3. json (.json файл)

Для использования пакета необходима версия:

python ^3.8
pip ^21.3 Для установки пакета используйте команду: python3 -m pip install git+https://github.com/ilnarkz/python-project-lvl2.git Для запуска игры используйте команду: poetry run brain-even

Пример работы вычислителя различий для простых JSON-файлов:

[![asciicast](https://asciinema.org/a/x9vC9yWSOPMNaQgBmi1eCLspq.svg)](https://asciinema.org/a/x9vC9yWSOPMNaQgBmi1eCLspq)

Пример работы вычислителя различий для простых YAML-файлов:

[![asciicast](https://asciinema.org/a/JvwHMPbaOg0oqAg83rENcYia7.svg)](https://asciinema.org/a/JvwHMPbaOg0oqAg83rENcYia7)

Пример работы вычислителя различий для вложенных JSON-файлов и YAML-файлов(форматтер stylish):

[![asciicast](https://asciinema.org/a/jbTbcS3y1Wo7mVpWkAtchIxDd.svg)](https://asciinema.org/a/jbTbcS3y1Wo7mVpWkAtchIxDd)

Пример работы вычислителя различий для вложенных JSON-файлов и YAML-файлов(форматтер plain):

[![asciicast](https://asciinema.org/a/TPGg4D898Q4S4HafkTl8g4rIJ.svg)](https://asciinema.org/a/TPGg4D898Q4S4HafkTl8g4rIJ)

Пример работы вычислителя различий для вложенных JSON-файлов и YAML-файлов(форматтер json):

[![asciicast](https://asciinema.org/a/V4AsE8WmwNsnhFlgcyyw8xlF9.svg)](https://asciinema.org/a/V4AsE8WmwNsnhFlgcyyw8xlF9)
