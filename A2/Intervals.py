import sys

def merge_tuples(intervals):
    # temp_tuple.sort(key=lambda interval: interval[0])
    # merged = [temp_tuple[0]]
    # for current in temp_tuple:
    #     previous = merged[-1]
    #     if current[0] <= previous[1]:
    #         previous[1] = max(previous[1], current[1])
    #     else:
    #         merged.append(current)



    # sortedIntervals = sorted(intervals, key= lambda tup: tup[0])
    # collapsed = []

    # for i in sortedIntervals:
    #     if not collapsed:
    #         collapsed.append(i)
    #     else:
    #         temp = collapsed.pop()
    #         if temp[1] >= i[0]:
    #             new = (temp[0], max(temp[1], i[1]))
    #             collapsed.append(new)
    #         else:
    #             collapsed.append(temp)
    #             collapsed.append(i)
    # return collapsed

    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
            else:
                merged.append(higher)
    return merged

# the result list to be returned is initialized and the original is sorted.
# The while loop iterates through the original tuples and compares it to the last element
# of the result list tuples.
#     tuples_list = sorted(tuples_list)
#     merged = [tuples_list[0]]
#     while True:
#         if tuples_list == []:
#             break

# # if the original tuple overlaps, and extends farther than the result tuple,
# # then the two tuples are collapsed into one and added to the result list.
#         elif tuples_list[0][0] <= merged[-1][1]:
#             if tuples_list[0][1] > merged[-1][1]:  
#                 start = merged[-1][0]
#                 end = tuples_list[0][1]
#                 merged[-1] = (start, end)
#                 tuples_list.remove(tuples_list[0])

#             else:
#                 tuples_list.remove(tuples_list[0])

# # if tuples doesn't overlap then it is added to result list.
#         else:
#             merged.append(tuples_list[0])
#             tuples_list.remove(tuples_list[0])
             
#     return merged


    # if len(intervals) < 2:
    #     return intervals
    # intervals.sort()
    # collapsedIntervals = [intervals[0]]
    # print(intervals)
    # for i,j in intervals[1:]:
    #     if i > collapsedIntervals[-1][1]:
    #         collapsedIntervals.append((i, j))
    #     elif j > collapsedIntervals[-1][1]:
    #         collapsedIntervals[-1][1] = j
    # return collapsedIntervals

def sort_by_interval_size(intervals):
    intervals.sort(key=lambda interval: interval[1] - interval[0], reverse=True)

def main():
    num_intervals = int(sys.stdin.readline().strip())
    


    intervals = []
    for i in range(num_intervals):
        templist = sys.stdin.readline().split()
        intervals.append((int(templist[0]), int(templist[1])))
    print(intervals)
    m = merge_tuples(intervals)
    ms = sort_by_interval_size(m)
    print(m)
    print(ms)


if __name__ == "__main__":
    main()
