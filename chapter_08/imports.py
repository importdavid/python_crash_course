# 8-16. Imports: pg 154
# This may look like terrible clashing,
# but I believe each import overrides appropriately

import sandwiches
sandwiches.make_sandwich('bacon', 'lettuce', 'tomato')

from sandwiches import make_sandwich
make_sandwich('bacon', 'lettuce', 'tomato')

from sandwiches import make_sandwich as ms
ms('bacon', 'lettuce', 'tomato')

import sandwiches as s
s.make_sandwich('bacon', 'lettuce', 'tomato')

from sandwiches import *
make_sandwich('bacon', 'lettuce', 'tomato')