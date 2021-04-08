from os.path import join
import numpy as np
import statistics
import matplotlib.pyplot as plt


def get_length_sentences_from_file(path_data: dir, file_name) -> list:
    length_sentences = []
    # print(join(path_data, file_name))
    with open(join(path_data, file_name)) as text:
        for sentence in text:
            words = sentence.split()
            length_sentences.append(len(words))

    return length_sentences

root_dir = "../final_results/"
list_of_data = ['EMEA', 'GNOME', 'JRC']
final_len_data = []
data_details = {}
for data in list_of_data:
    len_details_per_dataset = []
    # leng_dataset.append(get_length_sentences_from_file(join(root_dir, data), 'reference'))
    files = ['reference', 'baseline', 'original', 'phrase_4', 'phrase_4_tag']
    for file in files:
        len_details_per_dataset.append(statistics.mean(get_length_sentences_from_file(join(root_dir, data), file)))
    data_details.update({data: len_details_per_dataset})


#### bar plot : overlapping phrases
reference =[19.08, 13.61, 38.01]
baseline = [17.99, 13.07, 27.31]
finetune_orig = [18.75, 13.38, 36.87]
phrase_4 = [17.29, 12.85, 27.29]
phrase_4_tag = [18.02, 13.49, 27.25]
labels = ['EMEA', 'GNOME', 'JRC']

ind = np.arange(len(labels))  # the label locations
width = 0.13  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind, reference, width, label='Reference', color='dimgray')
rects2 = ax.bar(ind+width, baseline, width, label='Baseline',  color='cornflowerblue')
rects3 = ax.bar(ind+width*2, phrase_4, width, label='Phrase 4', color='lightsteelblue')
rects4 = ax.bar(ind+width*3, phrase_4_tag, width, label='Phrase 4 + Tag', color='lightblue')
rects5 = ax.bar(ind+width*4, finetune_orig, width, label='Original data', color='silver')



# ax.set_ylabel('Length of sentences', fontweight='bold')
ax.set_xlabel('Domains', fontweight='bold')
ax.set_xticks(ind+width+0.1)
ax.set_xticklabels(labels)
ax.autoscale_view()
ax.legend()


# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width()/2, height),
#                     xytext=(0, 2),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
#

#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)
#autolabel(rects4)
#autolabel(rects5)
fig.tight_layout()
plt.show()
