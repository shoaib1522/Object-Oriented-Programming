class DateTime:
    MaxDD=31
    MaxMM=12
    def __new__(cls,DD=1,MM=1,YYYY=1):
        # if DD<=cls.MaxDD and MM<=cls.MaxMM:
        #     if (MM==4 or MM==6 or MM==9 or MM==11) and DD<=30:
        #         print(f'THIS DATE {DD}/{MM}/{YYYY} EXISTS')
        #     elif (MM==2 and DD<=28) or (MM==2 and YYYY%4==0 and DD<=29):
        #         print(f'THIS DATE {DD}/{MM}/{YYYY} EXISTS')
        #     elif(MM==1 or MM==3 or MM==5 or MM==7 or MM==8 or MM==10 or MM==12) and DD<=31:
        #         print(f'THIS DATE {DD}/{MM}/{YYYY} EXISTS')
        # else:
        #     print(f'THIS DATE {DD}/{MM}/{YYYY} DOESN\'T EXISTS')
        #     print(f'YOU HAVE TO ENTER NEW DATES TO CHECK')
        #     return
        print(f'CHECKING DATE {DD}/{MM}/{YYYY}')
        obj = super().__new__(cls)
        return obj
    def __init__(self,DD=1,MM=1,YYYY=1):
        self.DD=DD
        self.MM=MM
        self.YYYY=YYYY
        return
    # def __str__(self):
    #     string=f'The last date of this month is the date you ASKED FOR: \n'
    #     string+=f'  Year:{self.YYYY}  and Month:{self.MM}  \n'
    #     for i in range(1,self.DD,7):
    #         for j in range(i,i+7):
    #             string+=f'{j}  '
    #         string+=f'\n'
    #     return string
    def __str__(self):
        return '{}/{}/{}'.format(self.DD,self.MM,self.YYYY)
def get_valid_date():
    while True:
        try:
            # Get input from the user
            DD = int(input("Enter day (DD): "))
            MM = int(input("Enter month (MM): "))
            YYYY = int(input("Enter year (YYYY): "))

            # Check if the date is valid
            if 1 <= DD <= DateTime.MaxDD and 1 <= MM <= DateTime.MaxMM:
                if (MM == 4 or MM == 6 or MM == 9 or MM == 11) and DD <= 30:
                    print(f'THIS DATE {DD}/{MM}/{YYYY} EXISTS')
                elif (MM == 2 and DD <= 28) or (MM == 2 and YYYY % 4 == 0 and DD <= 29):
                    print(f'THIS DATE {DD}/{MM}/{YYYY} EXISTS')
                elif (MM == 1 or MM == 3 or MM == 5 or MM == 7 or MM == 8 or MM == 10 or MM == 12) and DD <= 31:
                    print(f'THIS DATE {DD}/{MM}/{YYYY} EXISTS')
                else:
                    print(f'THIS DATE {DD}/{MM}/{YYYY} DOESN\'T EXISTS')
                    print(f'YOU HAVE TO ENTER NEW DATES TO CHECK')
                    continue  # Continue the loop to get valid input
            else:
                print(f'THIS DATE {DD}/{MM}/{YYYY} DOESN\'T EXISTS')
                print(f'YOU HAVE TO ENTER NEW DATES TO CHECK')
                continue  # Continue the loop to get valid input

            # If the code reaches here, the input is valid, break out of the loop
            break
        except ValueError:
            print("Invalid input. Please enter integers for day, month, and year.")

    return DateTime(DD, MM, YYYY)

def main():
    new_var = get_valid_date()
    print(str(new_var))

if __name__ == "__main__":
    main()
