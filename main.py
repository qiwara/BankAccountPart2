from bank import CoolBank
from checking import Checking
from savings import Savings

savingsAcct1 = Savings("Parth", 0.005)
savingsAcct2 = Savings("Qi", 0.003)

# Initial account setup
checkingAcct1 = Checking("Qi", 1000)
checkingAcct2 = Checking("Parth", 1000)
checkingAcct1.deposit(200)
checkingAcct2.deposit(1000)
checkingAcct1.print_customer_information()
checkingAcct2.print_customer_information()

# Transfer limit checks
checkingAcct1.transfer(2000, checkingAcct2)
checkingAcct1.transfer(200, checkingAcct2)
checkingAcct1.transfer(100, checkingAcct2)

# Transfer check
checkingAcct1.print_customer_information()
checkingAcct2.print_customer_information()

# Withdraw check
checkingAcct2.withdraw(1001)
checkingAcct2.withdraw(100)
checkingAcct2.print_customer_information()

