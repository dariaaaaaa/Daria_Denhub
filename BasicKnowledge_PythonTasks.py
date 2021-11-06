def filter_list(arr: list) -> list:
    filtered_list = []
    for i in arr:
        if type(i) == int:
            filtered_list.append(i)
    return filtered_list


def first_non_repeating_letter(s: str) -> str:
    unique_counter = {}
    for i in range(len(s)):
        if s[i].lower() in unique_counter.keys():
            unique_counter[s[i].lower()][0] = False
        else:
            unique_counter[s[i].lower()] = [True, i]

    values = list(unique_counter.values())
    for i in range(len(values)):
        if values[i][0] is True:
            return s[values[i][1]]

    return None


def digital_root(num: int) -> int:
    str_num = str(num)
    new_sum = 0
    for i in str_num:
        new_sum += int(i)

    if new_sum > 9:
        new_sum = digital_root(new_sum)
    return new_sum


def two_sum(nums: list, target: int) -> int:
    counter = 0
    length = len(nums)
    sorted_nums = sorted(nums)

    for i in range(length):
        if i != 0 and sorted_nums[i - 1] + sorted_nums[i] >= target:
            break

        temp = target - sorted_nums[i]

        mid = length // 2
        low = 0
        high = length - 1

        while sorted_nums[mid] != temp and low <= high:
            if temp > sorted_nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        if low <= high:
            counter += 1
    return counter


def friends_list(s: str) -> str:
    inv_list = s.upper().rstrip().split(';')
    inv_list = [person.split(':')[::-1] for person in inv_list]
    inv_list.sort(key=lambda elem: (elem[0], elem[1]))
    inv_list = [', '.join(i) for i in inv_list]
    inv_string = ')('.join(inv_list)
    return '(' + inv_string + ')'


def nextBigger(num: int) -> int:
    num_arr = list(str(num))
    max_num = int("".join(sorted(num_arr)[::-1]))
    num_set = set(num_arr)

    while num <= max_num:
        num += 1
        if set(str(num)) == num_set:
            return num

    return -1


def convert_to_ipv4(num: int) -> str:
    binary_num = bin(num).replace("0b", "")
    binary_num = '0' * (32 - len(binary_num)) + binary_num
    octets = [str(int(binary_num[i:(i + 8)], 2)) for i in range(0, len(binary_num), 8)]
    return '.'.join(octets)


if __name__ == '__main__':
    print('TASK 1')
    inputs = [[1, 2, 'a', 'b'], [1, 'a', 'b', 0, 15], [1, 2, 'aasf', '1', '123', 123]]
    for i in inputs:
        new_arr = filter_list(i)
        print(f'Input: {i}. Result: {new_arr}')

    print('\nTASK 2')
    inputs = ['stress', 'sTreSS', 'AAAAAA']
    for i in inputs:
        s = first_non_repeating_letter(i)
        print(f'Input: {i}. Result: {s}')

    print('\nTASK 3')
    inputs = [16, 942, 132189, 493193]
    for i in inputs:
        res = digital_root(i)
        print(f'Input: {i}. Result: {res}')

    print('\nTASK 4')
    inputs = [[[1, 3, 6, 2, 2, 0, 4, 5], 5], [[1, 3, 6, 2, 2, 0, 4, 5], 4], [[1, 1, 1], 3]]
    for i in inputs:
        res = two_sum(i[0], i[1])
        print(f'Input: {i}. Result: {res}')

    print('\nTASK 5')
    s = "Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    print(f'Input: {s}')
    new_list = friends_list(s)
    print(f'Result: {new_list}')

    print('\nExtra tasks:')

    print('\nTASK 1')
    inputs = [12, 513, 2017, 9, 111, 531]
    for i in inputs:
        res = nextBigger(i)
        print(f'Input: {i}. Result: {res}')

    print('\nTASK 2')
    inputs = [2149583361, 32, 0]
    for i in inputs:
        res = convert_to_ipv4(i)
        print(f'Input: {i}. Result: {res}')
