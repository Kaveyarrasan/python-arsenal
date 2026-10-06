# Function to calculate food delivery discount based on total order value
def food_delivery_discount():
    mov_threshold = 1000   # Setting threshold for discount

    try:
        total_order_value = float(input("Enter the total amount of order: "))

        if total_order_value < 0:
            # print("Entered total order cannot be negative")
            raise ValueError("Entered total order cannot be negative")

        elif total_order_value >= mov_threshold:
            discount = 0.1 * total_order_value
            total_order_value -= discount
            print(f"Discounted order amount: {total_order_value}")
        else:
            print(f"Total order amount: {total_order_value}")
    except ValueError as err_message:
        print(f"Error caused: {str(err_message).capitalize()}\nPlease provide the actual total amount in numbers")

    except Exception as err_message:
        print("Seems some unusual error causing in calculating discount")
        print("Please provide the actual total amount in numbers")


# We create multiple small reusable functions (bonus calc, tax calc, net salary calc)

# bonus calculation function
def bonus_calc(salary, bonus_percentage):
    return salary * bonus_percentage  # calculating bonus with salary

# tax calculation function as per new tax slabs in India following new regime for FY 2026-27
def tax_calc(salary):
    tax_value = 0

    if salary <= 1200000:
        return tax_value
        
    elif salary > 1200000:
        if 400001 <= salary <= 800000:
            tax_value = (salary - 400000) * 0.05
            
        elif 800001 <= salary <= 1200000:
            tax_value = (400000 * 0.05) + (salary - 800000) * 0.10
            
        elif 1200001 <= salary <= 1600000:
            tax_value = (400000 * 0.05) + (400000 * 0.10) + (salary - 1200000) * 0.15
            
        elif 1600001 <= salary <= 2000000:
            tax_value = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (salary - 1600000) * 0.20
            
        elif 2000001 <= 400000 <= 2400000:
            tax_value = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (salary - 2000000) * 0.25
            
        else:
            tax_value = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (400000 * 0.25) + (salary - 2400000) * 0.30
        
        tax_value += tax_value * 0.04
        return tax_value


# net salary calculation function
def net_salary_calc(salary, bonus_percentage, pf, incentives):
    bonus = bonus_calc(salary, bonus_percentage)
    tax = tax_calc(salary)
    net_salary = salary + bonus + incentives - (tax + pf)
    return net_salary
