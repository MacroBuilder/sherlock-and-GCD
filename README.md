### sherlock-and-GCD
HackerRank -- Algorithms -- Warmup

##### Problem Statement

Sherlock is stuck while solving a problem: Given an array A={a1,a2,⋯,aN}, he wants to know if there exists a subset B of this array which follows these statements:

B is a non-empty subset.

There exists no integer x(x>1) which divides all elements of B.

There are no elements of B which are equal to another.

##### Input Format

The first line of input contains an integer, T, representing the number of test cases. Then T test cases follow. 
Each test case consists of two lines. The first line contains an integer, N, representing the size of array A. In the second line there are N space-separated integers, a1,a2,…,an, representing the elements of array A.

Constraints 

1≤T≤10 

1≤N≤100 

1≤ai≤105 ∀1≤i≤N

##### Output Format

Print YES if such a subset exists; otherwise, print NO.

##### Sample Input
```
3
3
1 2 3
2
2 4
3
5 5 5
```
##### Sample Output
```
YES
NO
NO
```
##### Explanation

In the first test case, {1},{2},{3},{1,2},{1,3},{2,3} and {1,2,3} are all the possible non-empty subsets, of which the first and the last four satisfy the given condition.

For the second test case, all possible subsets are {2},{4},{2,4}. For all of these subsets, x=2 divides each element. Therefore, no non-empty subset exists which satisfies the given condition.

For the third test case, the following subsets exist: S1={5},S2={5,5}, and S3={5,5,5}. Because the single element in the first subset is divisible by 5 and the other two subsets have elements that are equal to another, there is no subset that satisfies every condition.
