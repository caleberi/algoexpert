package main

import "math"

type BST struct {
	Value int

	Left  *BST
	Right *BST
}

func walkTree(tree *BST, closestValueSoFar float64, distanceSoFar float64, target int) int {
	if tree == nil {
		return int(closestValueSoFar)
	}

	currentDistance := math.Abs(float64(tree.Value - target))

	if currentDistance < distanceSoFar {
		closestValueSoFar = float64(tree.Value)
		distanceSoFar = currentDistance
	}

	if target < tree.Value {
		return walkTree(tree.Left, closestValueSoFar, distanceSoFar, target)
	} else {
		return walkTree(tree.Right, closestValueSoFar, distanceSoFar, target)
	}

}

func (tree *BST) FindClosestValueV1(target int) int {
	if tree == nil {
		return -1
	}

	closestValueSoFar := float64(tree.Value)
	distanceSoFar := 1000000.0
	return walkTree(tree, closestValueSoFar, distanceSoFar, target)
}

func absdiff(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func (tree *BST) FindClosestValue(target int) int {
	return tree.findClosestValue(target, tree.Value)
}

func (tree *BST) findClosestValue(target, closest int) int {
	if absdiff(target, closest) > absdiff(target, tree.Value) {
		closest = tree.Value
	}

	if target < tree.Value && tree.Left != nil {
		return tree.Left.findClosestValue(target, closest)
	} else if target > tree.Value && tree.Right != nil {
		return tree.Right.findClosestValue(target, closest)
	}
	return closest
}

func (tree *BST) findClosestValueV3(target, closest int) int {
	currentNode := tree

	for currentNode != nil {
		if absdiff(target, closest) > absdiff(target, currentNode.Value) {
			closest = currentNode.Value
		}

		if target < currentNode.Value {
			currentNode = currentNode.Left
		} else if target > currentNode.Value {
			currentNode = currentNode.Right
		} else {
			break
		}
	}

	return closest
}
