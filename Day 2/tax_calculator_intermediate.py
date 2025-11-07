# This program allows user to calculate tax, based on tax slabs and tax rates.

# Inputs
# Tax limit amounts ranges
TAX_LIMIT_SLAB_1 : int = 10_00_000
TAX_LIMIT_SLAB_2 : int = 20_00_000
TAX_LIMIT_SLAB_3 : int = 35_00_000
TAX_LIMIT_SLAB_4 : int = 50_00_000
# Tax rates for different slab ranges
TAX_RATE_SLAB_1 : int = 5
TAX_RATE_SLAB_2 : int = 10
TAX_RATE_SLAB_3 : int = 20
TAX_RATE_SLAB_4 : int = 30
# User Input
base_income : float = float(input("Enter your annual base income: "))

# Display
print()
print("=" * 40)
print("Income Tax Calculator")
print("=" * 40)
print(f"Base Income:            \u20B9{base_income}")

# Calculation
tax_amount : float = 0

if base_income > TAX_LIMIT_SLAB_1:
    print(f"Tax Rate Slab 1:        {TAX_RATE_SLAB_1}%")
    if base_income > TAX_LIMIT_SLAB_2:
        tax_amount += 50_000
        print(f"Tax Rate Slab 2:        {TAX_RATE_SLAB_2}%")

        if base_income > TAX_LIMIT_SLAB_3:
            tax_amount += 1_50_000
            print(f"Tax Rate Slab 3:        {TAX_RATE_SLAB_3}%")

            if base_income > TAX_LIMIT_SLAB_4:
                tax_amount += 3_00_000 + ((base_income - TAX_LIMIT_SLAB_4) * TAX_RATE_SLAB_4 / 100)
                print(f"Tax Rate Slab 4:        {TAX_RATE_SLAB_4}%")

            else:
                tax_amount += ((base_income - TAX_LIMIT_SLAB_3) * TAX_RATE_SLAB_3 / 100)

        else:    
            tax_amount += ((base_income - TAX_LIMIT_SLAB_2) * TAX_RATE_SLAB_2 / 100)

    else:
        tax_amount += ((base_income - TAX_LIMIT_SLAB_1) * TAX_RATE_SLAB_1 / 100)

else:
    print("income below \u20B910,00,000 tax rate: 0%")

print("-" * 40)
print(f"Tax Amount:             \u20B9{tax_amount}")
print("=" * 40)

# Improve Logic, code quality, code annotation and timing