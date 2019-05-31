import os


def create_dir(name, address):
    foulderpath = os.path.join(address, name)
    if not os.path.exists(foulderpath):
        os.makedirs(foulderpath)


def create_file(name, address):
    filepath = os .path.join(address, name)
    if not os.path.exists(address):
        os.makedirs(address)
    open(filepath, "a")


def delete(name, address):
    filepath = os.path.join(address, name)
    if os.path.exists(filepath):
        os.remove(filepath)


def find(name, address):
        result = []
        for root, dirs, files in os.walk(address):
            if name in files:
                result.append(os.path.join(root, name))
        return result


