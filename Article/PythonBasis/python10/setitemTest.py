
class SchemaDict(dict):
    def __init__(self, **kwargs):
        super(SchemaDict, self).__init__()
        self.schema = {}
        self.strict = False
        self.doc = ""
        self.update(kwargs)

    def __setitem__(self, key, value):
        # XXX also update regular dict to SchemaDict??
        if isinstance(value, dict) and key in self and isinstance(self[key],
                                                                  SchemaDict):
            self[key].update(value)
        else:
            super(SchemaDict, self).__setitem__(key, value)

    def __missing__(self, key):
        if self.has_default(key):
            return self.schema[key].default
        elif key in self.schema:
            return self.schema[key]
        else:
            raise KeyError(key)

if __name__ == '__main__':
    sd = SchemaDict()
    sd['name'] = 'zjw'
    sd['age']  = 18
    sd['sex']  = 'man'
    print(sd['name'])
    print(sd['age'])
    print(sd['sex'])
    print(sd['id'])
