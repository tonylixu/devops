def cal_points(ops):
    ops_new = []
    for i in ops:
        # Simple cancel the last point
        if i == "C":
            ops_new.pop()
        # Double the last point
        elif i == "D":
            val = ops_new[-1]*2
            ops_new.append(val)
        elif i == "+":
            val_1 = ops_new[-1]
            val_2 = ops_new[-2]
            ops_new.append(val_1 + val_2)
        else:
            ops_new.append(int(i))
    return sum(ops_new)

if __name__ == '__main__':
    array = ["5","-2","4","C","D","9","+","+"]
    cal_points(array)
