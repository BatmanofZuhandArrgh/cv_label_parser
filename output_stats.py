import os
from tqdm import tqdm 
import glob as glob
import matplotlib.pyplot as plt
import numpy as np
from utils.utils import get_yaml

# LABELS = [ 
# "1U",
# "3U",
# "Other_ST",
# "Other",
# "4U",
# "2U",
# "6U",
# "12U"
# ]

LABELS = get_yaml(config_path='config/obj_cls.yaml')

def eda(folder_path, output_directory = None):
    input_paths = glob.glob(f'./{folder_path}/**/*.txt', recursive=True)

    all_labels = []
    for input_path in tqdm(input_paths):
        with open(input_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                all_labels.append(line[0])
    print(all_labels)

        # with open(input_path, 'w') as f:
        #     f.write(''.join(newlines))

  
    fig = plt.figure(figsize = (10, 5))
    
    values, count = np.unique(all_labels, return_counts=True)
    
    # creating the bar plot
    labels = [LABELS[int(x)] for x in values]
    print(values, labels)
    plt.bar(values, count, color ='blue',width = 0.4, tick_label = labels, align='center')


    plt.xlabel("Counts")
    plt.ylabel("Number of BBox")
    plt.title("NumberOfBBox per dataset")
    plt.show()

def full_eda(folder_paths, output_directory = None, folder_name = None):
    fig, axs = plt.subplots(4,  constrained_layout=True )
    # fig.suptitle('NumberOfBBox per dataset')
    # fig.tight_layout()

    for i, folder_path in enumerate(folder_paths):
        axs[i].set_title(folder_name[i])

        input_paths = glob.glob(f'{folder_path}/**/*.txt', recursive=True)

        all_labels = []
        for input_path in tqdm(input_paths):
            with open(input_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    all_labels.append(line[0])

            # with open(input_path, 'w') as f:
            #     f.write(''.join(newlines))

        values, counts = np.unique(all_labels, return_counts=True)
        print(values, counts)

        index_labels = [key for key in LABELS.keys()]
        
        label_keys = [LABELS[key] for key in index_labels]
        label_counts = []
        for index in index_labels:
            if index not in values:
                label_counts.append(0)
            else:
                label_counts.append(counts[list(values).index(index)])
        

        axs[i].bar(label_keys, label_counts, color ='teal',width = 0.4, tick_label = label_keys, align='center')
        if i != 3:
            axs[i].set_xticks([])

    # Set common labels
    # fig.text(0.5, 0.04, 'Counts', ha='center', va='center')
    # fig.text(0.01, 0.5, 'Number of BBoxes', ha='center', va='center', rotation='vertical')

    plt.show()
    fig.savefig(f'{output_directory}/common_labels_text.png', dpi=300) #, pad_inches = 1, bbox_inches = 1)


def main():
    folder_paths = [
        '/home/anhnguyen/Downloads/labelled_dataset/final_agency_testset/agencies_trainset',
        '/home/anhnguyen/Downloads/labelled_dataset/final_agency_testset/agencies_testset',
        '/home/anhnguyen/Downloads/labelled_dataset/deployment_testset',
        '/home/anhnguyen/Downloads/labelled_dataset/far_testset',
    ]
    full_eda(
        folder_paths=folder_paths, 
        output_directory='./sample/output/analysis',
        folder_name= ['agencies_trainset', 'agencies_testset', 'deployment_testset', 'far_testset']
        )

if __name__ == '__main__':
    main()