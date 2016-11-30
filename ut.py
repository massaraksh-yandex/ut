#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'platform'))
from platform.utils.main import main
from platform.db.scheme import SchemeFactory

if __name__ == '__main__':
    name = 'ut'
    info = '{path} - набор утилит'
    scheme = SchemeFactory(name, None).product(fake=True)

    main(name, info, scheme)
