# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
#https://www.w3schools.com/python/python_lists.asp
#https://www.w3schools.com/python/ref_list_append.asp
#https://www.pythonpool.com/remove-brackets-from-list-python/

# Student IIT NO : 20222360
# Student ID/ UOW NO : W1990085
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
    if feedback.lower() =='y':
        continue
    elif feedback.lower() =='q':
        break
    else:
        print('Invalid Feedback')
        break


#Then accessing those stored data from the list and print data in the below list and removing brackets by using join method
print('Part 2:')
for i in progress:
    print('Progress - ',', '.join(str(j) for j in i))
for i in progress_module_trailer:
    print('Progress (module trailer) - ',', '.join(str(j) for j in i))
for i in module_retriever:
    print('Module retriever - ',', '.join(str(j) for j in i))
for i in exclude:
    print('Exclude - ',', '.join(str(j) for j in i))