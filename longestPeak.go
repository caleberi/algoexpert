package main

import (
	"math"
)

func LongestPeak(array []int) int {
	if len(array) <= 2 { //  we need at least 3 element to form a peak
		return 0
	}

	longestPeakSoFar := 0.0
	for currentIdx := 1; currentIdx < len(array)-1; currentIdx++ {
		leftIdx := currentIdx  //  to calculate the left end of the mountain
		rightIdx := currentIdx //  to calculate the right end of the mountain

		isPeak := false
		if array[leftIdx-1] < array[currentIdx] && array[rightIdx+1] < array[currentIdx] {
			isPeak = true
		}
		if !isPeak {
			continue
		}
		for leftIdx > 0 {
			if array[leftIdx-1] >= array[leftIdx] {
				break
			}
			leftIdx -= 1
		}

		for rightIdx < len(array)-1 {
			if array[rightIdx] <= array[rightIdx+1] {
				break
			}
			rightIdx += 1
		}

		// ignore half peak mountain
		if leftIdx == currentIdx || rightIdx == currentIdx {
			continue
		}
		//  to calculate the length end of the mountain
		longestPeakSoFar = math.Max(longestPeakSoFar, float64((rightIdx-leftIdx)+1))

	}

	return int(longestPeakSoFar)
}
