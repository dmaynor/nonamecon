#!/usr/bin/env python

import investigate
import json

api_key="KEY"

inv = investigate.Investigate(api_key)

res = inv.categorization('amazon.com')
print res


