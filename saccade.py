import os
import json


def scaccade(fix_data, point_in_time, img_seq, point_list, person):
    delays_pos = [None for index in range(8)]
    delays_rev = [None for index in range(8)]
    j = 0
    cnt = 0
    for index in range(len(fix_data)):
        if point_in_time[10 + j][0] + 1700 <= fix_data[index][0] < point_in_time[10 + j][1]:
            if (fix_data[index][1] - point_list[img_seq[j]][0]) ** 2 + (fix_data[index][2] - point_list[img_seq[j]][1]) ** 2 < 30 ** 2:
                cnt += 1
        if fix_data[index][0] >= point_in_time[10 + j][1]:
            if img_seq[j] + 1 <= 4:
                if delays_pos[img_seq[j]] == None:
                    delays_pos[img_seq[j]] = cnt
                else:
                    delays_pos[img_seq[j] + 4] = cnt
            else:
                if delays_rev[img_seq[j] - 4] == None:
                    delays_rev[img_seq[j] - 4] = cnt
                else:
                    delays_rev[img_seq[j]] = cnt
            j += 1
            cnt = 0
        if j == 16:
            break


    if len(delays_rev) != 8 or len(delays_pos) != 8:
        print('failed extraction in {}'.format(person))
    else:
        return [delays_pos, delays_rev]


def main():
    point_list = [(317, 300), (233, 300), (487, 300), (571, 300), (317, 300), (233, 300), (487, 300), (571, 300)]
    for fold in ['HC', 'SZ']:
        path = os.path.join('./dataset/Fixation', fold)
        for person in os.listdir(path):

            trial_path = os.path.join(path, person, person + '_trial.json')
            data_path = os.path.join(path, person, person + '_fix_data.json')
            img_seq_path = os.path.join(path, person, 'saccade_img_seq.dat')
            save_path = os.path.join(path, person, person + '_saccade.json')

            if os.path.exists(trial_path) and os.path.exists(data_path) and os.path.exists(img_seq_path):
                fix_data = json.load(open(data_path, 'r'))
                point_in_time = json.load(open(trial_path, 'r'))
                dat_file = open(img_seq_path)
                img_seq = []
                for line in dat_file:
                    img_seq.append(int(line.split('\t')[0]) - 1)
                delays = scaccade(fix_data, point_in_time, img_seq, point_list, person)
                # compute statistics
                sac_stat = []
                for part in delays:
                    mean = sum(part) / len(part)
                    maximum = max(part)
                    variance = 0.0
                    for index in range(len(part)):
                        variance += (part[index] - mean) ** 2
                    stat = [mean, maximum, (variance / len(part)) ** 0.5]
                    sac_stat = sac_stat + stat
                print(person, sac_stat)
                with open(save_path, 'w', encoding='utf-8') as f:
                    json.dump(sac_stat, f)


if __name__ == '__main__':
    main()
