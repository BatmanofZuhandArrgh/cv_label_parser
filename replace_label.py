import os
import glob as glob
from tqdm import tqdm

from utils.utils import get_yaml
YAML_PATH = './config/REPLACEMENT.yaml'
REPLACE_DICT = get_yaml(YAML_PATH)

def replace_label(input_paths, output_directory = None, replacement_dict = REPLACE_DICT):
    for input_path in tqdm(input_paths):
        with open(input_path, 'r') as f:
            lines = f.readlines()
            newlines = []
            for oldline in lines:
                newline = replacement_dict[oldline[0]] + oldline[1:]
                newlines.append(newline)

        with open(input_path, 'w') as f:
            f.write(''.join(newlines))

def main():
    files = glob.glob('./sample/input/**')
    replace_label(files)


if __name__ == '__main__':
    main()