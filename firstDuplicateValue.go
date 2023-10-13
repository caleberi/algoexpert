package main

func FirstDuplicateValue(array []int) int {
	n := len(array)
	record := make([]int, n)
	for _, v := range array {
		key := v % n
		record[key]++
		if record[key] > 1 {
			return v
		}
	}
	return -1
}
