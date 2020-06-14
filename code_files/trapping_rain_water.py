class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        res = 0
        local_max = []
        flag = True

        for i in range(len(height)):
            if (i == len(height) - 1 or height[i] > height[i + 1]) and flag:
                local_max.append(i)
                flag = False

            if i == len(height) - 1 or height[i + 1] > height[i]:
                flag = True
        if len(local_max) < 2:
            return 0

        meta_local_max = []
        flag = True
        for i in range(len(local_max)):
            if (i == len(local_max) - 1 or height[local_max[i]] >= height[local_max[i + 1]]) and flag:
                meta_local_max.append(i)
                flag = False

            if i == len(local_max) - 1 or height[local_max[i + 1]] >= height[local_max[i]]:
                flag = True
        idx = 0
        print(local_max, meta_local_max)
        for i in range(1, len(local_max)):
            if len(meta_local_max) < 2 or i in meta_local_max or i < meta_local_max[0] or i > meta_local_max[-1]:
                min_height = min(height[local_max[idx]], height[local_max[i]])
                res += min_height * (local_max[i] - local_max[idx] - 1) - sum([min(min_height, x) for x in height[local_max[idx] + 1:local_max[i]]])
                idx = i
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        lm = 0
        rm = 0
        i = 0
        j = len(height) - 1
        res = 0

        while i < j:
            lm = max(lm, height[i])
            rm = max(rm, height[j])
            if lm <= rm:
                res += lm - height[i]
                i += 1
            else:
                res += rm - height[j]
                j -= 1
        return res