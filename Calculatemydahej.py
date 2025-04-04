import streamlit as st

st.title("Calculate My Dahej")
st.write("Enter your details to calculate the dowry amount")

# Create input fields
salary = st.number_input("Monthly Salary (in INR)", min_value=0, step=1000)
cows = st.number_input("Number of Cows", min_value=0, step=1)
property = st.number_input("Property in Acres", min_value=0.0, step=0.1)
govt_job = st.radio("Sarkari Naukri?", ("Yes", "No"))
# Calculate button
if st.button("Calculate Dowry"):
    # Base calculation logic
    base_amount = 10000  # Base amount
    

    if govt_job == "Yes":
        base_amount_govt = 2
    else:
        base_amount_govt = 1
    # Salary multiplier
    salary_multiplier = salary * 12  # Annual salary
    
    # Cow value (assuming 50,000 INR per cow)
    cow_value = cows * 50000
    
    # Property value (assuming 10,00,000 INR per acre)
    property_value = property * 1000000
    
    # Total calculation
    total_dowry = base_amount + salary_multiplier*base_amount_govt + cow_value + property_value
    #st.write(total_dowry)
    # Additional items and their costs
    items = []
    deductions = 0
    
    if total_dowry > 500000 and govt_job == "Yes":
        trait = "Maal"
    elif total_dowry > 1000000:
        trait = "Gori"
    elif total_dowry > 500000:
        trait = "petite"
    elif total_dowry > 200000:
        trait = "Matric pass"
    elif total_dowry > 100000:
        trait = "Dehati"
    else :
        trait = "Kali"

    


    # Ek Dulhan (1 lakh)
    if total_dowry > 100000:
        items.append(" " + trait + " dulhan ")
        
    
    if total_dowry > 1500000:
        items.append("Do Saali")
        
    # Ek Saali (10 lakh)
    elif total_dowry > 700000:
        items.append("Ek Saali ")
        
    
    # Do Saali (15 lakh)
    
    # Bike (3 lakh)

    if total_dowry > 7000000:
        items.append("Mercedes")
        deductions += 7000000
    elif total_dowry > 3000000:
        items.append("Fortuner")
        deductions += 3000000

    elif total_dowry > 2000000:
        items.append("Thar")
        deductions += 2000000
    elif total_dowry > 1500000:
        items.append("Tata Nexon")
        deductions += 1500000
    elif total_dowry > 700000:
        items.append("Maruti Alto")
        deductions += 400000
    

    # Bike (3 lakh)
    elif total_dowry > 300000 and govt_job == "Yes":
        items.append("Bullet ")
        deductions += 300000
    elif total_dowry > 300000:
        items.append("Bike ")
        deductions += 200000
    # Scooter (2 lakh)
    elif total_dowry > 200000:
        items.append("Scooter ")
        deductions += 100000
    
    if total_dowry > 500000:
        sen = "Cash"
    elif total_dowry < 500000 and total_dowry > 100000:

        sen = "UPI se"
    elif total_dowry < 100000:
        sen = "Udhar"
    
    if total_dowry > 1500000:
        items.append("Diamond set")
        deductions += 100000

    # Final amount after deductions
    final_amount = total_dowry - deductions
    st.success(f"Estimated Dahej: ₹{int(final_amount):,} {sen}")

    # Breakdown
  
    
    # Display additional items if any
    if items:
        st.write("\n plus :")
        for item in items:
            st.write(f"- {item}")
    
    #st.write(deductions)

# Disclaimer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        color: #888;
        font-family: 'Georgia', serif;
        font-size: 16px;
    }
    </style>
    <div class="footer">
        Developed by <strong>Rahul Singh</strong>
    </div>
    """,
    unsafe_allow_html=True
)
