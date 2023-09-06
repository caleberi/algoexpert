package main

import (
	"sort"
)

func ThreeNumberSum(array []int, target int) [][]int {
	results := make([][]int, 0)

	sort.Ints(array) // sort the array in increasing order

	for kPointer := 0; kPointer < len(array)-2; kPointer++ {

		// pick a number in the array at index kPointer + 1 let this be y
		lPointer := kPointer + 1
		// pick a number in the array at index len(array) - 1 let this be z
		rPointer := len(array) - 1

		//  pick a number in the array  let this be x
		curr := array[kPointer]
		for lPointer < rPointer {
			// calculate the total sum of all three numbers
			sumTotal := array[lPointer] + array[rPointer] + curr

			// determine which pointer element will get us closer to the target
			if sumTotal < target {
				lPointer += 1
			} else if sumTotal > target {
				rPointer -= 1
			} else {
				results = append(results, []int{curr, array[lPointer], array[rPointer]})
				lPointer += 1
				rPointer -= 1
			}
		}
	}
	return results
}

// Brute Force Method
// Time Complexity Analysis  - O(N^3)
// Space Complexity Analysis - O(N)+O(M*3(N)) -> O(M*N)
func ThreeNumberSumBruteForce(array []int, target int) [][]int {
	result := make([][]int, 0)

	sort.Ints(array) // sort the array in increasing order

	for i := 0; i < len(array)-2; i++ {
		for j := i + 1; j < len(array)-1; j++ {
			for k := j + 1; k < len(array); k++ {
				sum := array[i] + array[j] + array[k]
				if sum == target {
					result = append(result, []int{array[i], array[j], array[k]})
				}
			}
		}
	}

	return result
}
