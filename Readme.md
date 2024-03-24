# Bash Scripting

Bash Scripting is a powerful part of system administration and development used at an extreme level. It is used by the System Administrators, Network Engineers, Developers, Scientists, and everyone who use Linux/Unix operating system. They use Bash for **system administration, data crunching, web application deployment, automated backups, creating custom scripts for various pages,** etc.

**Script**

In Computer programming, a script is a set of commands for an appropriate run time environment which is used to automate the execution of tasks.

# Bash Script:

A Bash Shell Script is a plain text file containing a set of various commands that we usually type in the command line. It is used to automate repetitive tasks on Linux filesystem. It might include a set of commands, or a single command, or it might contain the hallmarks of imperative programming like loops, functions, conditional constructs, etc. Effectively, a **Bash script is a computer program written in the Bash programming language.**

# History of Bash

- Previously, most of the software in the UNIX world was proprietary and closed source. UNIX system was also not open-sourced for which, you had to use a shell. There was a shell existed at that time named by "Bourne Shell" under the /bin/sh command which was proprietary and closed source. Bourne named after its inventor- Steven Bourne.
- Richard Stallman at that time began GNU project with Free Software Foundation (FSF) to create a UNIX-compatible operating system aiming everything as open-source. There was a lack of progress in the revolution. He needed a free shell that could run existing shell scripts. It was imperative to a completely open-source system built as one of the few projects he funded with FSF. Then on January 110, 1988, Brian Fox (FSF employee) began coding on Bash and released Bash as beta, version 0.99 on June 8, 1989.
- Brian Fox remained in FSF as the primary Bash maintainer till 1993. Then he laid off from FSF, and Chet Ramey (earlier contributor in FSF) got his responsibility.
- Further, on December 23, 1996, Chet Ramey released another bash version 2.0 for the public with a range of new features over the old bash version.
- And now Chet Ramey is known for the official bash maintainer, and he continues to make further enhancements in bash.

Bash is the standard shell included with Linux. It is the most popular shell known today of being open-source and also with various productive features we read in the further topic. It is available for Linux distributions, macOS, Solaris 11, and Windows 10 too. It is offering the best experience for its users with a lot of improvements.

# Filesystem and File Permissions

The **Filesystem** is a kind of structure organized with the collection of files or folders. It determines control over data, i.e., how data is to be stored and retrieved?

Linux Filesystem is a tree-like structure comprised of lots of directories. These directories are just the files containing the list of other files. Linux makes no difference between the files and directories. All the files in Linux filesystem are known as directories, and these files are categorized as follows:

1. ***Ordinary files*** that contain data, text, images, program instructions.
2. ***Special files*** that give access to hardware devices.
3. ***Directories*** that contain both the ordinary and special files.

Let's have a look on Linux filesystem.

List all the files and directories by using ls -l command.

- The ***first column*** represents the file type and file permissions. Every file row begins with the file type and then specifies the access permissions associated with the files. These are the following types of files with their specific characters:
    1. Regular file (-)
    2. Directory (d)
    3. Link (l)
    4. Special File (c)
    5. Socket (s)
    6. Named pipe (p)
    7. Block device (b)
- The ***second column*** represents the number of memory blocks.
- The ***third column*** represents the owner of the file or the superuser, who has the administrating power.
- The ***fourth column*** represents the group of owner/superuser.
- The ***fifth column*** represents the file size.
- The ***sixth column*** represents the date and time when the file was created or lastly modified.
- The ***last column*** represents the name of the file or the directory.

### Permissions

There are three types of permissions associated with the files as follows:

**Read (r)** permission by which you can view the content of the file.

**Write (w)** permission by which you can modify the file content.

**Execute (x)** permission by which one can run the programming file or script.

# What are Bash Variables?

We cannot use bash variables without having the proper information (**syntax, data types, types, working**) about it, so, let's go throughout this brief tutorial for having the appropriate overview of Bash Variables.

At first, know the syntax.

### Syntax:

1. Variable_name=value

## Rules Set for Defining Bash Variables:

1. Prefix the variable name with dollar ($) sign while reading or printing a variable.
2. Leave off the dollar sign ($) while setting a variable with any value.
3. A variable name may be alphanumeric, or it may be written with an underscore (_).
4. A variable name is case-sensitive: x and X are considered as two different variables.
5. variable name can be written either in UPPER_CASE or LOWER_CASE letters or mixture of both as you want.
6. A variable can be placed at anywhere in a Bash Script or on the command line, because on runtime, Bash will replace it with its assigned value. It became possible because of doing substitution before running the command.
7. There should not be whitespace on either side of the equal sign (=) between the variable name and its value. Following are some example of **Invalid Variables** having whitespaces (denoted by dots ...) between them as given below:var1=...variable1var2...=variable2var3...=...variable3
8. There is no need of using any quotes, either single or double, to define a variable with single character value such as **var1=variable**. To input multiple words or String as a single item in a variable, then make use of quotes for enclosing your content in that variable.
    - Single Quote ('') helps to treat every character.
    - Double Quote ("") helps to do the substitution.

# Bash Arithmetic Operators

In this topic, we will understand how to use arithmetic operators in Bash.

Depending on what type of result we want through our scripts, we may need to apply arithmetic operators at some point. Like variables, they are reasonably easy to apply. In the bash script, we can perform arithmetic operations on numeric values to get the desired result.

There are 11 arithmetic operators which are supported by Bash Shell.

Look at the following table demonstrating the syntax, description and examples for each of the arithmetic operators:

| Operator | Description | Examples |
| --- | --- | --- |
| + | Addition, measures addition of numbers (operands) | $(( 10 + 3 )), result=13 |
| - | Substraction, measures subtraction of second operand from first | $(( 10 - 3 )), result=7 |
| * | Multiplication, measures the multiplication of operands. | $(( 10 * 3 )), result=30 |
| / | Division, measures the division of first operand by second operand and and return quotient. | $(( 10 / 3 )), result=3 |
| ** | Exponentiation, measures the result of second operand raised to the power of first operand. | $((  10 ** 3 )), result=1000 |
| % | Modulo, measures remainder when the first operand is divided by second operand. | $(( 10 % 3 )), result=1 |
| += | Increment Variable by Constant- used to increment the value of first operand by the constant provided. | x=10
let "x += 3"
echo $x
result=13 |
| -= | Decrement Variable by Constant- used to decrement the value of first operand by the constant provided. | x=10
let "x -= 3"
echo $x
result=7 |
| *= | Multiply Variable by Constant- used to multiply the value of the first operand by the constant provided. | x=10
let "x *= 3"
echo $x
result=30 |
| /= | Divide Variable by Constant- used to calculate the value of (variable / constant) and store the result back to variable. | x=10
let "10 /= 3"
echo $x
result=3 |
| %= | Remainder of Dividing Variable by Constant- used to calculate the value of (variable % constant) and store the result back to variable. | x=10
let "10 %= 3"
echo $x
result=1 |

# Bash If

In this topic, we will understand how to use **if statements** in Bash scripts to get our automated tasks completed.

Bash if statements are beneficial. They are used to perform conditional tasks in the sequential flow of execution of statements. If statements usually allow us to make decisions in our Bash scripts. They help us to decide whether or not to run a piece of codes based upon the condition that we may set.

# Basic if Statements

A basic if statement commands that if a particular condition is true, then only execute a given set of actions. If it is not true, then do not execute those actions. If statement is based on the following format:

### Syntax

```bash
if [ expression ];
then
statements
fi
```

- For using multiple conditions with AND operator: