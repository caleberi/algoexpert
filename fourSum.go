package main

func FourNumberSum(array []int, target int) [][]int {
	quadruplets := [][]int{}

	paritalSums := make(map[int][][]int)

	for i := 1; i < len(array)-2; i++ {
		for k := 0; k < i; k++ {
			currentSum := array[i] + array[k]
			paritalSums[currentSum] = append(paritalSums[currentSum], []int{array[i], array[k]})
		}
		for j := i + 2; j < len(array); j++ {
			currentSum := array[i+1] + array[j]
			diff := target - currentSum
			if pairs, found := paritalSums[diff]; found {
				for _, pair := range pairs {
					quadruplets = append(quadruplets, append(pair, array[i+1], array[j]))
				}
			}
		}
	}

	return quadruplets
}

func FourNumberSumV3(array []int, target int) [][]int {
	quadruplets := [][]int{}

	paritalSums := map[int][][]int{}

	for i := 0; i < len(array)-1; i++ {
		for j := i + 1; j < len(array); j++ {
			difference := target - (array[i] + array[j])
			values, found := paritalSums[difference]
			if found {
				for _, v := range values {
					quadruplets = append(quadruplets, []int{array[i], array[j], v[0], v[1]})
				}
			}
		}
		for j := i - 1; j >= 0; j-- {
			currentSum := array[i] + array[j]
			paritalSums[currentSum] = append(paritalSums[currentSum], []int{array[i], array[j]})
		}
	}

	return quadruplets
}
