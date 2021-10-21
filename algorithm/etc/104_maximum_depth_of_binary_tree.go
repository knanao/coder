package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	q := []*TreeNode{root}
	depth := 1
	start, end := 0, 1
	for {
		child := 0
		for i := 0; start < end; i++ {
			node := q[i]
			if node.Left != nil {
				q = append(q, node.Left)
				child++
			}
			if node.Right != nil {
				q = append(q, node.Right)
				child++
			}
		}
		if child == 0 {
			break
		}
		depth++
		start = end
		end += child
	}
	return depth
}
