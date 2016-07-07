% The Theory of Computation
# The Theory of Computation #

The Church-Turing Hypothesis states that any algorithm can be expressed on a Turing machine, a hypothetical device that manipulates data on an infinite memory tape using a set of rules. More importantly, if a problem can be proven to be unsolvable on a Turing machine, no computer could ever solve it. One example of this is the Halting Problem - Can a machine, given a program and some input, determine whether the program will eventually stop or stay in an infinite loop?

Alan Turing used the Turing machine to prove that any algorithm that claims to solve this problem will contradict itself. The Turing Machine forms the basis of the idea of computation as a mathematical concept, and reveals a deep underlying truth about computation as a whole. Regardless of how fast computers become, no computer will ever be able to solve this problem for all cases.

When people think of computers, they often think of laptops or smartphones. As a computer scientist, it is important to remember that a computer is any device that performs computations - it doesn't need a screen or a keyboard or internet access. We will examine this idea in more depth when we talk about computer organization.

## Big O Notation ##

What makes a computer science problem hard for a computer to solve? We can use Big O notation to discuss how difficult a problem is to solve. The idea is that we look at how the time (or some other resource, like memory) increases compared to input size. If it takes twice as long to solve a problem when the input size is doubled, then that problem can be solved in linear time, or O(n). Big O notation is only a general estimate, allowing different algorithms to be compared without worrying about the details of the computer they are being run on. Here are some examples:

Time Complexity | Name | Example Problem
----------------|------|-----------------
O(1) | Constant-time | Accessing a variable in memory
O(log n) | Logarithmic time | Searching through a sorted array
O(n) | Linear time | Finding the biggest value in an unsorted array
O(n log n) | Linearithmic time | Sorting an array of values
O(n^2) | Quadratic time | Bubble sort (explained below)
O(n!) | Factorial time | Solving a problem by trying all possibilities

The big idea here is that it doesn't matter if you have a very fast computer. If you have an quadratic-time algorithm, every time you double your computational power, you get diminishing returns on the size of problems you can solve. Instead of focusing on the new shiny hardware being released every few months, studying computational complexity lets us see the bigger picture.

Quantum computers let us solve some types of problems faster. For example, Shor's algorithm can be used to factor a large number in polynomial time on a quantum computer. On a classical computer, the fastest this can be done is in sub-exponential (between polynomial and exponential) time. This is important because modern cryptography is based on the assumption that some problems are inherently hard for classical computers to solve.

## Example - Searching ##

Binary Search vs Linear Search

## Example - Sorting ##

Quicksort vs Insertion Sort

## Challenge ##

Can you think of a way to sort a deck of cards in time directly proportional to the number of cards (O(n))? Hint - As is often the case in Computer Science, you must trade one kind of performance for another. Think for a bit before looking at the solution.

## Solution ##

Radix sort

## Project ##

Brainfuck interpreter, describe turing completeness

## Takeaways ##

One of the most profound things that I've ever learned is the universal theory of computation. Programming languages change, new libraries and technologies gain traction, and new shiny hardware comes out, but the big ideas in Computer Science will always be the same. Until next time, Happy Coding!
