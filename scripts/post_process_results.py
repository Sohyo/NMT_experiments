import os


orig_dir = "../meaningful_results"
file_name = "g_EMEA_p_3.out_orig.sys"

new_sys = []
with open(os.path.join(orig_dir, file_name)) as f:
    for line in f:
        if line.startswith('<unk> '):
            new_sys.append(line.split(' ', 1)[1])
        # elif line.endswith('<unk>'):
        #     print("hey")
        #     print(new_sys.append(line.split(' ', 1)[-1]))
        else:
            new_sys.append(line)
with open('../meaningful_results/g_EMEA_p_3.out.sys', 'w') as filehandle:
    for listitem in new_sys:
        filehandle.write('%s' % listitem)
