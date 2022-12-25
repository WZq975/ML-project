import os
from scipy import io
import json


def stability(fix_data, point_in_time, person):
    distances_1_wo = []  # trail 0-7 without interference
    distances_1_w = []  # ... with interference
    distances_2_wo = []  # trail 8
    distances_2_w = []
    distances_3_wo = []  # trail 9
    distances_3_w = []
    # print('=============={}============'.format(persons[i]))
    for index in range(len(fix_data)):
        if 0 <= fix_data[index][1] <= 800 and 0 <= fix_data[index][2] <= 600:
            if point_in_time[0][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[0][0] + 1500 + 200 + 5000:
                distances_1_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[0][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[0][1]:
                distances_1_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif point_in_time[1][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[1][0] + 1500 + 200 + 5000:
                distances_1_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[1][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[1][1]:
                distances_1_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif point_in_time[2][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[2][0] + 1500 + 200 + 5000:
                distances_1_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[2][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[2][1]:
                distances_1_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif point_in_time[3][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[3][0] + 1500 + 200 + 5000:
                distances_1_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[3][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[3][1]:
                distances_1_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif point_in_time[4][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[4][0] + 1500 + 200 + 5000:
                distances_1_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[4][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[4][1]:
                distances_1_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif point_in_time[5][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[5][0] + 1500 + 200 + 5000:
                distances_1_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[5][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[5][1]:
                distances_1_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif point_in_time[6][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[6][0] + 1500 + 200 + 5000:
                distances_1_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[6][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[6][1]:
                distances_1_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif point_in_time[7][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[7][0] + 1500 + 200 + 5000:
                distances_1_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[7][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[7][1]:
                distances_1_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif point_in_time[8][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[8][0] + 1500 + 200 + 5000:
                distances_2_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[8][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[8][1]:
                distances_2_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif point_in_time[9][0] + 1500 + 200 <= fix_data[index][0] <= point_in_time[9][0] + 1500 + 200 + 5000:
                distances_3_wo.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue
            elif point_in_time[9][0] + 1500 + 200 + 5000 + 200 <= fix_data[index][0] <= point_in_time[9][1]:
                distances_3_w.append(((400 - fix_data[index][1]) ** 2 + (300 - fix_data[index][2]) ** 2) ** 0.5)
                continue

            elif fix_data[index][0] > point_in_time[9][1]:
                if len(distances_1_w) == 0 or len(distances_2_w) == 0 or len(distances_3_w) == 0 or len(distances_1_wo) == 0 or len(distances_2_wo) == 0 or len(distances_3_wo) == 0:
                    print('{} has wrong time! distance_1 is {}, distance_2 is {}, distance_3 is {}!'
                          .format(person, len(distances_1_w) + len(distances_1_wo), len(distances_2_w) + len(distances_2_wo), len(distances_3_w) + len(distances_3_wo)))
                    break
                else:
                    mean_distance_1 = (sum(distances_1_w) + sum(distances_1_wo)) / (
                                len(distances_1_w) + len(distances_1_wo))
                    mean_distance_2 = (sum(distances_2_w) + sum(distances_2_wo)) / (
                                len(distances_2_w) + len(distances_2_wo))
                    mean_distance_3 = (sum(distances_3_w) + sum(distances_3_wo)) / (
                                len(distances_3_w) + len(distances_3_wo))
                    print([mean_distance_1, mean_distance_2, mean_distance_3])
                    return [mean_distance_1, mean_distance_2, mean_distance_3]


def main():

    for fold in ['HC', 'SZ']:
        path = os.path.join('./dataset/Fixation', fold)
        for person in os.listdir(path):
            trial_path = os.path.join(path, person, person + '_trial.json')
            data_path = os.path.join(path, person, person + '_fix_data.json')
            save_path = os.path.join(path, person, person + '_stability.json')
            if os.path.exists(trial_path) and os.path.exists(data_path):
                fix_data = json.load(open(data_path, 'r'))
                point_in_time = json.load(open(trial_path, 'r'))
                feature_stability = stability(fix_data, point_in_time, person)
                print(person, feature_stability)
                with open(save_path, 'w', encoding='utf-8') as f:
                    json.dump(feature_stability, f)


if __name__ == '__main__':
    main()