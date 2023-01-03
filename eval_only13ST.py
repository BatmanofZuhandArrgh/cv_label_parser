import os
import glob as glob
import pandas as pd

def output_eval(
    input_paths,
    output_dir = './sample/input/eval', 
    match_output =[ 'one', 'three', 'space_target']
    ):
    for input_path in input_paths:
        df = pd.read_csv(input_path, sep='\t')
        output_filename = os.path.basename(input_path)
        for prioritized_cls in match_output:
            
        print(df)


def main():
    input_paths = ['./sample/input/eval/mAP_evaluation.csv']
    output_eval(input_paths=input_paths) 
if __name__ == '__main__':
    main()
