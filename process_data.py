import json, os
import argparse

def process_extras(file_path, platform):
    extraFile = os.path.join(
        os.path.dirname(__file__),
        'extras',
        os.path.basename(
            file_path
                .replace('.json', '.txt')
                .replace('CodegenData', platform)
        )
    )

    extras = []
    if os.path.exists(extraFile):
        with open(extraFile, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                if '-' not in line: continue
                func_name, hex_addr = line.split('-', 1)
                func_name = func_name.strip()
                hex_addr = hex_addr.strip()
                try:
                    addr = int(hex_addr, 16)
                    if any(b[0] == addr for b in extras): continue
                    extras.append((addr, func_name))
                except ValueError:
                    continue

    return extras

def main(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    win = []
    m1 = []
    imac = []
    ios = []

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
            if 'ios' in bindings and isinstance(bindings['ios'], int):
                if any(b[0] == bindings['ios'] for b in ios): continue
                imac.append((bindings['ios'], func_name))

    win.extend(process_extras(input_file, 'Win64'))
    m1.extend(process_extras(input_file, 'Arm'))
    imac.extend(process_extras(input_file, 'Intel'))
    ios.extend(process_extras(input_file, 'iOS'))
    win = list(dict.fromkeys(win))
    m1 = list(dict.fromkeys(m1))
    imac = list(dict.fromkeys(imac))
    ios = list(dict.fromkeys(ios))

    win.sort(key=lambda x: x[0])
    m1.sort(key=lambda x: x[0])
    imac.sort(key=lambda x: x[0])
    ios.sort(key=lambda x: x[0])

    base_filename = input_file.replace('.json', '')

    with open(f"{base_filename}-Win64.json", 'w') as f:
        json.dump(win, f)

    with open(f"{base_filename}-Arm.json", 'w') as f:
        json.dump(m1, f)

    with open(f"{base_filename}-Intel.json", 'w') as f:
        json.dump(imac, f)

    with open(f"{base_filename}-iOS.json", 'w') as f:
        json.dump(imac, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True, help="Path to the input JSON file")
    args = parser.parse_args()
    main(args.input_file)