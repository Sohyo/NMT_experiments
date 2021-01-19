import matplotlib.pyplot as plt
import re
from os.path import isfile, join
from os import listdir


def get_loss(file_path):

    """
    This function is getting the losses from the 'slurm' file.

    :param file_path: The directory of slurm.
    :return: List of train/validation losses
    """

    train_loss = []
    valid_loss = []

    with open(file_path) as f:
        for line in f:
            # Get train loss
            if "| INFO | train |" in line:
                # Extract loss by pattern "loss x.xxxx"
                loss = re.search(r"loss \d{1,3}.\d{1,4}", line)
                # Only get the digits from the extracted loss information
                train_loss.append(re.sub(r"\Aloss\s", "", loss.group(0)))

            # Get validation loss
            elif "| INFO | valid |" in line:
                loss = re.search("loss \d{0,3}.\d{0,4}", line)
                valid_loss.append(re.sub("\Aloss\s", "", loss.group(0)))

    return train_loss, valid_loss


def get_BLEU(file_path):
    valid_BLEU = []
    with open(file_path) as f:
        for line in f:
            if "| INFO | valid |" in line:
                bleu = re.search("bleu \d{0,3}.\d{0,4}", line)
                valid_BLEU.append(re.sub("\Ableu\s", "", bleu.group(0)))

    return valid_BLEU


def plot_loss(train_loss, valid_loss, filename):
    fig = plt.figure()
    plt.title(filename)
    plt.plot(list(map(float, train_loss)), label=f'Train loss')
    plt.plot(list(map(float, valid_loss)), label=f'Validation loss')
    plt.ylabel('Loss')
    plt.xlabel('Epochs')
    plt.legend(loc='lower right')
    plt.locator_params(axis='x', nbins=10)
    # plt.show()
    plt.savefig(f"../plots/{filename}_loss.png")
    plt.close(fig)


def plot_BLEU(valid_bleu, filename):
    fig = plt.figure()
    plt.title(filename)
    plt.plot(list(map(float, valid_bleu)), label=f'Validation BLEU')
    plt.ylabel('BLEU')
    plt.xlabel('Epochs')
    plt.legend(loc='lower right')
    plt.savefig(f"../plots/{filename}_BLEU.png")
    plt.close()


def plot_loss_BLEU(train_loss, valid_loss, valid_bleu, filename):
    fig, ax1 = plt.subplots()

    color = 'navy'
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss', color=color)
    plt.plot(list(map(float, train_loss)), label=f'Train loss', color="tab:blue")
    plt.plot(list(map(float, valid_loss)), label=f'Validation loss', color="tab:orange")
    ax1.tick_params(axis='y', labelcolor=color)
    plt.title("EMEA_phrase")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'navy'
    ax2.set_ylabel('BLEU', color=color)  # we already handled the x-label with ax1
    plt.plot(list(map(float, valid_bleu)), label=f'Validation BLEU', color="tab:green")
    ax2.tick_params(axis='y', labelcolor=color)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='lower left')
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.savefig(f"../plots/all_{filename}.png")
    plt.show()
    plt.close()

def get_sorted_file_list_by_name(files_path):
    file_list = [f for f in listdir(files_path) if isfile(join(files_path, f))]
    file_list.sort()
    return file_list

def main():
    root_path = "../slurms"
    file_list = get_sorted_file_list_by_name(root_path)

    ###  To run every files at \slurms  ###

    # for file_name in file_list:
    #     train_loss, valid_loss = get_loss(file_path=join(root_path, file_name))
    #     valid_bleu = get_BLEU(file_path=join(root_path, file_name))
    #
    #     plot_loss(train_loss, valid_loss, filename=file_name)
    #     plot_BLEU(valid_bleu, filename=file_name)
    #     plot_loss_BLEU(train_loss, valid_loss, valid_bleu, filename=file_name)



    ###  To run specific file  ###


    file_name = "slurm_EMEA_p_3"
    train_loss, valid_loss = get_loss(file_path=join(root_path, file_name))
    valid_bleu = get_BLEU(file_path=join(root_path, file_name))

    plot_loss(train_loss, valid_loss, filename=file_name)
    plot_BLEU(valid_bleu, filename=file_name)
    plot_loss_BLEU(train_loss[:5], valid_loss[:5], valid_bleu[:5], filename=file_name)


if __name__ == '__main__':
    main()
