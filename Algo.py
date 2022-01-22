class Algo:

    @staticmethod
    def bubble_sort(l2: list):
        """
        :param l1: list
        :return: sorted list and steps
        """
        step = 0
        l1 = l2
        for iter_num in range(len(l1) - 1, 0, -1):
            for idx in range(iter_num):
                step += 1
                if l1[idx] > l1[idx + 1]:
                    temp = l1[idx]
                    l1[idx] = l1[idx + 1]
                    l1[idx + 1] = temp
                    step += 2
        return l1, step

    @staticmethod
    def merge_sort(arr2):
        step = 0
        arr = arr2
        if len(arr2) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            L, step1 = Algo.merge_sort(L)
            R, step2 = Algo.merge_sort(R)
            step += len(arr) + step1 + step2

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                step += 3
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                step += 3
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                step += 3
                arr[k] = R[j]
                j += 1
                k += 1
            return arr, step
        else:
            return arr, 0

    @staticmethod
    def insertion_sort(l2):
        """
        :param l1: list
        :return: ordered list
        """
        l1 = l2
        steps = 0
        for i in range(1, len(l1)):
            j = i-1
            curr = l1[i]
            steps += 3
            while curr < l1[j] and j >= 0:
                l1[j+1] = l1[j]
                j -= 1
                steps += 3
            l1[j+1] = curr
            steps += 1
        return l1, steps

    @staticmethod
    def selection_sort(l1):
        """
        :param input_list:
        :return: Sorted List
        """
        input_list = [elem for elem in l1]
        steps = 0
        for idx in range(len(input_list)):
            min_idx = idx
            for j in range(idx + 1, len(input_list)):
                steps += 1
                if input_list[min_idx] > input_list[j]:
                    min_idx = j
                    steps += 1
            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
        steps += 3
        return input_list, steps

    @staticmethod
    def counting_sort(l1):
        """
        :param l1: list
        :return: ordered list, steps
        """
        steps = 0
        freq = [0 for _ in range(max(l1)+1)]
        res = [0 for _ in range(len(l1))]
        prefix_sum = [0 for _ in range(max(l1)+1)]
        for elem in l1:
            freq[elem] += 1
        prefix_sum[0] = freq[0]
        for i in range(1, len(freq)):
            prefix_sum[i] = freq[i] + prefix_sum[i-1]

        for elem in l1:
            res[prefix_sum[elem]-1] = elem
            prefix_sum[elem] -= 1

        steps += (max(l1)+1) * 2 + 4 * len(l1) + 1 + len(freq)
        return res, steps

    @staticmethod
    def partition(start, end, array):
        step = 2
        pivot_index = start
        pivot = array[pivot_index]
        while start < end:
            while start < len(array) and array[start] <= pivot:
                start += 1
                step += 1
            while array[end] > pivot:
                end -= 1
                step += 1
            if start < end:
                array[start], array[end] = array[end], array[start]
                step += 3
        array[end], array[pivot_index] = array[pivot_index], array[end]
        step += 3
        return end, step

    @staticmethod
    def quick_sort(start, end, array):
        if start < end:
            p, step1 = Algo.partition(start, end, array)
            step2 = Algo.quick_sort(start, p - 1, array)
            step3 = Algo.quick_sort(p + 1, end, array)
            total = step1 + step2 + step3
            return total
        else:
            return 0


    @staticmethod
    def stable_sort(l1, digit):
        steps = 0

        freq = [0 for _ in range(10)]
        steps += 10
        res = [0 for _ in range(len(l1))]
        steps += len(l1)

        for elem in l1:
            element = (elem // digit) % 10
            freq[element] += 1
            steps += 3

        for i in range(1, 10):
            freq[i] += freq[i - 1]
            steps += 2

        x = len(l1) - 1
        while x >= 0:
            element = (l1[x] // digit) % 10
            res[freq[element] - 1] = l1[x]
            freq[element] -= 1
            x -= 1
            steps += 5

        return res, steps

    @staticmethod
    def radix_sort(array):
        steps = 0
        max_number = max(array)
        digit = 1

        while max_number // digit > 0:
            a = Algo.stable_sort(array, digit)
            array = a[0]
            steps += a[1] + 3
            digit *= 10

        return array, steps

    @staticmethod
    def heapify(arr, n, i):
        count = 0
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
        count += 3
        if l < n and arr[largest] < arr[l]:
            largest = l
            count += 1
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
            count += 1
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            count += 3
            # Heapify the root.
            count += Algo.heapify(arr, n, largest)
        return count

    @staticmethod
    def heap_sort(arr2):
        count = 0
        arr = arr2
        n = len(arr)
        count += 2
        # Build a maxheap.
        for i in range(n // 2 - 1, -1, -1):
            count += Algo.heapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            count += 3
            count += Algo.heapify(arr, i, 0)
        return arr, count

    @staticmethod
    def maximum(array):
        max_val = max(array)
        min_val = min(array)
        if max_val < abs(min_val):
            return abs(min_val)
        else:
            return max_val

    @staticmethod
    def counting_sort_neg(array2):
        array = array2
        count = 0
        max_val = Algo.maximum(array)
        count += 3
        counting_list = [0 for _ in range(2 * max_val + 1)]
        count += 2 * max_val + 1
        temp_list = [0 for _ in range(len(array))]
        count += len(array)
        for i in range(0, len(array)):
            counting_list[array[i] + max_val] += 1
            count += 1

        for i in range(1, len(counting_list)):
            counting_list[i] += counting_list[i - 1]
            count +=1

        for i in range(len(array) - 1, -1, -1):
            temp_list[counting_list[array[i] + max_val] - 1] = array[i]
            counting_list[array[i] + max_val] -= 1
            count += 1

        for i in range(0, len(array)):
            array[i] = temp_list[i]
            count += 1
        return array, count

    @staticmethod
    def key(number, digit):
        weight = pow(10, digit)
        return (abs(number) % weight) // (weight // 10)

    @staticmethod
    def radix_digits(number):
        number_of_digits = 0
        while number != 0:
            number_of_digits += 1
            number /= 10
        return number_of_digits

    @staticmethod
    def radix_sort_neg(array):
        count = 0
        max_val = Algo.maximum(array)
        digits = Algo.radix_digits(max_val)
        count += 6

        for j in range(1, digits + 1):
            counting_list = [0 for _ in range(10)]
            count += 10
            temp_list = [0 for _ in range(len(array))]
            count += len(array)

            for i in range(0, len(array)):
                counting_list[Algo.key(array[i], j)] += 1
                count += 2

            for i in range(1, len(counting_list)):
                counting_list[i] += counting_list[i - 1]
                count += 1

            for i in range(len(array) - 1, -1, -1):
                temp_list[counting_list[Algo.key(array[i], j)] - 1] = array[i]
                count += 4
                counting_list[Algo.key(array[i], j)] -= 1
                count += 4

            for i in range(0, len(array)):
                array[i] = temp_list[i]
                count += 1

        start = 0
        end = len(array) - 1
        count += 2
        temp_list = [0 for _ in range(len(array))]
        count += len(array)
        for i in range(len(array) - 1, -1, -1):
            if array[i] < 0:
                temp_list[start] = array[i]
                start += 1
                count += 2

            elif array[i] > 0:
                temp_list[end] = array[i]
                end -= 1
                count += 2

        for i in range(0, len(array)):
            array[i] = temp_list[i]
            count += 1

        return array, count
