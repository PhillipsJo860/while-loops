## Python While Loops: A Quick Guide

### **What is Iteration?**

Iterating means repeating a task over and over again. It's like washing a stack of plates, one plate at a time. Each time you wash a plate would be called an iteration.

In programming, each time a loop runs (loops) is known as an *iteration*.

### **What is a While Loop?**

A while loop is a control statement that allows you to **execute** (*run*) a block of code over and over again *as long as a certain condition is true*.

**Creating a While Loop:**

```python
while condition:
    # code to be executed
```

### **When to Use a While Loop vs. When to Use a For Loop**

* **For Loop:** Use when you know in advance how many times you want your loop to loop.  
  * Example: Iterating (looping) over the items in a Python list.
  * The for loop stops when it reaches the end of your Python list.
* **While Loop:** Use when you don't know in advance how many times you want your loop to run or when you want the loop to keep looping until a certain condition is met.  
  * Example: Prompting the user to enter a number (such as a temperature or a quiz score) until the user decides to quit the loop.

### **Example 1: Simple Counter**

```
count = 0 
while count < 5:
    print(count)  
    count += 1
```
In this example, we're *iterating* (looping) 5 times, and *incrementing* (increasing) the count variable by one each time the loop runs (iterates).

### **Example 2: User Input**

```python
user_input = ""
while user_input != "quit": # != means IS NOT EQUAL TO
    user_input = input("Enter a word (or 'quit' to exit): ") 
    print(user_input)
```

Here, we're iterating (looping) until the user enters "quit". The loop runs as long as the user's input is not the word "quit".

### **Flag Variables & While Loops**

A flag variable is a Boolean variable that can be used to control the execution of a while loop. When the flag is set to False, the loop *terminates* (quits or exits).

**Remember**:  A Boolean variable can only be set to `True` or `False`.

### **Example 3: Flag Variable**

```python
keep_going = True
while keep_going: 
    user_input = input("Enter a word (or 'quit' to exit): ").lower() # Convert input to lowercase
    if user_input == "quit": 
        keep_going = False  
    else: 
        print(user_input)
```

In this example, the `keep_going` flag is initially set to `True`. The loop continues as long as the flag is `True`. When the user enters "quit", the flag is set to `False`, and the loop terminates (quits).

### **The break Keyword**

The break keyword can be used to **immediately** exit a while loop, regardless of the loop's condition.

### **Example 4: Break Keyword**

```python
while True: 
    user_input = input("Enter a number: ") 
    if user_input == "quit": 
        break
    number = int(user_input) 
    print(number * 2)
```
Here, the loop is set to run infinitely (while True). However, if the user enters "quit", the break statement is executed, and the loop **immediately** terminates (quits).

**Remember:**

- Make sure the condition in your while loop will eventually become false, otherwise you'll create an infinite loop (a loop that never stops).
- Consider using for loops when you only have a small number of items to loop through (such as in a short Python list or tuple) or when you know **in advance** how many times you want your loop to loop (run).
