def calculate_difference(a, b):
    return abs(a - b)


def calculate_closest_difference_with_sorted_elements(candidates, number_of_candidates):
    closest_difference = calculate_difference(candidates[1], candidates[0])

    for index in range(1, number_of_candidates - 1):
        current_difference = calculate_difference(candidates[index], candidates[index + 1])
        if current_difference < closest_difference:
            closest_difference = current_difference
    return closest_difference


if __name__ == '__main__':
    horse_strengths = []

    n = int(input())
    for i in range(n):
        pi = int(input())
        horse_strengths.append(pi)

    horse_strengths.sort()
    print(calculate_closest_difference_with_sorted_elements(horse_strengths, n))
