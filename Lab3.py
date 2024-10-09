def check_loan_eligibility(salary, loan_amount):
    # Eligibility criteria
    min_salary = 30000.00
    max_loan_amount = salary * 10

    if salary < min_salary:
        return False, "Salary is too low."
    elif loan_amount > max_loan_amount:
        return False, "Requested loan amount is too high."
    else:
        return True, ""

def calculate_repayment(loan_amount, months):
    # Calculate the total repayment with a 10% interest increase
    interest_rate = 0.10
    total_repayment = loan_amount * (1 + interest_rate)
    monthly_payment = total_repayment / months
    return total_repayment, monthly_payment

def main():
    # Input: salary and requested loan amount
    try:
        salary = float(input("Enter your monthly salary: "))
        loan_amount = float(input("Enter the loan amount you want to request: "))

        # Check eligibility
        eligible, message = check_loan_eligibility(salary, loan_amount)
        
        if eligible:
            months = int(input("Enter the number of months to pay: "))
            total_repayment, monthly_payment = calculate_repayment(loan_amount, months)
            print(f"You are eligible for the loan.")
            print(f"Total amount to be repaid: {total_repayment:.2f}")
            print(f"Monthly payment over {months} months: {monthly_payment:.2f}")
        else:
            print("Loan not approved:", message)

    except ValueError:
        print("Please enter valid numbers for salary and loan amount.")

if __name__ == "__main__":
    main()
