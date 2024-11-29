# Description: One Stop Insurance Company - a program to enter and calculate new insurance policy information for its customers
# Author: Justin Greenslade
# Class: Python SD 13.
# Date(s): Nov 15 – 29


# Define required libraries.
import datetime
import FormatValues as FV

# Define program constants.
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00 # Insurance premiums are calculated using a basic rate for the first automobile.
DISCOUNT_ON_ADDITIONAL = .25 # each additional automobile offered at a discount of 25%. 
EXTRA_LIABILITY_COST = 130.00 # $130.00 per car for extra liability.
GLASS_COST = 86.00 # $86.00 per car for glass coverage.
LOANER_COST = 58.00 # $58.00 per car for the loaner car.
HST = .15
PROCESSING_FEE = 39.99
ALLOWED_NAME_CHARACTERS = set("ABCDEFGHIJKLMNOPQRSTUVTXYZ abcdefghijklmnopqrstuvwxyz-")
ALLOWED_NUMBER_CHARACTERS = set("1234567890")
PROVINCE_LST = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]
PAYMENT_OPTIONS_LST = ["Full", "Monthly"]
YES_OR_NO_VAL = ["Y", "N"]
CURRENT_DATE = datetime.datetime.now()

# Define program functions.

# Function to calculate extra costs based on user's choices.
def CalculateExtraCost(NumInsured):

    YES_OR_NO_VAL = ["Y", "N"]
    GLASS_COST = 86.00 # $86.00 per car for glass coverage.
    LOANER_COST = 58.00 # $58.00 per car for the loaner car.

    while True:
        # Determines if the user whats to pay any extra liability
        ExtraLiabilityChoice = input("Would you like to have extra liability ( Y or N ): ").upper()

        if ExtraLiabilityChoice == "":
            print()
            print("Data entry error - Must enter ( Y or N )...")
            print()

        elif ExtraLiabilityChoice not in YES_OR_NO_VAL:
            print()
            print("Data entry error - Must enter ( Y or N )...")
            print()
        
        else:
            break

    
    if ExtraLiabilityChoice == "Y":
        ExtraLiabilityMsg = "Yes"
        ExtraLiabilityCost = EXTRA_LIABILITY_COST * NumCarsInsured
           
    else:
        ExtraLiabilityMsg = "No"
        ExtraLiabilityCost = 0.0


    # Determins if the user wants the glass coverage.
    while True:
        GlassCoverChoice = input("Would you like glass coverage ( Y or N ): ").upper()
        if GlassCoverChoice == "":
            print()
            print("Data entry error - Must enter ( Y or N )...")
            print()
        elif GlassCoverChoice not in YES_OR_NO_VAL:
            print()
            print("Data entry error - Must enter ( Y or N )...")
            print()
        elif GlassCoverChoice == "Y":
            GlassCoverMsg = "Yes"
            GlassCoverCost = GLASS_COST * NumCarsInsured
            break
        else:
            GlassCoverMsg = "No"
            GlassCoverCost = 0.0
            break

    while True:
        LoanerCarChoice = input("Would you like a loaner car ( Y or N ): ").upper()
        if LoanerCarChoice == "":
            print()
            print("Data entry error - Must enter ( Y or N )...")
            print()
        elif LoanerCarChoice not in YES_OR_NO_VAL:
            print()
            print("Data entry error - Must enter ( Y or N )...")
            print()
        elif LoanerCarChoice == "Y":
            LoanerCarMsg = "Yes"
            LoanerCarCost = LOANER_COST * NumCarsInsured
            break
        else:
            LoanerCarMsg = "No"
            LoanerCarCost = 0.0
            break

    # Return all relevant information
    return ExtraLiabilityMsg, ExtraLiabilityCost, GlassCoverMsg, GlassCoverCost, LoanerCarMsg, LoanerCarCost, ExtraLiabilityChoice, GlassCoverChoice, LoanerCarChoice

# Function to calculate total premium, including base premium and extra costs.
def CalculateTotalPremium(NumCarsInsured, ExtraLiabilityCost, GlassCoverCost, LoanerCarCost, DownPayAmt):
    AddCarPremium = 0
    BasePremium = BASIC_PREMIUM

    if NumCarsInsured > 1:
        AddCarPremium = BASIC_PREMIUM - (BASIC_PREMIUM * DISCOUNT_ON_ADDITIONAL)

    ExtraCost = ExtraLiabilityCost + GlassCoverCost + LoanerCarCost
    TotalInsurancePremium = (BasePremium + AddCarPremium + ExtraCost)
    NewTotalInsurancePremium = TotalInsurancePremium - DownPayAmt
    Tax = NewTotalInsurancePremium * HST
    Total = NewTotalInsurancePremium + Tax
    return TotalInsurancePremium, Tax, Total, ExtraCost, AddCarPremium, BasePremium, DownPayAmt, NewTotalInsurancePremium

# Gets Basic Customer Information.
def GetCustomerInfo():

    #Defined allowed characters 
    ALLOWED_NAME_CHARACTERS = set("ABCDEFGHIJKLMNOPQRSTUVTXYZabcdefghijklmnopqrstuvwxyz-")
    ALLOWED_NUMBER_CHARACTERS = set("1234567890")
    PROVINCE_LST = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]

    #Gets Customers first name.
    while True:
        FirstName = input("Enter the Customer first name: ").title()
        if FirstName == "":
            print()
            print("Data entry error - first name must be entered...")
            print()
        elif set(FirstName).issubset(ALLOWED_NAME_CHARACTERS) == False:
            print()
            print("Data entry error - first name must be valid characters...")
            print()
        else:
            break

    #Gets Customers last name.
    while True:
        LastName = input("Enter the Customer last name: ").title()
        if LastName == "":
            print()
            print("Data entry error - last name must be entered...")
            print()
        elif set(LastName).issubset(ALLOWED_NAME_CHARACTERS) == False:
            print()
            print("Data entry error - last name must be valid characters...")
            print()
        else:
            break

    # Gets Customers Address.
    while True:
        Address = input("Enter the Customer address: ")
        if Address == "":
            print()
            print("Data entry error - address must be entered...")
            print()
        else:
            break

    # Gets Customer City.
    while True:
        City = input("Enter the name of the Costumers city: ").title()
        if City == "":
            print()
            print("Data entry error - city must be entered...")
            print()
        else:
            break

    # Gets Customer Province.
    while True:
        Province = input("Enter the Customers province (XX): ").upper()
        if len(Province) != 2:
            print()
            print("   Data Entry Error - Provice is a 2 character code only...")
            print()
        elif Province not in PROVINCE_LST:
            print()
            print("   Data Entry Error - province is not valid...")
            print()
        else:
            break
        
    ##Gets Customers Postal code.
    while True:
        PostalCode = input("Enter the Customer postal code (X#X#X#): ").upper()
        if len(PostalCode) != 6:
            print()
            print("Data entry error - postal code must be 6 characters...")
            print()
            # Check the first, third, and fifth characters for letters, and the others for digits
        elif not (PostalCode[0].isalpha() and PostalCode[2].isalpha() and PostalCode[4].isalpha()):
                print()
                print("Data entry error - postal code must be in (X#X#X#) format...")
                print()

        elif not (PostalCode[1].isdigit() and PostalCode[3].isdigit() and PostalCode[5].isdigit()):
                print()
                print("Data entry error - postal code must be in (X#X#X#) format...")
                print()
        else:
            break

    #Gets Customers phone number.
    while True: 
        PhoneNumber = input("Enter the Customer phone number (0000000000): ")
        if set(PhoneNumber).issubset(ALLOWED_NUMBER_CHARACTERS) == False:
            print()
            print("Data entry error - phone number must be valid characters...")
            print()
        elif len(PhoneNumber) != 10:
            print()
            print("Data entry error - phone number must be 10 characters...")
            print()
        else:
            break
    
    return FirstName, LastName, Address, City, Province, PostalCode, PhoneNumber 

# Gets claims and adds them to a list.
def CollectClaims():
    Claims = []
    while True:
        while True:
            ClaimNumber = input("Enter the claim number (#####): ")# Check
            
            if len(ClaimNumber) != 5:                                   # Check
                print()
                print("Data entry error - claim number must be 5 digits")
                print()
            elif ClaimNumber.isdigit() == False:
                print()
                print("Data entry error - must consist of numbers...")
                print()
            else:
                break
        while True:
            ClaimDate = input("Enter the claim date (YYYY/MM/DD): ")
            if len(ClaimDate) != 10:
                print()
                print("Data entry error - must consist of numbers...")
                print()
            else:
                break


        while True:
            try:
                ClaimAmount = input("Enter the claim amount: ")
                ClaimAmount = (float(ClaimAmount))
                if ClaimAmount == "":
                    print()
                    print("Data entry error - must be a valid number")
                    print()
            except:
                print()
                print("Data entry error - must be a valid number")
                print()
            else:
                break
            
        Claims.append((ClaimNumber, ClaimDate, ClaimAmount))
        MoreClaims = input("Do you have more claims? (Y/N): ").upper()
        if MoreClaims == "N":
            break
    
    return Claims

# Main program starts here.

print()

while True:
    
    # Gather user inputs.


    FirstName, LastName, Address, City, Province, PostalCode, PhoneNumber = GetCustomerInfo()

    # Number of cars being insured
    while True:
        try:
            NumCarsInsured = input("Enter the number of cars being insured: ")
            NumCarsInsured = int(NumCarsInsured)  
            
            if NumCarsInsured < 1:
                print()
                print("Data entry error - must insure at least 1 car")
                print()
            else:
                break  

        except:  
            print()
            print("Data entry error - Number of cars insured must be a valid number...")
            print()

    
    ExtraLiabilityMsg, ExtraLiabilityCost, GlassCoverMsg, GlassCoverCost, LoanerCarMsg, LoanerCarCost, ExtraLiabilityChoice, GlassCoverChoice, LoanerCarChoice=  CalculateExtraCost(NumCarsInsured)


    
    # Determines if the Customer wants to pay in full or monthly or down payment.
    while True:
        PayMentChoice = input("How would you like to pay (Full or Monthly): ").title()
        if PayMentChoice not in PAYMENT_OPTIONS_LST:
            print()
            print("   Data Entry Error - Payment option is not valid...")
            print()
        else:
            break
    
    if PayMentChoice == "Monthly":
        PaymentMsg = "Payment will be 8 monthly payments"
    
        while True:
            DownPayMsg = "No"
            DownPayAmt = 0
            DownPayChoice = input("Would you like to make a down payment ( Y or N ): ").upper()
            if DownPayChoice == "":
                print()
                print("Data entry error - Must enter ( Y or N )...")
                print()
            elif set(DownPayChoice).issubset(YES_OR_NO_VAL) == False:
                print()
                print("Data entry error - Must enter ( Y or N )...")
                print()
            else:
                break

        if DownPayChoice == "Y":
            DownPayMsg = "Yes"
            while True:
                try:
                    DownPayAmt = input('Enter the amount you would like to down pay: ')
                    DownPayAmt =float(DownPayAmt)

                except:
                    print()
                    print("Data entry error - Downpayment must be a valid number...")
                    print()
                else:
                    break
                

                
                
                    
                    
       

    if PayMentChoice == "Full":
        PaymentMsg = "Thank you for paying in full"
        DownPayAmt = 0
        DownPayMsg = "No"
        DownPayChoice = "N"
            




    Claim = CollectClaims()

    # Perform required calculations.

    TotalInsurancePremium, Tax, Total, ExtraCost, AddCarPremium, BasePremium, DownPayAmt, NewTotalInsurancePremium = CalculateTotalPremium(NumCarsInsured, ExtraLiabilityCost, GlassCoverCost, LoanerCarCost, DownPayAmt)

    if PayMentChoice == "Monthly":
        if DownPayChoice == "Y":
            Cost = (Total + PROCESSING_FEE) / 8
        else:
            Cost = (Total + PROCESSING_FEE) / 8
    else: 
        Cost = Total



    InvoiceDateDsp = datetime.datetime.strftime(CURRENT_DATE, "%Y/%m/%d")
    InvoiceYear = CURRENT_DATE.year
    InvoiceMonth = CURRENT_DATE.month
    InvoiceDay = CURRENT_DATE.day

    if InvoiceMonth == 12:
        FirstPaymentMonth = 1
        FirstPaymentYear = InvoiceYear + 1
    else:
        FirstPaymentMonth = InvoiceMonth + 1
        FirstPaymentYear = InvoiceYear

    FirstPaymentDate = datetime.date(FirstPaymentYear, FirstPaymentMonth, 1)

    PhoneNumberDsp = "(" + PhoneNumber[0:3] + ") " + PhoneNumber[3:6] + "-" + PhoneNumber[6:10]
    PostalCodeDsp = PostalCode[0:3] + "-" + PostalCode[3:6]
    if PayMentChoice == "Monthly":
        NewTotal = Total + PROCESSING_FEE
    # Display results
    print()
    print(f"      One Stop Insurance Company")
    print()
    print(f"----------------------------------------")
    print(f"Invoice date:                 {InvoiceDateDsp:>10s}")
    print(f"Policy number:                      {POLICY_NUMBER:>2d}")
    print()
    print(f"First name:                 {FirstName:>12s}")
    print(f"Last name:                  {LastName:>12s}")
    print(f"Street Adress:      {Address:>20s}")
    print(f"City:               {City:>20s}")
    print(f"Province:                             {Province:>2s}")
    print(f"PostalCode:                      {PostalCodeDsp:>7s}")
    print(f"Phone Number:             {PhoneNumberDsp:>14s}")
    print(f"----------------------------------------")
    print()
    print(f"Number of cars insured:               {NumCarsInsured:>2d}")
    print(f"Price for first car:           {FV.FDollar2(BasePremium):>9s}")
    if NumCarsInsured >1:
        print(f"Price for extra cars:          {FV.FDollar2(AddCarPremium):>9s}")
    print(f"----------------------------------------")
    print()
    print(f"Extra liability coverage:            {ExtraLiabilityMsg:>3s}")
    print(f"Glass Coverage:                      {GlassCoverMsg:>3s}")
    print(f"Loaner car:                          {LoanerCarMsg:>3s} ")
    print()
    if ExtraLiabilityChoice == "Y":
        print(f"Extra liability coverage cost: {FV.FDollar2(ExtraLiabilityCost):>9s}")

    if GlassCoverChoice == "Y":
        print(f"Glass Coverage cost:           {FV.FDollar2(GlassCoverCost):>9s}")

    if LoanerCarChoice == "Y":
        print(f"Loaner car cost:               {FV.FDollar2(LoanerCarCost):>9s} ")
        
    print(f"                                --------")
    print(f"Total Extra fees:              {FV.FDollar2(ExtraCost):>9s}")
    print(f"----------------------------------------")
    print()
    if PayMentChoice == "Monthly":
        print(f"Down Payment:                        {DownPayMsg:>3s}")
    if DownPayChoice == "Y":
        print(f"Balance Before Downpayment:    {FV.FDollar2(TotalInsurancePremium):>9s}")
        print(f"Down Payment amount:         - {FV.FDollar2(DownPayAmt):>9s}")
        print(f"                              ----------")
    print(f"Insurance Premium:             {FV.FDollar2(NewTotalInsurancePremium):>9s}")
    print(f"HST (15%):                     {FV.FDollar2(Tax):>9s}")
    print(f"                              ----------")
    print(f"Total Premium:                 {FV.FDollar2(Total):>9s}")
    if PayMentChoice == "Monthly":
        print(f"Processing fee:                   {FV.FDollar2(PROCESSING_FEE):>6s}")
        print(f"                              ----------")
        print(f"New Total Premium:             {FV.FDollar2(NewTotal):>9s}")
    print()
    print(f"Payment option:                  {PayMentChoice:>7s}")
    if PayMentChoice == "Full":
        print()
        print(f"----- {PaymentMsg} -----")
    if PayMentChoice == "Monthly":
        print(f"Monthly Payment:               {FV.FDollar2(Cost):>9s}")
    print()
    if PayMentChoice == "Monthly":
        print(f"First Payment Date:  {FirstPaymentDate.strftime('%Y-%m-%d')}")

    # Claims
    print(f"----------------------------------------")
    print()
    print(f"            Claims History")
    print()
    print(f"  Claim         Claim           Claim")
    print(f"  Number         Date           Amount")
    print("---------------------------------------")
    for claims in Claim:
        print(f"  {claims[0]}        {claims[1]}    {FV.FDollar2(claims[2]):>10s}")
    print("---------------------------------------")


    AnotherCustomer = input("Do you want to enter another customer? (Y or N): ").upper()
    if AnotherCustomer != "Y":
        break
