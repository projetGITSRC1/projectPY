import itertools

min_length = "2"
max_length = "2"

list= '1234567890qwertyuiopasdfgjklzxcvbnm[];,./!@#$%^&*()_+:<>?'




with open('listpass.txt', 'w') as f_out:
    for n in range(min_length, max_length+1):
        for xs in itertools.product(list, repeat=n):
            print (''.join(xs), file=f_out)
