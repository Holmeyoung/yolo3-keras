def convert_to_yolo(f_r, f_w):
    for line in f_r:
        line = line.replace('"', '')
        line = line.replace(':', '')
        line = line.replace('(', '')
        line = line.replace('),', '')
        line = line.replace(');', '')
        line = line.replace(').', '')
        line = line.replace('\n', '')
        line = line.replace(', ', ',')

        loc = line.split(' ')
        # 图像中没有要标注的物体
        if len(loc) == 1:
            continue
        f_w.write('/root/meeting_room/data/brainwash/' + loc[0])
        for i in range(1,len(loc)):
            loc[i] = ' ' + ','.join(str(int(float(j))) for j in loc[i].split(',')) + ',0'
            f_w.write(loc[i])
        f_w.write('\n')

if __name__ == "__main__":
    f_r_test = open('brainwash_test.idl')
    f_r_train = open('brainwash_train.idl')
    f_r_val = open('brainwash_val.idl')

    f_w = open('yolo_data.txt', 'w')

    convert_to_yolo(f_r_test, f_w)
    convert_to_yolo(f_r_train, f_w)
    convert_to_yolo(f_r_val, f_w)

    f_r_test.close()
    f_r_train.close()
    f_r_val.close()
    f_w.close()