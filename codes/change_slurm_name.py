from os import listdir, rename
from os.path import isfile, join, getsize
import argparse
import re


def parse_arguments():
    parser = argparse.ArgumentParser(description='In the directory, change the name of slurms as job names.')
    parser.add_argument('--data_name', type=str, nargs='+', default=['EMEA'],
                        help='The name of the datasets that want to change slurms to different name.')
    parser.add_argument('--phrase', default=True, action='store_false',
                        help='The dataset is extracted phrase version.')

    args = parser.parse_args()
    return args.data_name, args.phrase


def get_all_slurms(files_path):
    file_list = [f for f in listdir(files_path) if isfile(join(files_path, f)) and f.startswith('slurm-')]
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
    rename(file_path, f'../slrums/slurm_{new_name}')

if __name__ == '__main__':

    name, phrase = parse_arguments()
    if phrase:
        data_type = 'phrase'
    else:
        data_type = 'orig'
    path = f'../peregrine_jobscripts/jobscript_{name[0]}_{data_type}'
    list_slurms = get_all_slurms(path)
    print(list_slurms)
    for slurm in list_slurms:
        change_names(join(path, slurm))
