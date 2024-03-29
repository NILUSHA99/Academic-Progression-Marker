# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# https://www.w3D3schools.com/python/python_while_loops.asp
# https://www.toolsqa.com/python/python-while-loop/#:~:text=The%20%22while%20true%22%20loop%20in,the%20%22do%20while%22%20loop.
# https://www.w3schools.com/python/ref_string_lower.asp
# https://www.javatpoint.com/python-new-line
# https://www.w3schools.com/python/ref_string_format.asp

# Student IIT NO : 20222360
# Student ID/ UOW NO : W1990085
# Date : 21/04/2023

#assigning varible
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
progrees = []
progress_module_trailer = []
module_retriever =[]
exclude = []

#Using a function for take values from user 
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
        continue

    elif pass_credit == 120:
        print('Progress')
        progress_count = progress_count + 1

    elif pass_credit == 100:
        print('Progress(module trailer)')
        trailer_count = trailer_count + 1

    elif fail_credit <= 60:
        print('Module retriever')
        retriever_count = retriever_count + 1

    else:
        print('exclude')
        exclude_count = exclude_count + 1


#Asking user to continue this program or quit program 
    print('\nWould you like to enter another set of data?')
    feedback = str(input("Enter 'y' for yes or 'q' to quit and view results : "))

    if feedback.lower() =='y':
        continue
    elif feedback.lower() =='q':
        break
    else:
        print('Invalid Feedback')
        break

#Print the histogram and progression outcome
print('-'*50)
print('Histogram')
print('\nProgress',progress_count, ':','*'*progress_count)
print('\nTrailer',trailer_count, ':', '*'*trailer_count)
print('\nRetriever',retriever_count, ':', '*'*retriever_count)
print('\nExcluded',exclude_count, ':', '*'*exclude_count)
print(f"\n{progress_count + trailer_count + retriever_count + exclude_count} outcomes in total.")
print('-'*50)