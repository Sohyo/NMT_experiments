import matplotlib.pyplot as plt
import re


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
                loss = re.search(r"loss \d{1,3}.\d{1,4}", line)
                valid_loss.append(re.sub(r"\Aloss\s", "", loss.group(0)))

    return train_loss, valid_loss


def get_BLEU(file_path):
    valid_BLEU = []
    with open(file_path) as f:
        for line in f:
            if "| INFO | valid |" in line:
                bleu = re.search(r"bleu \d{1,3}.\d{1,4}", line)
                valid_BLEU.append(re.sub(r"\Ableu\s", "", bleu.group(0)))

    return valid_BLEU


def plot_loss(train_loss, valid_loss, filename):
    plt.plot(train_loss, label=f'Test loss {filename}')
    plt.plot(valid_loss, label=f'Validation loss {filename}')
    plt.ylabel('Loss')
    plt.xlabel('Epochs')
    plt.legend(loc='lower right')
    plt.show()


def plot_BLEU(valid_bleu,filename):
    plt.plot(valid_bleu, label=f'Test loss {filename}')
    plt.ylabel('BLEU')
    plt.xlabel('Epochs')
    plt.legend(loc='lower right')
    plt.show()


def main():
    file_path = "../slurms/slurm_JRC_p3"
    train_loss, valid_loss = get_loss(file_path=file_path)
    plot_loss(train_loss, valid_loss, "slurm_JRC_p3")
    valid_bleu = get_BLEU(file_path=file_path)
    print(valid_bleu)
    plot_BLEU(valid_bleu, filename="slurm_JRC_p3")


if __name__ == '__main__':
    main()
