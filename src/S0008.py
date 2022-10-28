"""
请你来实现一个myAtoi(string s)函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231, 231− 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
注意：

本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        #是否排除了空格
        start = False
        #是否跳过了符号
        startNum = False
        positive = True
        for s_i in s:
            if not start and s_i == ' ':
                continue
            start = True
            if s_i in "-+" and not startNum:
                startNum = True
                if s_i == '-':
                    positive = not positive
                elif s_i == '+':
                    pass
            elif s_i in "1234567890":
                startNum = True
                result = result*10 + (ord(s_i) - ord('0'))
            else:
                break

        result = result * (1 if positive else -1)
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        elif result < - 2 ** 31:
            result = -2 ** 31
        return result


if __name__ == '__main__':
    # print(2 ** 31 - 1)
    # print(Solution().reverse(7463847412))
    # print(-2 ** 31)
    print(Solution().myAtoi("+-12"))
