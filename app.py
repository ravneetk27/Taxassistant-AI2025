from openai import OpenAI

client = OpenAI(api_key="") # Add api key this is custom api key using with temp account

def calculate_tax(income):
    """
    Calculate income tax based on the following tax brackets:
    - Up to ₹2,50,000: no need to pay tax
    - ₹2,50,001 to ₹5,00,001: 5%
    - ₹5,00,001 to ₹10,00,000: 10%
    - above ₹10,00,001 : 20%
    """
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = income * 5/100
    elif income <=1000000:
        tax = income *10/100
    else: 
        tax=income * 20/100
    return tax

def get_tax_tips():
    """
    Provide some general tax tips.
    """
    tips = [
        "1. Always keep track of your expenses and save receipts.",
        "2. Contribute to a retirement account to reduce taxable income.",
        "3. File your taxes on time to avoid penalties.",
        "4. Consider consulting a tax professional for complex situations."
        "5. Claim home loan benefits – Save tax on both principal (80C) and interest (Section 24, up to ₹2 lakh) of a home loan."
        "6. Get health insurance (80D) – Save tax on premiums paid for self, family, and parents (up to ₹75,000 if parents are senior citizens)."
    ]
    return "\n".join(tips)

def ask_ai(question):
    # here is the openai api execution
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "You are a helpful tax assistant. Provide clear and concise answers to tax-related questions."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    print("Welcome to the AI-Powered Tax Assistance Bot!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Calculate Income Tax")
        print("2. Get Tax Tips")
        print("3. Ask a Tax Question")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            income = float(input("Enter your annual income: ₹"))
            tax = calculate_tax(income)
            print(f"Your estimated income tax is: ₹{tax:.2f}")
        elif choice == "2":
            print("\nHere are some tax tips:\n")
            print(get_tax_tips())
        elif choice == "3":
            question = input("What is your tax-related question? ")
            print("\nAI Response:\n")
            print(ask_ai(question))
        elif choice == "4":
            print("Thank you for using the AI-Powered Tax Assistance Bot. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()