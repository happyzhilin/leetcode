"""
2760. 最长奇偶子数组
简单
相关标签
相关企业
提示
给你一个下标从 0 开始的整数数组 nums 和一个整数 threshold 。

请你从 nums 的子数组中找出以下标 l 开头、下标 r 结尾 (0 <= l <= r < nums.length) 且满足以下条件的 最长子数组 ：

nums[l] % 2 == 0
对于范围 [l, r - 1] 内的所有下标 i ，nums[i] % 2 != nums[i + 1] % 2
对于范围 [l, r] 内的所有下标 i ，nums[i] <= threshold
以整数形式返回满足题目要求的最长子数组的长度。

注意：子数组 是数组中的一个连续非空元素序列。



示例 1：

输入：nums = [3,2,5,4], threshold = 5
输出：3
解释：在这个示例中，我们选择从 l = 1 开始、到 r = 3 结束的子数组 => [2,5,4] ，满足上述条件。
因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。
示例 2：

输入：nums = [1,2], threshold = 2
输出：1
解释：
在这个示例中，我们选择从 l = 1 开始、到 r = 1 结束的子数组 => [2] 。
该子数组满足上述全部条件。可以证明 1 是满足题目要求的最大长度。
示例 3：

输入：nums = [2,3,4,5], threshold = 4
输出：3
解释：
在这个示例中，我们选择从 l = 0 开始、到 r = 2 结束的子数组 => [2,3,4] 。
该子数组满足上述全部条件。
因此，答案就是这个子数组的长度 3 。可以证明 3 是满足题目要求的最大长度。


提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= threshold <= 100
"""
from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        """
        :param nums: 传入的列表
        :param threshold: 子列表中的最大值
        :return: 子列表最大长度
        """
        # 求子列表的最大长度，要求是第一个元素是偶数，并且一个偶数交替一个奇数交替，并且了列表所有元素都小于等于传入的整数
        max_len = 0
        sub_list = list()
        for value in nums:
            if value > threshold:
                # 当出现大于传入整数时，求子列表最大长度然后创建新的子列表
                max_len = max(max_len, len(sub_list))
                sub_list = list()
                continue
            if not sub_list and value % 2 == 0:
                # 子列表是空列表并且遍历元素是偶数时，加入第一个子列表元素
                sub_list.append(value)
            elif len(sub_list) == 1 and value % 2 == 0:
                # 当子列表只有一个元素时且新增元素也是偶数，将其替换
                sub_list[0] = value
            elif sub_list and value % 2 != sub_list[-1] % 2:
                # 如果和子列表最后一个元素的奇偶性不同，则将遍历的元素加入子列表
                sub_list.append(value)
            else:
                # 执行到这里说明遍历的元素的与子列表最后一个元素的奇偶性相同
                # 遍历元素是奇数则创建新的子列表，是偶数则将该元素加入新的子列表中
                max_len = max(max_len, len(sub_list))
                sub_list = list()
                if value % 2 == 0:
                    sub_list.append(value)
        # 每次新建子列表时都求一次最大长度，最后一个子列表也可能是最大的
        max_len = max(max_len, len(sub_list))
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.longestAlternatingSubarray([3, 2, 5, 4], 5))
    print(s.longestAlternatingSubarray([1, 2], 2))
    print(s.longestAlternatingSubarray([2, 3, 4, 5], 4))
    print(s.longestAlternatingSubarray([4], 1))
    print(s.longestAlternatingSubarray([2, 2], 18))
    print(s.longestAlternatingSubarray([1], 1))
    print(s.longestAlternatingSubarray([1, 2], 2))
    print(s.longestAlternatingSubarray([2, 7], 9))
    print(s.longestAlternatingSubarray([8, 4], 6))
    print(s.longestAlternatingSubarray([4, 10, 3], 10))
    print(s.longestAlternatingSubarray([2, 3, 3, 10], 18))
    print(s.longestAlternatingSubarray([4, 10, 3], 10))
    print(s.longestAlternatingSubarray([4, 10, 3, 8, 4, 5, 4, 1], 16))
