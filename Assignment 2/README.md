This is a Loan Contract based on a smart contract Metacoin.
Meta coin smart contract has 2 functions and our loan contract inherits from Metacoin.
The creditor can request loan to be cleared using reqLoan function and can see balance of the owner by getOwnerBalance function. reqLoan takes principal amount crediter gave, rate and time as parameters. getOwnerBalance doesn't require any parameters.
Owner can view his dues using viewDues function which takes address of the creditor as parameter and can settle his dues using settleDues function ehich also takes address of the creditor as parameter. These functions can only be used by Owner of the contract.
