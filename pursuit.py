import os
import json
import math

# var
def get_var(distance, avg):
    var = 0.0
    for k in range(len(distance)):
        var += (distance[k] - avg) ** 2
    var = (var / len(distance)) ** 0.5
    return var


def pursuit(fix_data, point_in_time, person):
    cnt_ver = 0.0
    cnt_hor = 0.0
    cnt_lsr_1 = 0.0
    cnt_lsr_2 = 0.0

    for index in range(len(fix_data)):
        if 0 <= fix_data[index][1] <= 1024 and 0 <= fix_data[index][2] <= 768:
            if point_in_time[0][0] <= fix_data[index][0] <= point_in_time[0][1]:
                t = (fix_data[index][0] - point_in_time[0][0]) / 1000
                x = 512
                y = 384 + 256 * math.sin(2 * math.pi * 0.4 * t + math.pi)

                if ((x - fix_data[index][1]) ** 2 + (y - fix_data[index][2]) ** 2) ** 0.5 > 100:
                    cnt_ver += 1
                continue
            elif point_in_time[1][0] <= fix_data[index][0] <= point_in_time[1][1]:
                t = (fix_data[index][0] - point_in_time[1][0]) / 1000
                x = 512 + 341 * math.sin(2 * math.pi * 0.4 * t + 3 / 2 * math.pi)
                y = 384

                if ((x - fix_data[index][1]) ** 2 + (y - fix_data[index][2]) ** 2) ** 0.5 > 100:
                    cnt_hor += 1
                continue
            elif point_in_time[2][0] <= fix_data[index][0] <= point_in_time[2][1]:
                t = (fix_data[index][0] - point_in_time[2][0]) / 1000
                x = 512 + 341 * math.sin(2 * math.pi * 0.15 * t + 3 / 2 * math.pi)
                y = 384 + 256 * math.sin(2 * math.pi * 0.2 * t)

                if ((x - fix_data[index][1]) ** 2 + (y - fix_data[index][2]) ** 2) ** 0.5 > 100:
                    cnt_lsr_1 += 1
                continue
            elif point_in_time[3][0] <= fix_data[index][0] <= point_in_time[3][1]:
                t = (fix_data[index][0] - point_in_time[3][0]) / 1000
                x = 512 + 341 * math.sin(2 * math.pi * 0.3 * t + 3 / 2 * math.pi)
                y = 384 + 256 * math.sin(2 * math.pi * 0.4 * t)

                if ((x - fix_data[index][1]) ** 2 + (y - fix_data[index][2]) ** 2) ** 0.5 > 100:
                    cnt_lsr_2 += 1
                continue
    print(person, cnt_ver, cnt_hor, cnt_lsr_1, cnt_lsr_2)
    return cnt_ver, cnt_hor, cnt_lsr_1, cnt_lsr_2


def main():

    for fold in ['HC', 'SZ']:
        path = os.path.join('./dataset/LSR', fold)
        for person in os.listdir(path):
            trial_path = os.path.join(path, person, person + '_trial.json')
            data_path = os.path.join(path, person, person + '_fix_data.json')
            save_path = os.path.join(path, person, person + '_tracking.json')
            if os.path.exists(trial_path) and os.path.exists(data_path):
                fix_data = json.load(open(data_path, 'r'))
                # print(fix_data)
                point_in_time = json.load(open(trial_path, 'r'))
                # print(point_in_time)
                feature_tracking = pursuit(fix_data, point_in_time, person)
                print(person, feature_tracking)
                with open(save_path, 'w', encoding='utf-8') as f:
                    json.dump(feature_tracking, f)


if __name__ == '__main__':
    main()
