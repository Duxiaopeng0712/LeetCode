class Solution(object):
    def shipWithinDays(self, weights, D):
        l = max(weights)
        r = sum(weights)
        # [l, r)
        while l < r:
            mid = l + (r - l) / 2
            if self.getNeedDays(weights, mid) > D:
                l = mid + 1
            else:
                r = mid
        return l

    def getNeedDays(self, weights, x):
        need = 1
        cur = 0
        for w in weights:
            if cur + w > x:
                need += 1
                cur = 0
            cur += w
        return need
