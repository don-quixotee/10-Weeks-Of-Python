class Author:

    authorList = []
    
    def __init__(self, first_name, last_name, email,profession,password ):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.profession = profession
        Author.authorList.append(self)





    def display(self):
        for x in Author.authorList:
            print(x)
    


    

#     print( "Author {} :  ".format(i+1) ,x.firstName, x.lastName, x.email, x.profession, x.password)
