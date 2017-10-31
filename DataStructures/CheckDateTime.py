#!/usr/bin/python3.6

import dateutil.parser as date_parser


dtTm1 = date_parser.parse('2017-10-31 17:34:56.123456')
dtTm2 = date_parser.parse('2017-10-31 18:35:57.223457')
dtTm3 = date_parser.parse('2017-10-31 10:35:57.223457')

delta = dtTm2 - dtTm1
print(delta.total_seconds())
print(type(dtTm2))
print(type(delta.total_seconds()))
print(type(dtTm2 - dtTm1))
print((dtTm2 - dtTm3).total_seconds())
