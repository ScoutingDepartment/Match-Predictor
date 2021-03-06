from team import *
from alliance import *
from match import *

raw_data = {
    51: [1.00, [0.50, 0.25], [0.00, 0.00], [2.90, 1.79], [0.90, 1.10], [0.70, 1.64], [1.10, 1.91], 0.70],
    56: [1.00, [0.67, 0.58], [0.5, 0.25], [3.90, 1.73], [1.70, 2.16], [0.60, 0.97], [1.30, 1.95], 0.80],
    78: [1.00, [0.00, 0.00], [0.90, 0.32], [2.70, 2.36], [0.90, 1.37], [0.80, 1.93], [1.60, 3.20], 0.70],
    111: [0.80, [0.20, 0.45], [0.00, 0.00], [2.20, 1.93], [1.10, 1.10], [0.50, 0.97], [0.70, 1.89], 0.10],
    125: [1.00, [1.25, 0.50], [1.50, 0.50], [4.30, 2.11], [0.80, 1.32], [0.40, 0.97], [0.70, 1.34], 0.30],
    157: [1.00, [0.67, 0.58], [0.5, 0.25], [0.73, 1.01], [0.45, 0.82], [0.18, 0.40], [3.36, 3.41], 0.00],
    176: [1.00, [1.25, 0.96], [1.33, 0.52], [5.10, 1.79], [0.20, 0.42], [0.50, 0.85], [0.10, 0.32], 0.80],
    177: [1.00, [0.75, 0.50], [0.5, 0.25], [3.90, 1.66], [0.40, 0.84], [1.30, 1.70], [0.70, 1.34], 0.70],
    234: [1.00, [0.00, 0.00], [2.30, 0.95], [3.70, 1.34], [0.30, 0.67], [0.80, 1.62], [0.60, 1.26], 1.00],
    247: [0.90, [0.50, 0.25], [0.50, 0.58], [1.40, 1.17], [1.40, 1.78], [0.10, 0.32], [2.90, 2.88], 0.30],
    250: [0.90, [0.00, 0.00], [0.50, 0.71], [0.78, 1.56], [1.11, 1.27], [0.44, 1.01], [4.56, 3.81], 0.11],
    365: [1.00, [0.50, 0.25], [1.60, 0.55], [4.50, 1.51], [0.20, 0.42], [1.00, 1.63], [0.70, 2.21], 0.70],
    494: [1.00, [0.80, 0.45], [0.5, 0.25], [3.55, 1.92], [0.73, 1.49], [1.27, 1.56], [0.73, 1.68], 0.70],
    548: [0.80, [0.00, 0.00], [0.71, 0.49], [1.44, 1.88], [1.11, 1.36], [0.33, 1.00], [0.78, 1.99], 0.44],
    578: [1.00, [0.50, 0.25], [1.17, 0.41], [1.44, 1.42], [1.11, 1.05], [0.00, 0.00], [6.00, 2.92], 0.11],
    772: [1.00, [0.67, 0.58], [1.00, 0.63], [4.90, 1.85], [0.10, 0.32], [0.60, 1.26], [0.20, 0.63], 0.60],
    857: [1.00, [0.50, 0.25], [0.00, 0.00], [0.00, 0.00], [1.80, 2.15], [0.40, 0.97], [5.20, 3.05], 0.10],
    865: [1.00, [1.17, 0.75], [1.50, 0.58], [4.10, 1.37], [0.50, 1.08], [1.40, 2.32], [0.10, 0.32], 0.70],
    977: [1.00, [0.00, 0.00], [0.5, 0.25], [1.10, 1.29], [0.70, 0.95], [0.30, 0.95], [1.50, 2.01], 0.56],
    1018: [0.90, [0.25, 0.50], [0.80, 0.45], [3.90, 2.23], [0.40, 0.70], [1.80, 2.04], [1.60, 2.72], 0.10],
    1391: [1.00, [0.50, 0.25], [1.25, 0.50], [3.10, 2.33], [0.80, 1.32], [0.30, 0.67], [0.90, 1.91], 0.80],
    1418: [0.90, [0.25, 0.50], [0.5, 0.25], [2.00, 2.05], [0.40, 0.52], [0.00, 0.00], [1.00, 1.76], 0.70],
    1519: [1.00, [1.67, 0.50], [0.5, 0.25], [3.90, 1.73], [0.10, 0.32], [1.30, 2.11], [0.00, 0.00], 0.50],
    1625: [1.00, [0.75, 0.96], [1.50, 0.50], [1.90, 1.73], [1.20, 1.87], [0.80, 1.75], [1.00, 1.63], 0.90],
    1711: [1.00, [0.00, 0.00], [0.5, 0.25], [2.56, 2.19], [1.00, 1.00], [0.33, 0.71], [2.78, 4.18], 0.56],
    2194: [1.00, [0.50, 0.25], [1.60, 0.55], [3.00, 1.66], [0.67, 1.32], [0.11, 0.33], [0.78, 1.56], 0.78],
    2337: [1.00, [1.82, 1.17], [0.00, 0.00], [2.55, 1.57], [0.00, 0.00], [3.55, 2.07], [0.27, 0.65], 0.50],
    2451: [1.00, [0.57, 0.53], [0.5, 0.25], [1.70, 1.95], [0.10, 0.32], [3.90, 2.28], [0.90, 1.73], 0.30],
    2481: [1.00, [1.89, 0.60], [0.00, 0.00], [3.20, 2.30], [0.10, 0.32], [2.80, 2.86], [1.00, 1.89], 0.10],
    2501: [1.00, [0.00, 0.00], [0.88, 0.35], [2.20, 1.75], [0.50, 0.85], [0.10, 0.32], [2.10, 3.21], 0.60],
    2791: [1.00, [0.80, 0.84], [0.00, 0.00], [4.11, 2.09], [0.00, 0.00], [0.22, 0.67], [0.33, 1.00], 0.00],
    2834: [1.00, [0.50, 0.25], [1.50, 0.55], [3.88, 2.03], [0.38, 0.74], [0.25, 0.71], [1.00, 2.83], 0.63],
    3117: [0.80, [0.00, 0.00], [0.5, 0.25], [0.90, 1.10], [0.20, 0.42], [0.40, 0.84], [0.00, 0.00], 0.20],
    3130: [1.00, [1.50, 1.05], [0.50, 0.71], [3.40, 2.01], [0.10, 0.32], [1.40, 2.37], [0.30, 0.95], 0.70],
    3274: [1.00, [0.50, 0.25], [0.5, 0.25], [3.90, 2.38], [1.40, 2.17], [0.40, 0.97], [2.80, 3.01], 0.10],
    3461: [1.00, [0.60, 0.55], [0.5, 0.25], [3.78, 1.86], [0.11, 0.33], [1.78, 1.79], [1.44, 2.51], 0.67],
    3504: [0.80, [0.00, 0.00], [0.80, 0.84], [1.70, 2.16], [0.00, 0.00], [0.80, 1.14], [0.40, 0.97], 0.30],
    3535: [1.00, [0.00, 0.00], [0.67, 0.58], [1.00, 1.73], [1.33, 1.58], [1.44, 2.30], [2.56, 3.05], 0.44],
    3536: [1.00, [1.00, 0.76], [0.5, 0.25], [2.55, 1.37], [0.64, 1.12], [2.18, 2.27], [0.82, 2.71], 0.40],
    3542: [1.00, [0.50, 0.25], [1.71, 0.49], [4.33, 1.87], [0.56, 1.33], [0.00, 0.00], [0.33, 1.00], 0.89],
    3572: [1.00, [0.50, 0.25], [0.5, 0.25], [0.33, 0.50], [1.67, 1.32], [0.33, 1.00], [3.00, 2.06], 0.67],
    3695: [1.00, [0.50, 0.25], [0.5, 0.25], [1.56, 2.40], [0.44, 0.73], [0.89, 2.67], [3.33, 3.35], 0.67],
    3844: [0.90, [0.00, 0.00], [0.5, 0.25], [0.10, 0.32], [0.40, 0.70], [0.50, 1.08], [1.30, 1.83], 0.20],
    4028: [1.00, [1.60, 0.84], [0.5, 0.25], [3.60, 1.35], [0.10, 0.32], [0.40, 0.70], [0.00, 0.00], 0.90],
    4122: [0.80, [0.00, 0.00], [1.29, 0.49], [0.40, 0.70], [1.00, 1.25], [0.00, 0.00], [3.50, 2.37], 0.00],
    4198: [1.00, [0.00, 0.00], [0.75, 0.46], [1.00, 1.63], [1.70, 2.16], [0.90, 1.37], [3.20, 2.97], 0.60],
    4458: [1.00, [0.50, 0.25], [0.5, 0.25], [0.20, 0.63], [0.60, 0.84], [0.00, 0.00], [6.60, 1.43], 0.60],
    4645: [1.00, [0.00, 0.00], [0.00, 0.00], [0.00, 0.00], [2.00, 1.15], [0.00, 0.00], [7.20, 1.32], 0.00],
    4905: [0.90, [0.50, 0.25], [0.5, 0.25], [2.18, 1.78], [1.00, 1.79], [0.00, 0.00], [1.27, 2.28], 0.00],
    4917: [1.00, [0.00, 0.00], [1.83, 0.41], [4.10, 2.38], [0.40, 1.26], [0.70, 1.25], [1.20, 2.30], 0.60],
    4946: [1.00, [0.50, 0.25], [0.5, 0.25], [2.50, 2.55], [1.10, 0.99], [0.10, 0.32], [2.50, 2.37], 0.10],
    5036: [1.00, [0.00, 0.00], [1.67, 0.52], [0.00, 0.00], [0.67, 0.71], [0.11, 0.33], [5.44, 2.88], 0.11],
    5234: [1.00, [0.00, 0.00], [1.22, 0.67], [1.45, 1.86], [0.27, 0.47], [1.27, 1.49], [3.45, 3.67], 0.18],
    5339: [0.90, [0.00, 0.00], [0.5, 0.25], [0.20, 0.42], [1.10, 1.10], [0.70, 1.49], [1.90, 1.79], 0.10],
    5406: [1.00, [1.50, 0.93], [1.50, 0.71], [4.30, 2.41], [0.30, 0.67], [0.40, 0.97], [0.80, 1.93], 0.90],
    5434: [1.00, [1.00, 1.41], [0.5, 0.25], [2.89, 1.45], [0.11, 0.33], [0.00, 0.00], [0.67, 1.41], 0.22],
    5443: [1.00, [0.00, 0.00], [0.00, 0.00], [0.22, 0.44], [0.33, 0.50], [0.22, 0.44], [3.11, 2.93], 0.22],
    5492: [1.00, [0.00, 0.00], [1.00, 1.41], [3.00, 1.94], [0.80, 1.55], [0.50, 0.85], [0.70, 1.89], 0.30],
    5740: [0.80, [0.00, 0.00], [0.5, 0.25], [0.00, 0.00], [0.40, 0.70], [1.40, 2.12], [2.20, 3.01], 0.10],
    5883: [1.00, [0.50, 0.25], [0.5, 0.25], [2.10, 1.60], [0.30, 0.48], [0.80, 1.23], [0.40, 1.26], 0.40],
    5914: [1.00, [0.00, 0.00], [0.5, 0.25], [2.30, 1.49], [1.10, 1.52], [0.10, 0.32], [3.00, 3.02], 0.20],
    6193: [1.00, [0.50, 0.25], [0.67, 0.58], [1.70, 1.83], [0.40, 0.52], [0.90, 1.37], [2.70, 3.02], 0.30],
    6590: [0.90, [0.00, 0.00], [0.60, 0.55], [0.30, 0.67], [1.00, 1.15], [1.80, 2.04], [0.90, 1.45], 0.10],
    6823: [0.90, [0.00, 0.00], [0.00, 0.00], [0.00, 0.00], [1.67, 1.58], [0.22, 0.67], [5.56, 3.21], 0.11],
    6869: [0.90, [0.00, 0.00], [0.50, 0.71], [0.00, 0.00], [1.25, 1.49], [0.38, 1.06], [3.88, 2.53], 0.25],
    6936: [1.00, [0.00, 0.00], [0.75, 0.50], [1.00, 1.49], [1.10, 0.99], [0.50, 1.27], [2.70, 2.45], 0.50],
    6947: [0.90, [0.00, 0.00], [0.00, 0.00], [0.00, 0.00], [0.90, 1.29], [0.00, 0.00], [4.60, 2.27], 0.10]}
data = {}
for i in raw_data:
    data[i] = make_team(raw_data, i)

teams = list(data.keys())

raw_schedule = [[2337, 125, 3274, 3535, 176, 5740],
                [5339, 365, 4028, 1625, 51, 3572],
                [3542, 5492, 250, 4458, 2501, 3461],
                [2481, 548, 1711, 2194, 1391, 3844],
                [2834, 977, 1018, 6193, 56, 3695],
                [4946, 772, 5883, 111, 6823, 234],
                [4905, 857, 5234, 5406, 3536, 6869],
                [4122, 1519, 157, 5036, 2451, 4198],
                [5443, 4917, 247, 3130, 177, 4645],
                [5914, 3504, 578, 78, 6936, 6590],
                [2791, 494, 865, 6947, 3117, 5434],
                [1418, 6193, 3274, 3542, 4028, 4946],
                [5036, 2481, 111, 5740, 4458, 5339],
                [3572, 5443, 2194, 157, 1018, 857],
                [51, 4122, 176, 578, 5234, 1711],
                [6936, 4917, 3536, 5434, 2451, 250],
                [234, 977, 2501, 177, 1418, 125],
                [5406, 56, 6947, 3844, 365, 3117],
                [4645, 3535, 5492, 6869, 5914, 2834],
                [6823, 494, 548, 1625, 247, 3504],
                [4198, 4905, 772, 3695, 6590, 2791],
                [3461, 5883, 3130, 865, 78, 1391],
                [2337, 234, 3844, 1519, 250, 857],
                [5234, 2481, 125, 177, 3542, 5434],
                [5914, 5406, 6823, 3274, 3572, 1711],
                [365, 578, 4198, 4645, 977, 772],
                [2451, 1418, 176, 3504, 3130, 5339],
                [494, 1625, 111, 1018, 78, 3535],
                [3461, 4946, 5036, 2337, 6590, 4917],
                [4028, 5883, 157, 56, 5740, 2791],
                [3695, 865, 2194, 51, 2501, 5443],
                [1391, 4458, 1519, 6869, 3117, 6936],
                [4122, 3536, 4905, 2834, 6947, 548],
                [247, 6193, 3542, 5492, 5406, 111],
                [1625, 3274, 56, 250, 1711, 4645],
                [2481, 365, 3695, 3130, 578, 4946],
                [1018, 3844, 125, 4458, 6823, 4917],
                [4122, 78, 5339, 1519, 5443, 5740],
                [6947, 2194, 177, 772, 3461, 5914],
                [234, 176, 6869, 247, 2834, 2791],
                [5492, 5036, 51, 3117, 3504, 977],
                [6936, 548, 4028, 865, 157, 2501],
                [1418, 2337, 3572, 1391, 4198, 3536],
                [6590, 857, 3535, 5883, 5434, 5234],
                [6193, 4905, 5740, 494, 2451, 234],
                [2791, 5339, 5492, 56, 578, 2194],
                [4122, 250, 3130, 772, 1018, 3542],
                [3504, 3572, 6947, 4946, 5443, 2481],
                [157, 6590, 51, 3536, 125, 1625],
                [977, 177, 5883, 548, 3274, 2451],
                [5434, 6869, 6193, 78, 3844, 5036],
                [5914, 3695, 247, 5234, 4458, 1418],
                [4028, 1711, 3117, 3535, 4917, 4198],
                [2337, 2834, 857, 6936, 111, 365],
                [865, 4645, 3461, 6823, 1519, 4905],
                [176, 5406, 2501, 494, 1391, 772],
                [1018, 6869, 6590, 5339, 1418, 6947],
                [51, 3117, 2451, 3844, 2481, 247],
                [1625, 3695, 4122, 3274, 5492, 5883],
                [1711, 865, 4198, 6193, 857, 3504],
                [6823, 5434, 3130, 5740, 2501, 2337],
                [250, 1391, 2834, 578, 4028, 494],
                [4917, 176, 5914, 4905, 157, 365],
                [4645, 3542, 2194, 234, 3536, 5036],
                [5234, 111, 3572, 125, 56, 1519],
                [4458, 2791, 78, 177, 4946, 548],
                [3535, 5443, 977, 5406, 3461, 6936],
                [4198, 6869, 250, 176, 2481, 5883],
                [1711, 5339, 3695, 3542, 2337, 494],
                [2501, 111, 578, 4917, 6947, 3274],
                [2451, 6590, 4458, 6823, 3572, 2834],
                [247, 5434, 56, 3461, 3504, 4122],
                [857, 3130, 1391, 125, 5914, 5036],
                [5740, 2194, 772, 3844, 6936, 1625],
                [1519, 3536, 3535, 2791, 6193, 177],
                [4645, 5406, 1018, 4946, 865, 51],
                [548, 365, 5443, 4028, 5234, 234],
                [78, 157, 1418, 3117, 4905, 5492],
                [977, 6947, 3542, 857, 1625, 176],
                [2501, 5914, 6193, 2791, 4122, 2481],
                [4458, 3535, 865, 1391, 51, 56],
                [2451, 125, 4946, 2194, 4198, 494],
                [4905, 234, 6936, 3274, 3117, 1018],
                [5443, 5036, 1418, 365, 250, 6823],
                [3536, 5740, 78, 977, 1711, 247],
                [6590, 4645, 3844, 111, 3130, 4028],
                [4917, 1519, 3504, 3695, 5883, 5406],
                [157, 177, 3572, 578, 6869, 2337],
                [2834, 3461, 5339, 772, 548, 5234],
                [5434, 1391, 1711, 5492, 1018, 365],
                [3536, 3274, 494, 3130, 4198, 4458],
                [5883, 6936, 6823, 6947, 51, 6193],
                [578, 3542, 6590, 2194, 247, 1519],
                [3117, 857, 5740, 177, 3695, 3461],
                [56, 2337, 2451, 5443, 78, 5914],
                [865, 5036, 4917, 3572, 5492, 234],
                [157, 2791, 5234, 250, 111, 977],
                [2834, 1625, 5406, 2481, 1418, 5434],
                [3504, 4028, 6869, 125, 772, 4122],
                [5339, 3844, 4946, 2501, 3535, 4905],
                [548, 4645, 3117, 176, 6193, 2337],
                [6947, 234, 1519, 1711, 3130, 157],
                [51, 5740, 5914, 4198, 2834, 3542],
                [3274, 772, 2481, 857, 4917, 78],
                [4028, 4905, 4458, 5434, 2194, 977],
                [2501, 4946, 1625, 6869, 5234, 2451],
                [111, 177, 1391, 250, 3695, 3504],
                [3572, 2791, 6936, 1418, 4122, 4645],
                [365, 247, 125, 5883, 5339, 865],
                [5492, 3461, 5443, 176, 3844, 3536],
                [548, 1018, 578, 5036, 3535, 5406],
                [56, 494, 177, 6590, 6823, 2481]]
schedule = []
for match in raw_schedule:
    schedule.append(make_match(data, match[:3], match[-3:]))  # TODO fix

# TODO make this use Match

alliances = {
    1: [56, 4028, 1391],
    2: [5406, 2481, 2451],
    3: [3536, 125, 2194],
    4: [176, 177, 772],
    5: [3542, 2337, 1018],
    6: [494, 865, 4917],
    7: [234, 1519, 3130],
    8: [4946, 2791, 2834]
}
for k, v in alliances.items():
    alliances[k] = make_alliance(data, v)

elims_order = [
    [
        [{1: 1}, {8: 1}],
        [{4: 1}, {5: 1}]],
    [
        [{2: 1}, {7: 1}],
        [{3: 1}, {6: 1}]
    ]
]
