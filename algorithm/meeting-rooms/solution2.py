def can_attend_meetings(intervals):
    length = len(intervals)
    if length == 0 or length == 1:
        return True
    intervals.sort(key=lambda list:list[0])
    for i in range(1,length):
        if intervals[i][0] < intervals[i-1][1]:
            print False
    print True

if __name__ == '__main__':
    intervals = [[0, 30],[15, 20],[5, 10]]
    can_attend_meetings(intervals)
