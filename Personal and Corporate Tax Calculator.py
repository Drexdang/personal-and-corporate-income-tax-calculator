import streamlit as st

# Set page config
st.set_page_config(page_title="Personal and Corporate Income Tax Calculator")

# Markdown and Headings
html_temp = """ 
<div style="background-color: red; padding: 16px">
<h2 style="color: black; text-align: center;">Personal and Corporate Income Tax Calculator Web App</h2>
</div>
"""

st.markdown(html_temp, unsafe_allow_html=True)

st.write('')
st.write('')
st.markdown("##### Welcome to this web app that will help you calculate your personal and corporate income tax liabilities.\n##### Enjoy your time on the app.")

# Function to calculate personal income tax based on provided rules
def calculate_personal_income_tax(income):
    consolidated_relief_allowance = max(200000, income * 0.01)
    pension = income * 0.08
    taxable_income = income - consolidated_relief_allowance - pension

    # Define personal tax brackets and rates
    personal_tax_brackets = [
        (300000, 0.07),
        (300000, 0.11),
        (500000, 0.15),
        (500000, 0.19),
        (1600000, 0.21),
        (3200000, 0.24)
    ]

    # Calculate the personal tax payable
    personal_tax_payable = 0
    for bracket in personal_tax_brackets:
        bracket_amount, rate = bracket
        if taxable_income <= 0:
            break
        taxable_amount = min(bracket_amount, taxable_income)
        personal_tax_payable += taxable_amount * rate
        taxable_income -= taxable_amount

    # Calculate PAYE for personal income
    paye = personal_tax_payable

    return paye

# Function to calculate corporate income tax based on provided rules
def calculate_corporate_income_tax(turnover, assessable_profits, foreign_company=False):
    tax = 0
    if turnover <= 0:
        tax = 0
    elif assessable_profits <= 0:
        tax = 0
    else:
        if foreign_company:
            tax = turnover * 0.1
        else:
            tax = assessable_profits * 0.3

    return tax

# Streamlit UI for Personal Income Tax Calculator
st.sidebar.title("Personal Income Tax Calculator")
st.subheader("Enter your annual income (NGN):")
st.subheader("For personal income  tax calculation, enter the annual gross income.")
income = st.sidebar.number_input("Annual Gross Income (NGN)")

if st.sidebar.button("Calculate Personal Tax"):
    personal_income_tax = calculate_personal_income_tax(income)
    st.write(f"PAYE (Tax Payable): {personal_income_tax:.2f}")

# Streamlit UI for Corporate Income Tax Calculator
st.sidebar.title("Corporate Income Tax Calculator")
st.subheader("Enter company financials (NGN):")
st.subheader("For corporate tax calculation, enter the company's turnover and assessable profits.")
turnover = st.sidebar.number_input("Turnover (NGN):", value=0.0)
assessable_profits = st.sidebar.number_input("Assessable Profits (NGN):", value=0.0)
foreign_company = st.sidebar.checkbox("Is it a foreign digital company?")
calculate_button = st.sidebar.button("Calculate Corporate Tax")

if calculate_button:
    corporate_income_tax = calculate_corporate_income_tax(turnover, assessable_profits, foreign_company)
    st.write(f"Company Income Tax: {corporate_income_tax:.2f}")

# Run the Streamlit app
if __name__ == '__main__':
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.set_option('deprecation.showPyplotGlobalUse', False)