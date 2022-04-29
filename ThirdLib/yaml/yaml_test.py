from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


if __name__ == '__main__':
    stream = file('document.yaml', 'w')

    document = """
      a: 1
      b:
        c: 3
        d: 4
    """
    print(dump(load(document, Loader=Loader), Dumper=Dumper, default_flow_style=True))
    print(dump({'name': 'Silenthand Olleander', 'race': 'Human', 'traits': ['ONE_HAND', 'ONE_EYE']}, Dumper=Dumper, default_flow_style=True))


