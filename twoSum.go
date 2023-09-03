package main

import "sort"

func TwoNumberSum(array []int, target int) []int {
	result := []int{}
	hash := make(map[int]int)
	for _, curr := range array {
		difference := target - curr
		_, diffOk := hash[difference]
		_, currOk := hash[curr]
		if !diffOk && !currOk {
			hash[difference] = curr
		} else {
			result = append(result, curr, hash[curr])
		}
	}
	return result
}

func TwoNumberSumV3(array []int, target int) []int {
	result := []int{}
	hash := make(map[int]struct{})
	for _, curr := range array {
		difference := target - curr
		_, diffOk := hash[difference]
		if !diffOk {
			hash[curr] = struct{}{}
		} else {
			result = append(result, curr, difference)
		}
	}
	return result
}

func TwoNumberSumV2(array []int, target int) []int {
	for idx := 0; idx < len(array); idx++ {
		firstNum := array[idx]
		for idx2 := 0; idx2 < len(array); idx2++ {
			secondNum := array[idx2]
			if firstNum+secondNum == target {
				return []int{firstNum, secondNum}
			}
		}
	}
	return []int{}
}

func TwoNumberSumV4(array []int, target int) []int {
	leftPointer := 0
	rightPointer := len(array) - 1

	sort.Ints(array)

	for leftPointer < rightPointer {
		currentSum := array[leftPointer] + array[rightPointer]
		if currentSum > target {
			rightPointer -= 1
		} else if currentSum < target {
			leftPointer += 1
		} else {
			return []int{array[leftPointer], array[rightPointer]}
		}
	}
	return []int{}
}
