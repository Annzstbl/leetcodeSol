import math


class Solution:
    """
        将整数反转，需要在每步确认是否溢出了
        python int最小值为-2^31  最大值为2^31-1

    """

    def reverse(self, x: int) -> int:
        result = 0
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31
        while x != 0:
            res = x % 10 if x > 0 else x % -10
            x = int(x / 10)
            if 0 <= result <= int_max // 10 and int_max - 10 * result >= res:
                result = result * 10 + res
            elif 0 >= result >= int_min // 10 and int_min - 10 * result <= res:
                result = result * 10 + res
            else:
                return 0
        return result


if __name__ == '__main__':
    # print(2 ** 31 - 1)
    # print(Solution().reverse(7463847412))
    print(-2 ** 31)
    print(Solution().reverse(-7463848412))
