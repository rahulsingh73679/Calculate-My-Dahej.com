import streamlit as st
import os
import random

st.title("Calculate My Dahej")
st.write("Enter your details to calculate the dowry amount")

# Create input fields
salary = st.number_input("Monthly Salary (in INR)", min_value=0, step=1000)
cows = st.number_input("Number of Cows", min_value=0, step=1)
property = st.number_input("Property in Acres", min_value=0.0, step=0.1)
siblings = st.slider("Number of Siblings", min_value=0, max_value=10, value=0)
govt_job = st.radio("Sarkari Naukri?", ("Yes", "No"))

# Calculate button
if st.button("Apna Dahej Jane"):
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
    total_dowry = (base_amount + salary_multiplier*base_amount_govt + cow_value + property_value)/(siblings+1)
    #st.write(total_dowry)
    # Additional items and their costs
    
    items = []
    deductions = 0
    if total_dowry > 12000000 :
        trait = "Exotic"
    elif total_dowry > 500000 and govt_job == "Yes":
        trait = "Maal"
    
    
    elif total_dowry > 1000000:
        trait = "Gori"
    elif total_dowry > 500000:
        trait = "Sundar"
    elif total_dowry > 200000:
        trait = "Matric pass"
    elif total_dowry > 100000:
        trait = "Dehati"
    else :
        trait = "Sawli"

    


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
        deductions += 6000000
    elif total_dowry > 3000000:
        items.append("Fortuner")
        deductions += 2000000

    elif total_dowry > 2000000:
        items.append("Thar")
        deductions += 1300000
    elif total_dowry > 1500000:
        items.append("Tata Nexon")
        deductions += 1000000
    elif total_dowry > 700000:
        items.append("Maruti Alto")
        deductions += 400000
    

    # Bike (3 lakh)
    elif total_dowry > 300000 and govt_job == "Yes":
        items.append("Bullet ")
        deductions += 200000
    elif total_dowry > 300000:
        items.append("Bike ")
        deductions += 200000
    # Scooter (2 lakh)
    elif total_dowry > 200000:
        items.append("Scooter ")
        deductions += 100000
    
    if total_dowry > 1500000:
        items.append("Diamond set")
        deductions += 100000
    elif total_dowry > 700000:
        items.append("Sone Ka chain")
        deductions += 50000
    if total_dowry < 200000:
        items.append("Chandi Ka Anguthi")
        deductions += 4000


    if total_dowry > 7000000:
        items.append("Aur Ek Farmhouse")
        deductions += 1500000
    elif total_dowry > 3000000:
        items.append("Patna mein flat")
        deductions += 700000
    if total_dowry > 2500000:
        items.append("Aur Ek Russian")
        deductions += 6000
    
    
    # Final amount after deductions
    final_amount = total_dowry - deductions


    if final_amount > 500000:
        sen = "Cash"
    elif final_amount < 500000 and final_amount > 100000:

        sen = "UPI se"
    elif final_amount < 100000:
        sen = "Udhar"
    
    st.success(f"Estimated Dahej: ₹{int(final_amount):,} {sen}")

    # Display additional items if any
    if items:
        st.write("\n plus :")
        for item in items:
            st.write(f"- {item}")
    
    # Display image
    try:
        image_folder = f"images/{trait}"
        
        if os.path.exists(image_folder):
            # Filter only .jpeg files
            image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpeg')]
            
            if image_files:
                random_image = random.choice(image_files)
                image_path = os.path.join(image_folder, random_image)
                st.image(image_path, caption=f"✨ Aapki hone wali dulhan ✨", use_column_width=True)



            else:
                st.warning(f"No .jpeg images found in `{image_folder}`.")
        else:
            st.warning(f"Folder `{image_folder}` does not exist.")
    except Exception as e:
        st.error(f"⚠️ Error displaying image: {str(e)}")
