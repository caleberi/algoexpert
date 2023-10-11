package main

func MoveElementToEnd(array []int, toMove int) []int {
	i, j := 0, len(array)-1
	for i < j {
		if array[j] == toMove && array[i] == toMove {
			j -= 1
		} else if array[j] != toMove && array[i] == toMove {
			array[j], array[i] = array[i], array[j]
			j -= 1
			i += 1
		} else {
			i += 1
		}
	}
	return array
}
