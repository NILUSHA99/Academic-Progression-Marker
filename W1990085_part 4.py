# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
#https://www.w3schools.com/python/python_dictionaries.asp
#https://www.pythonpool.com/remove-brackets-from-list-python/
#https://www.w3schools.com/python/ref_string_format.asp

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
dictionary = {}
#put all the marks to this crdit variable list


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
    UOW_No = input('Enter your UOW No : ')

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
#Now assigning a total to get progression outcome
    total = pass_credit + defer_credit + fail_credit

#Now adding dictionary part for the all the progress outcome 
    if total != 120:
        print('Total incorrect')
    elif pass_credit == 120:
        print('Progress')
        dictionary[UOW_No] = f'Progress - {pass_credit}, {defer_credit}, {fail_credit}'
    elif pass_credit == 100:
        print('Progress(module trailer)')
        dictionary[UOW_No] = f'Progress (module trailer) - {pass_credit}, {defer_credit}, {fail_credit}'
    elif fail_credit <= 60:
        print('Do not progress - module retriever')
        dictionary[UOW_No] = f'Module retriever - {pass_credit}, {defer_credit}, {fail_credit}'
    else:
        print('exclude')
        dictionary[UOW_No] = f'Exclude - {pass_credit}, {defer_credit}, {fail_credit}'


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

print('-'*50)
#Printing part 4 and removing the brackets by using join method
print('Part 4:')
print(' '.join("{}: {}".format(k, v) for k, v in dictionary.items()))