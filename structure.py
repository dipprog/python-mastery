# structure.py

import sys

class Structure:
    _fields = tuple()
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({', '.join(repr(getattr(self, name)) for name in self._fields)})"
    
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)
