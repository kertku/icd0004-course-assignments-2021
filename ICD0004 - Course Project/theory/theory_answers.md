### 1. Which of the following activities cannot be automated
 ~~~
 Exploratory testing
 Discussing testability issues
 ~~~

### 2. How do we describe a good unit test?
~~~
 Fast, Repeatable, Self-validating, Timely, Isolated
~~~
### 3. When is it a good idea to use XPath selectors
~~~
 When CSS or other selectors are not an option or would be brittle and hard to maintain

 When we need to find an element based on parent/child/sibling relationship

 When an element is located deep within the HTML (or DOM) structure
 
 (All the above are correct answers.)
~~~

### 4. Describe the TDD process
~~~
TDD requires to have test first and then code to implement it. Create test - (Red). 
Implement the code to past the test - (Green). Then refactor the code and repeat.
~~~
### 5. Write 2 test cases or scenarios for a String Calculator application, which has a method calculate() that takes a string of two numbers separated by a comma as input, and returns the sum.
~~~
Given the input "4,6" When the method calculate() is called Then I should see 10 as result.
Given the input "4 6" When the method calculate() is called Then I should see "Error! Wrong input format" as a result.
~~~~