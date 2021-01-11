from os import listdir, rename
from os.path import isfile, join
import argparse
import re


def parse_arguments():
    parser = argparse.ArgumentParser(description='In the directory, change the name of slurms as job names.')
    parser.add_argument('--data_name', type=str,  default='EMEA',
                        help='The name of the datasets that want to change slurms to different name.')
    parser.add_argument('--orig', default=False, action='store_true',
                        help='The dataset is not phrases.')

    args = parser.parse_args()
    return args.data_name, args.orig


def get_all_slurms(files_path):
    file_list = [f for f in listdir(files_path) if isfile(join(files_path, f)) and f.startswith('slurm-')]
    # Sort the file names: This is because want to only save the latest file for every job scripts.
    file_list.sort(key=lambda f: float(re.sub("\D", "", f)))
    return file_list


def change_names(file_path):
    with open(file_path) as f:
        for line in f:
            # In the slurm file, need to find line where 'job name' is.
            if line.startswith('Name                : '):
                new_name = line.split()[-1]
            # elif line.startswith('End                 :'):
            #     date = line.split([-1])

    rename(file_path, f'../slurms/slurm_{new_name}')


def main():
    name, is_original_dataset = parse_arguments()
    data_type = 'orig' if is_original_dataset else 'phrase'
    path = f'../peregrine_jobscripts/jobscript_{name}_{data_type}'
    list_slurms = get_all_slurms(path)

    for slurm in list_slurms:
        change_names(join(path, slurm))


if __name__ == '__main__':
    main()
