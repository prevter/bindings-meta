import json, os
import argparse

def main(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    win = []
    m1 = []
    imac = []

    for cls in data['classes']:
        name = cls['name']
        for func in cls['functions']:
            func_name = f"{name}::{func['name']}"
            bindings = func.get('bindings', {})
            if 'win' in bindings and isinstance(bindings['win'], int):
                if any(b[0] == bindings['win'] for b in win): continue
                win.append((bindings['win'], func_name))
            if 'm1' in bindings and isinstance(bindings['m1'], int):
                if any(b[0] == bindings['m1'] for b in m1): continue
                m1.append((bindings['m1'], func_name))
            if 'imac' in bindings and isinstance(bindings['imac'], int):
                if any(b[0] == bindings['imac'] for b in imac): continue
                imac.append((bindings['imac'], func_name))

    win.sort(key=lambda x: x[0])
    m1.sort(key=lambda x: x[0])
    imac.sort(key=lambda x: x[0])

    base_filename = input_file.replace('.json', '')

    with open(f"{base_filename}-Win64.json", 'w') as f:
        json.dump(win, f)

    with open(f"{base_filename}-Arm.json", 'w') as f:
        json.dump(m1, f)

    with open(f"{base_filename}-Intel.json", 'w') as f:
        json.dump(imac, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True, help="Path to the input JSON file")
    args = parser.parse_args()
    main(args.input_file)