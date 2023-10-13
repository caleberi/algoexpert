package main

func IsMonotonic(array []int) bool {
	// empty and array of one element are monotonic
	if len(array) <= 1 {
		return true
	}
	strictlyIncreasing := true
	strictlyDecreasing := true
	//  for an array to be monotonic
	//  it must either be strictly decreasing or increasing
	for i, j := 0, len(array)-1; i < len(array)-1 && j > 0; i, j = i+1, j-1 {
		strictlyDecreasing = strictlyDecreasing && (array[i] <= array[i+1])
		strictlyIncreasing = strictlyIncreasing && (array[j] <= array[j-1])
	}
	return strictlyIncreasing || strictlyDecreasing
}
