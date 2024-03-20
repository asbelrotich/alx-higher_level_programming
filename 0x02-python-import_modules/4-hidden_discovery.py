#!/usr/bin/python3
import importlib.util

def name_of_module(module_name):
    spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    names = [name for name in dir(module) if not name.startswith("__")]
    names.sort()
    
    for name in names:
        print(name)

if __name__ == "__main__":
    print_names_of_module("hidden_4")
