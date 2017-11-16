def can_attend_meetings(intervals):
    length = len(intervals)
    if length == 0:
        print True
    for i in range(length):
        for j in range(i+1, length):
            if min(intervals[i][1], intervals[j][1]) > max(intervals[i][0], intervals[j][0]):
                print False
    print True

if __name__ == '__main__':
    intervals = [[0, 30],[5, 10],[15, 20]]
    can_attend_meetings(intervals)
