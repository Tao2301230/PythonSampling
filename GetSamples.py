import os


def get_data_from_product_name():

    file_Path = os.path.abspath('/home/bantao/pcworkspace/bt_develop/datasets/prediction_pn.csv')
    print(file_Path)
    count = 0

    sample = list()
    with open(file_Path, 'r') as f:

        for line in f:
            count += 1
            if count % 2500 == 0:
                sample.append(line.split(',')[0])

    print(len(sample))
    print(sample[50])

    with open('output', 'w') as f:
        f.write('\n'.join(sample))


def get_data_from_ask_online():
    with open('/home/bantao/pcworkspace/bt_develop/CNN/datasets/ask_online.txt', 'r') as f:
        records = list(set(f.readlines()))
        records = [records[i] for i in range(0, len(records), 30) if len(records[i]) >= 10]
        print(len(records))
    with open('output_a_o', 'w') as f:
        f.write(''.join(records))


def get_data_from_knowledge_db():
    with open('/home/bantao/pcworkspace/bt_develop/CNN/datasets/knowledge_db_similar_question.txt', 'r') as f:
        records = list(set(f.readlines()))
        records = [records[i] for i in range(0, len(records), 30) if len(records[i]) >= 10]
        print(len(records))

    with open('output_knowledge_db', 'w') as f:
        f.write(''.join(records))

