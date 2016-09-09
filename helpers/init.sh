#!/usr/bin/env bash

mysql -e 'DROP DATABASE aquari;'
mysql -e 'CREATE DATABASE aquari DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;'
python3 ../manage.py migrate
python3 ../manage.py shell < data-population.py
