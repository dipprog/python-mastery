# structure.py

class Structure:
    _fields = tuple()

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(repr(getattr(self, name)) for name in self._fields)})"
    
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)

    @classmethod
    def create_init(cls):
        argstr = ', '.join(cls._fields)
        init_code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            init_code += f'    self.{name} = {name}\n'
        locs = { }
        exec(init_code, locs)
        cls.__init__ = locs['__init__']
