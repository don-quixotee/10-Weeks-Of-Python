class Blog:
    def __init__(self):
        self.blogTitle=""
        self.blogText =""

    def writeAblog(self):
        print("Enter Blog Title: ")
        print()
        self.blogTitle = input()
        print()
        print("write you blog below")
        print()
        self.blogText = input()
        print("_________________________________________________")
    

    def displayBlog(self):
        return self.blogTitle, self.displayBlog


