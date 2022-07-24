
#Assignments (SET - 1)
#1.Write a program to print each word of the line in a new line using both while and for loops.
#Input : Love All Serve All Help Ever Hurt Never
'''str=("Love","All","Serve","All","Help","Ever","Hurt","Never")
for i in str:
    print(i)    #Love  All  Serve  All  Help  Ever  Hurt  Never  

#2.Write a program to find the maximum, minimum, average, addition, multiplication of any 2 integer numbers (for example : 23 and 34)
a=23
b=34
c=(a,b)
maximum=max(c)
print("maximum is :",maximum)                 #maximum is : 34
minimum=min(c)
print("minimum is :",minimum)                 #minimum is : 23
addition=sum(c)
print("addition is :",addition)               #addition is : 57
d=addition/2
print("averege is :",d)                       #averege is : 28.5
multiplication=a*b
print("multiplication is :",multiplication)   #multiplication is : 782     '''

#3.Write a program to print all the elements within a list in the reverse order. The entire list has to be passed via command line arguments (Hint : use argv)

#4.Write a program to print all the alternative elements of a tuple. The elements to the tuple have to be given to the program using input() function.

'''#5.Write a program to print all the details of a student by storing all of his details in a dictionary by retrieveing the values from keys. Next, Print the entire dictionary. Next, print each and every key value pair seperately. Next, print only values (Don't print keys).
student_datails={"name":"Ramu","age":"20","group":"b.come","gender":"male","address":"palamaner"}
dic=student_datails
print(dic.keys())       #dict_keys(['name', 'age', 'group', 'gender', 'address'])
print(dic)              #{'name': 'Ramu', 'age': '20', 'group': 'b.come', 'gender': 'male', 'address': 'palamaner'}
print(dic.items())      #dict_items([('name', 'Ramu'), ('age', '20'), ('group', 'b.come'), ('gender', 'male'), ('address', 'palamaner')])
print(dic.values())     #dict_values(['Ramu', '20', 'b.come', 'male', 'palamaner'])   '''

#6.Write a program to pass a list as a command line arguments. Next, convert that list into a tuple after removing all the duplicate elements. (hint : use set) Next, add all the elements of that duplicate free tuple and print the addition output.

#7.Write a program to print this pattern (hint : use \t and \n wherever required).

         *
     * python *
   * is  *  a    *
 * good  * programming * language *
* to * learn * for * beginners *
#8.Write a program to create variables storing values for each datatype. print the object identities of all the created variables. Next, convert the types of the each varible into another type. After changing the type, store all the values of all the variables in a list. Finally, Print the list.

#9.Write a program that imports numpy, matplotlib, pandas libraries. If the program imports those modules successfully. print "modules imported successfully" (hint : research about these libraries in google. Find out the command of how to install those libraries. Understand the purpose and importance of these libraries).

#10.What is zen of python? Write a program to illustrate "zen of python"? (Hint : Search on google.)

#11.Very IMPORTANT! Please search in google whenever you are stuck. Even if you get an error (traceback). Search about that traceback on google. For every difficulty or uncertainity, don't forget to search on google.

Steps to submit:
Create a folder with name : submissionnumber_fullname_contributions
include all of your programs in that folder. Each program for each question.
then drag and drop the entire folder to your cloned repo
then raise a pull request.
#Assignments (SET-2)
#1.Write a program to print the add, subtract, divide, multiply, of the digits using functions. Add, subtract, divide, multiply functions should be created. For example, if the input is 235, the result should be 10. Next, Load the input number 235 from a text file input.txt. Next, Save the program output into a text file output.txt.
#2.Given a Full name stored in a input file input_name.txt which contains first name, middle name and last name. All the first, middle and last name are seperated by spaces. Print the output in the following order: Last Name, First Name, middle name. Next, Save the last name in last_name.txt file. Save the first name in first_name.txt. Save the middle name in middle_name.txt file.
#3.Write a program that accepts a positive integer n. Next, write a function to find factorial of the number. and next, write another function to compute the value of n+nn+nnn. If n is 5, first output should be 5! = 120 and the next output should be 5+55+555 = 615.
#4.Write a program to load, open and save an image. (hint : use opencv-python or PIL modules. Research about them on google and youtube)
#5.Given a list of numbers write a program to calculate the sum of odd and even numbers and print the same. Accept from the user the count of numbers and the actual numbers.
#6.Find out what is a timestamp? Print date and time in a timestamp. Print the seconds, hours, minutes as sepearate integer numbers from that timestamp. (hint : use datetime module. Search on google when stuck).
#7.Given a string print all the lowercase characters, upper case characters and numeric characters and their counts.
#8.Write a program to check if the input string is a palindrome? Next, Make the program to work on integers as well. Write a palindrome function. Call that function of 5 different inputs to test whether the function is written properly or not.

#9.Store student name, id, age, class, course in a dictionary. Write a script to lookup a student name, age, class, course given the student ids.
student={"name","id","age","class","course"}








#10.Write a script to print all the rows of a csv file. (hint : use pandas library).
#11.What is a json file? Write a script to load and print a json file. (hint : use json library)
#12.Write a script to get the maximum and minimum value in a csv column containing 10 numbers. (hint : use pandas or csv libraries).
#13.Write a function that accepts a sentence from a paragraph stored in a text file input.txt and calculates the number of letters and digits within that sentence string.
#14.Write a function add which takes variable parameters using *args and **kwargs. and it returns the sum of all arguments which are integers (hint : research about *args and **kwargs in python on google).
#15.Write a function calculate() such that it can accept two variables and calculate the addition, multiplication of them. The result must be returned a single return call. The two variables are lists. (Do arithmetic operations on lists).
#16.Create a function display_student_data() which takes student id, student name and marks as input. It should display all the data. If marks is missing it should display 75.
#17.Write a script to read first n lines of a file. Accept filename and n as input from the user. Similar to Unix head command. (understand how unix head command works by searching on google or youtube).
#18.Write a script to read last n lines of a file. Accept filename and n as input from the user. Similar to Unix tail command. (understand how unix tail command works by searching on google or youtube).
#19.Write a program to count the number of words in an input file that contains 2 Huge paragraphs. (Take random text from websites containing multiple paragraphs and store that text in a text file). Perform Exception Handling for the code to work even if the input file doesn't exist.
#20.Write a script that accepts a comma separated list of characters (and words) and prints an underscore _ separated list of characters (and words) in the sorted order as shown below :
#Input: b,c,a,d,a,e,b,f Output: a_a_b_b_c_d_e_f. Next apply this logic to words. Input : om sri sai ram. Output : om_ram_sai_sri

#Top 10 contributors will be rewarded.

HAPPY PYTHON CODING AND ALL THE BEST

Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About     '''
