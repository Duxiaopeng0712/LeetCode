import numpy as np


def findMedianSortedArrays(nums1, nums2):
    return np.median(np.array(nums1 + nums2))
