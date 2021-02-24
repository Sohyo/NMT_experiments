import os

#
# new_sys = []
# with open(os.path.join(orig_dir, file_name)) as f:
#     for line in f:
#         if line.startswith('<unk> '):
#             new_sys.append(line.split(' ', 1)[1])
#         elif line.endswith('<unk>'):
#             print(new_sys.append(line.split(' ', 1)[-1]))
#         else:
#             new_sys.append(line)
# with open('../meaningful_results/g_EMEA_p_3.out.sys', 'w') as filehandle:
#     for listitem in new_sys:
#         filehandle.write('%s' % listitem)

def arr2txt(arr, file_name):
    with open(file_name, "w") as txt_file:
        txt_file.writelines(arr)


def remove_unk(orig_dir, file_name):

    new_sys = []
    with open(os.path.join(orig_dir, file_name)) as file:
        for sentence in file:
            if sentence.startswith('<unk> <unk> '):
                new_sys.append(sentence.split(' ', 2)[2])
            elif sentence.startswith('<unk> '):
                new_sys.append(sentence.split(' ', 1)[1])
            elif sentence.endswith('<unk>'):
                new_sys.append(sentence.split(' ', 1)[-1])
            else:
                new_sys.append(sentence)
    arr2txt(arr=new_sys, file_name=os.path.join(orig_dir, file_name))


orig_dir = "../meaningful_results"
file_name = "GNOME_phrase_4_0.5_tag.sys"
remove_unk(orig_dir=orig_dir, file_name=file_name)
