% First Project
# Our First Project - RPN Calculator #

Let's start off with a small project to get you caught up. We will be building a simple reverse-polish-notation calculator, demonstrating how we can move from requirements to a solution. This example will be in Java, but you can follow along in any imperative programming language. If you don't understand anything, look it up. I will try to give you tips to help you with your research.

## What is Reverse Polish Notation?

Reverse Polish Notation is a way of specifying mathematical expressions without using brackets. It was commonly used during the 70s on calculators.

![RPN Calculator - [more](https://www.youtube.com/watch?v=feddLrXonpQ)](images/01/rpn.jpg)

Numbers are pushed to a stack in order from left to right. Imagine each number like a plate on top of a stack of dishes. Whenever an operator is encountered, it takes its operands off the top of the stack and pushes the result. Here are a few example calculations

~~~
3 4 +
>7

5 4 3 * +
>17

6 3 /
>2

5 10 * 6 + 4 /
>14

5 10 * 6
> 50, 6
~~~

Our program will take output produce output like above. It will take an expression as input, and output the current stack.

## What is a Stack?

A stack is a very common data structure in Computer Science. There are two common ways a stack can be implemented - using an array or a linked list.

TODO Image

TODO discuss stacks, linked lists, arrays

For our RPN Calculator, we will use the built-in stack implementation for our language (`java.util.Stack` in Java) to avoid duplicated effort. This is generally a good idea when programming - be lazy.

## How will we organize our program?

The goal of this example is to give you experience breaking apart a problem into smaller problems. Our program will have a few main parts. It will need to:

- Loop to read user input
- Split up the input into tokens (i.e `5 10+` would become `[5, 10, +]`) - notice how a space isn't necessary between tokens.
- Implement the four basic operations - `+, -, *, /`
- Output the stack to the screen

Try this yourself before looking at my solution. If you get stuck, here are some hints.

## Finding tokens

My suggestion would be to loop over every character in the input. If it is an operator, add it as a separate token. Otherwise, append it to the current token.

## Processing tokens

Be careful! Order matters for subtraction and division. `10 5 -` is 5, not -5. Remember that items at the top of the stack were added last (First In, First Out).

## My Solution

Here is my first implementation. I can't stress enough how important it is for you to try this yourself first.

<pre><code class="ext-code java" data-src="examples/01/src/RPN.java">Downloading Code Example...</code></pre>

Let's see how we can make it cleaner. 
 
TODO

## What did we learn?

Always remember that there is room for improvement. Until next time, Happy Coding!

