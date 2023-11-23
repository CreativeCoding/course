Setup
=====

Using an IDE
--------------

An IDE is an integrated development environment. It is a software application that helps programmers
develop software code efficiently. There are many to choose from e.g. Microsoft Visual Code, Pycharm, IDLE.
It is advised to download one and use it for your code development.

Alternatively, you could edit your code in Textedit, Notepad or BBEdit which
come packaged with your OS, and then run your code in a Terminal.


Using GitHub
------------
We recommend that you get a GitHub account and use the Git for code sharing and storage. This might need installing in your system.


    | Here is a good tutorial https://www.freecodecamp.org/news/introduction-to-git-and-github/


Using Terminal & Bash
---------------------
Bash is a command processor that typically runs in a text window where the user types commands that cause actions. It is
crucial to understand how Bash works and how to navigate the computer using Bash commands.

On UNIX systems Bash runs in a Terminal window, in Windows it runs in Command Prompt or PowerShell. However, some of
the language differs between Terminal Bash, Command Prompt and PowerShell.

    | A great way to get familiar with Bash is to play the game BashCrawler https://gitlab.com/slackermedia/bashcrawl


Help and problem solving
-------------------------

Creative coding will mostly involve debugging, problem solving, optimising and trawling the internet for help suggestions.
This is normal, and a great way to learn and advance your coding creativity. Even experienced developers will spend 90%
of their coding time debugging, trawling stack overflow, and experimenting with different solutions.

There are several ways to help you problem-solve:

1. Use the error handling reports in the python console.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python will tell you what is wrong. For example::

    Traceback (most recent call last):
        File "C:/Users/Owner.OWNER-PC/AppData/Local/Programs/Python/Python37-32/lab 5 maybe.py", line 41, in <module>
        main()
        File "C:/Users/Owner.OWNER-PC/AppData/Local/Programs/Python/Python37-32/lab 5 maybe.py", line 8, in main
        rand_gen(myfile)
        File "C:/Users/Owner.OWNER-PC/AppData/Local/Programs/Python/Python37-32/lab 5 maybe.py", line 19, in rand_gen
        my_file.write(line +'\n')
        TypeError: unsupported operand type(s) for +: 'int' and 'str'

In this error the final line is the actual error that needs to be dealt with. In this case there is a type error in a command.

2. look through the module's API in your IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Modules and Libraries that we will be using have comprehensive and well documented API's and DocStrings. In your IDE
if you hover over a function it should explain the format of a command.

3. use the module's API online
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Modules and Libraries that we will be using have comprehensive and well documented websites.

4. look through Stack Overflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stack Overflow is a question-and-answer website for programmers. It contains billions of questions and answers related to
many programming languages. It has been helping programmers since 2008. Beware ... some of the answers may be incorrect;
or old, or both.

For example, when I put the final line of the above error (TypeError: unsupported operand type(s) for +: 'int' and 'str')
into stack overflow the following answer was one listed. https://stackoverflow.com/questions/53550165/how-to-fix-typeerror

The answers are credible and will work in Python BUT ... the thread was from 2018, and the answers only have a few
positive responses (in bold next to each suggestion). My advice would be to find a newer and better supported thread
on the same issue.

5. ChatGPT
^^^^^^^^^^
Well it's not going away, and it is very clever. But generally wont help you become more creative. You are better off
enjoying your trawls through stack overflow and the API's: you will learn so much more.

6. Dont ask an instructor unless ...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This is the LAST option. And be prepared for the instructor to ask you to walk them through the first 5 help steps.
Coding is a creative language in itself. To be expressive in your coding - and therefore to be expressive in your creative
coding - requires you to make mistakes and hunt for solutions. Along the way you will be presented with options. This is all
a crucial part of your journey.

Pseudocode and FlowCharts
-------------------------
Before you commit to writing your *script* in Python, it is very helpful to outline the system design of your *algorithms*.
There are 2 methods that you might find helpful:

Pseudocode
^^^^^^^^^^
Pseudocode is an algorithm written in an informal way using everyday language in basic terms. The aim is to outline and highlight
the flow of data, key functions and core systems. For example::

    set time to 0
    Repeat until time is greater than 5 minutes
        choose a sample from the bank
        choose a random start point
        choose a random end point in remaining lenbgth of sample
        choose a random playback speed
        play the sample
        add modified sample length to time

Flowcharts
^^^^^^^^^^
Flowcharts are algorithms written in a visual format. The above pseudocode will look like this:


Fundamentals
------------
There are two fundamental coding concepts that are essential to understand before we move forward:

1. Threading (I/O concurrency)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Threading enables concurrent processes (or the illusion of concurrency) in your code. For example analysing the sound input
from the laptop's microphone AND displaying notes on a screen. Through this course we will use 4 libraries that support concurrency:

+ *trio* https://trio.readthedocs.io/en/stable/
+ *asyncio* https://docs.python.org/3/library/asyncio.html
+ *concurrent.futures* https://docs.python.org/3/library/concurrent.futures.html
+ *threading* https://docs.python.org/3/library/threading.html

2. Object-oriented programming (OOP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Object-oriented programming (OOP) is a computer programming model that organizes software design around data, or objects,
rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.

    | Further info https://www.w3schools.com/python/python_classes.asp


