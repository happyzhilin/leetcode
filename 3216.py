"""
3216. 交换后字典序最小的字符串
简单
相关标签
相关企业
提示
给你一个仅由数字组成的字符串 s，在最多交换一次 相邻 且具有相同 奇偶性 的数字后，返回可以得到的
字典序最小的字符串
。

如果两个数字都是奇数或都是偶数，则它们具有相同的奇偶性。例如，5 和 9、2 和 4 奇偶性相同，而 6 和 9 奇偶性不同。



示例 1：

输入： s = "45320"

输出： "43520"

解释：

s[1] == '5' 和 s[2] == '3' 都具有相同的奇偶性，交换它们可以得到字典序最小的字符串。

示例 2：

输入： s = "001"

输出： "001"

解释：

无需进行交换，因为 s 已经是字典序最小的。



提示：

2 <= s.length <= 100
s 仅由数字组成。
"""


class Solution:
    def getSmallestString(self, s: str) -> str:
        number_list = list()
        for i in s:
            number_list.append(int(i))
        for i in range(len(number_list)-1):
            if number_list[i] % 2 == number_list[i+1] % 2 and number_list[i] > number_list[i+1]:
                number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
                break

        result_str = str()
        for value in number_list:
            result_str += str(value)

        return result_str


if __name__ == '__main__':
    s = Solution()
