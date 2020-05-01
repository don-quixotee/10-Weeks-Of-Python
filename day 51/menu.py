from blog import Blog
from author import Author
import sys


print("WELCOME TO MY BLOGGER")

choice = True
while True:

    print("__________________")
    print()
    print(""" please Enter:
                
                1. to write  blog
                2. to  display blog
                3. to quit

                """

                )

    n = int(input())
    if n == 1:
        blog = Blog()
        blog.writeAblog()
    elif n == 2:
        blog = Blog()
        print(blog.displayBlog())
    elif n == 3:
        sys.exit()
    else:
        print("please enter a valid choice")

    

