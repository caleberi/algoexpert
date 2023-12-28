package main

import "math"

func (tree *BST) ValidateBst() bool {
	return tree.validateBstTree(math.MinInt, math.MaxInt)
}

func (tree *BST) isLeaf() bool {
	return tree.Left == nil && tree.Right == nil
}

func (tree *BST) validateBstTree(minVal, maxValue int) bool {

	if tree == nil {
		return true
	}

	if tree.Value < minVal || tree.Value >= maxValue {
		return false
	}

	if tree.Left != nil && !tree.Left.validateBstTree(minVal, tree.Value) {
		return false
	}

	if tree.Right != nil && !tree.Right.validateBstTree(tree.Value, maxValue) {
		return false
	}
	return true
}
