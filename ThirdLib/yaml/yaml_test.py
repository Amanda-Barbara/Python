import yaml
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
class Person(yaml.YAMLObject):
    yaml_tag = '!person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '%s(name=%s, age=%d)' % (self.__class__.__name__, self.name, self.age)

if __name__ == '__main__':

    # document = """
    #   a: 1
    #   b:
    #     c: 3
    #     d: 4
    # """
    # print(dump(load(document, Loader=Loader), Dumper=Dumper, default_flow_style=True))
    # print(dump({'name': 'Silenthand Olleander', 'race': 'Human', 'traits': ['ONE_HAND', 'ONE_EYE']}, Dumper=Dumper, default_flow_style=True))

    james = Person('James', 20)

    print(yaml.dump(james, default_flow_style=True))  # Python对象实例转为yaml

    lily = yaml.load('!person {name: Lily, age: 19}')

    print(lily)  # yaml转为Python对象实例


