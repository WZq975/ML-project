import os
import json


def main():
    for fold in ['HC', 'SZ']:
        path = os.path.join('./dataset/Fixation', fold)
        for person in os.listdir(path):
            path_stability = os.path.join(path, person, person + '_stability.json')
            path_saccade = os.path.join(path, person, person + '_saccade.json')
            path_tracking = os.path.join(path.replace('Fixation', 'LSR'), person, person + '_tracking.json')
            path_save = os.path.join(path.replace('Fixation', 'features'))
            if os.path.exists(path_stability) and os.path.exists(path_saccade) and os.path.exists(path_tracking):
                if not os.path.exists(path_save):
                    os.mkdir(path_save)
                stability = json.load(open(path_stability, 'r'))
                sac_stat = json.load(open(path_saccade, 'r'))
                tracking = json.load(open(path_tracking, 'r'))
                print(person)
                print(len(stability), len(sac_stat), len(tracking))

                features = stability + sac_stat + tracking
                with open(os.path.join(path_save, person + '_features.json'), 'w', encoding='utf-8') as f:
                    json.dump(features, f)


if __name__ == '__main__':
    main()