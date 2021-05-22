package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	ret := &TreeNode{}
	if root1 == nil {
		return root2
	}
	if root2 == nil {
		return root1
	}
	ret.Val = root1.Val + root2.Val
	ret.Left = mergeTrees(root1.Left, root2.Left)
	ret.Right = mergeTrees(root1.Right, root2.Right)
	return ret
}

func main() {
	root1 := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val:  3,
			Left: &TreeNode{Val: 5},
		},
		Right: &TreeNode{Val: 2},
	}
	root2 := &TreeNode{
		Val: 2,
		Left: &TreeNode{
			Val:   1,
			Right: &TreeNode{Val: 4},
		},
		Right: &TreeNode{
			Val:   3,
			Right: &TreeNode{Val: 7},
		},
	}
	out := mergeTrees(root1, root2)
	fmt.Printf("out: %v\n", out)
}
