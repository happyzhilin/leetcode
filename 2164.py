"""
2164. 对奇偶下标分别排序
简单
相关标签
相关企业
提示
给你一个下标从 0 开始的整数数组 nums 。根据下述规则重排 nums 中的值：

按 非递增 顺序排列 nums 奇数下标 上的所有值。
举个例子，如果排序前 nums = [4,1,2,3] ，对奇数下标的值排序后变为 [4,3,2,1] 。奇数下标 1 和 3 的值按照非递增顺序重排。
按 非递减 顺序排列 nums 偶数下标 上的所有值。
举个例子，如果排序前 nums = [4,1,2,3] ，对偶数下标的值排序后变为 [2,1,4,3] 。偶数下标 0 和 2 的值按照非递减顺序重排。
返回重排 nums 的值之后形成的数组。



示例 1：

输入：nums = [4,1,2,3]
输出：[2,3,4,1]
解释：
首先，按非递增顺序重排奇数下标（1 和 3）的值。
所以，nums 从 [4,1,2,3] 变为 [4,3,2,1] 。
然后，按非递减顺序重排偶数下标（0 和 2）的值。
所以，nums 从 [4,1,2,3] 变为 [2,3,4,1] 。
因此，重排之后形成的数组是 [2,3,4,1] 。
示例 2：

输入：nums = [2,1]
输出：[2,1]
解释：
由于只有一个奇数下标和一个偶数下标，所以不会发生重排。
形成的结果数组是 [2,1] ，和初始数组一样。


提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_list = list()
        even_list = list()
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)
        odd_list.sort(reverse=True)
        even_list.sort()
        result_list = list()
        for i in range(len(odd_list)):
            result_list.append(even_list[i])
            result_list.append(odd_list[i])
        if len(even_list) != len(odd_list):
            result_list.append(even_list[-1])
        return result_list


if __name__ == '__main__':
    s = Solution()
    print(s.sortEvenOdd([4, 1, 2, 3]))
    print(s.sortEvenOdd([2, 1]))
    print(s.sortEvenOdd([2, 1, 3]))
    print(s.sortEvenOdd([5, 39, 33, 5, 12, 27, 20, 45, 14, 25, 32, 33, 30, 30, 9, 14, 44, 15, 21]))
