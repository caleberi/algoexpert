package main

func MinHeightBST(array []int) *BST {
	start := 0
	end := len(array) - 1
	return constructBSTWithMinHeight(array, start, end)
}

func constructBSTWithMinHeight(array []int, start, end int) *BST {
	if end < start {
		return nil
	}
	middle := (end + start) / 2
	node := &BST{Value: array[middle]}
	node.Left = constructBSTWithMinHeight(array, start, middle-1)
	node.Right = constructBSTWithMinHeight(array, middle+1, end)
	return node
}
