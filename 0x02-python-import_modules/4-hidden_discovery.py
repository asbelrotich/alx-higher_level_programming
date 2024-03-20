#!/usr/bin/python3
import importlib.util


def name_of_module(name_m):
    spec = importlib.util.spec_from_file_location(name_m, f"{name_m}.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = [name for name in dir(module) if not name.startswith("__")]
    names.sort()
    for name in names:
        print(name)


if __name__ == "__main__":
    name_of_module("hidden_4")
