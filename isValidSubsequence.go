package main

import (
	"reflect"
)

func IsValidSubsequence(array []int, sequence []int) bool {
	if len(sequence) > len(array) {
		return false
	}
	ret := []int{}
	i, j := 0, 0
	for j < len(array) {
		if i < len(sequence) {
			if array[j] == sequence[i] {
				ret = append(ret, sequence[i])
				i++
			}
		}
		j++
	}
	return reflect.DeepEqual(sequence, ret)
}

func IsValidSubsequenceV2(array []int, sequence []int) bool {
	if len(sequence) > len(array) {
		return false
	}
	i, j := 0, 0
	for j < len(array) {
		if i < len(sequence) {
			if array[j] == sequence[i] {
				i++
			}
		}
		j++
	}
	return i == len(sequence)
}
