# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
#https://www.w3schools.com/python/python_file_handling.asp
#https://www.pythonpool.com/remove-brackets-from-list-python/
#https://www.w3schools.com/python/ref_string_format.asp

# Student IIT No : 20222360
# Student ID/ UOW No : W1990085
# Date : 21/04/2023

#assigning varible
pass_count = 0       
defer_count = 0
fail_count = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
progress = []
progress_module_trailer = []
module_retriever =[]
exclude = []

#put all the marks to this crdit variable list
credit = [0,20,40,60,80,100,120]

def checkinput(marks):
#Putting all marks to list called credit
    credit = [0,20,40,60,80,100,120]
    #Going to check the input marks is number or not
    try:
        marks = int(marks)
    except ValueError:
        print('Integer required')
        return 'error'
    else:
        if not marks in credit:
            print('Out of range')
            return 'error'
        
        return marks
    
while True:
    
    #Adding while loop to get pass, defer, fail marks while calling function
    while True:
        pass_credit = checkinput(input('Please enter your credit at pass : '))
        if pass_credit != 'error':
            break

    while True:    
        defer_credit = checkinput(input('Please enter your credit at defer : '))
        if defer_credit != 'error':
            break

    while True:    
        fail_credit = checkinput(input('Please enter your credit at fail : '))   
        if fail_credit != 'error':
            break

    #Now assigning a total varible to print the progression outcome 
    total = pass_credit + defer_credit + fail_credit
    if total != 120:
        print('Total incorrect')
#Now appending values to the progress list
    elif pass_credit == 120:
        print('Progress')
        progress.append([pass_credit, defer_credit, fail_credit])
    #Now appending values to the progreess module trailer list
    elif pass_credit == 100:
        print('Progress(module trailer)')
        progress_module_trailer.append([pass_credit, defer_credit, fail_credit])
    #Now appendingg values to the module retriever list
    elif fail_credit <= 60:
        print('Do not progress - module retriever')
        module_retriever.append([pass_credit, defer_credit, fail_credit])
#And finally appending values to the exclude list
    else:
        print('exclude')
        exclude.append([pass_credit, defer_credit, fail_credit])

    #Asking user to continue this program or quit program 
    print('\nWould you like to enter another set of data?')
    feedback = str(input("Enter 'y' for yes or 'q' to quit and view results : "))
    print()
    if feedback.lower() == 'y':
        continue
    elif feedback.lower() == 'q':
        break
    else:
        print('Invalid Feedback')
        break


#Now putting all the progression outcome to text file that I assigned as CW part 3.txt
print('Part 3:')
newfile = open('CW part 3.txt','w')
with open("CW part 3.txt","a") as output :
#Now using join method to remove brackets and  using format strings for this program
    for i in progress:
        output.write(f'Progress - {", ".join(str(j) for j in i)}\n')
    for i in progress_module_trailer:
        output.write(f'Progress (module trailer) -{", ".join(str(j) for j in i)}\n')
    for i in module_retriever:
        output.write(f'Module retriever -{", ".join(str(j) for j in i)}\n')
    for i in exclude:
        output.write(f'Exclude -{", ".join(str(j) for j in i)}\n')      