# Import pandas to read, update, and analyse CSV data using DataFrames.
import pandas as pd

# Read the user accounts, role permissions, and worker safety records from their CSV files.
# Load project data
users = pd.read_csv("C:/Users/Katleho Mofokeng/Desktop/users.csv")
permissions = pd.read_csv("C:/Users/Katleho Mofokeng/Desktop/permissions.csv")
workers = pd.read_csv("C:/Users/Katleho Mofokeng/Desktop/workers.csv")


# Return True only when the logged-in user's role permits the requested operation.
# Check role permissions
def has_access(permission_name):
    if role_permissions[permission_name].values[0] == "Yes":
        return True
    else:
        return False


# Verify the username, Worker ID, and role before accepting a replacement password.
# Reset password
def forgot_password():

    username = input("Enter username: ")
    worker_id = input("Enter Worker ID: ")
    user_role = input("Enter Role: ")

    if username in users.Username.values:

        current_user = users[users.Username == username]

        if worker_id in current_user["Worker ID"].values:

            if user_role in current_user.Role.values:
                print("User verified")

                new_password = input("Enter new password: ")
                confirm_password = input("Confirm new password: ")

                # Only update the saved password if the two entered passwords match.
                if new_password == confirm_password:
                    users.loc[users.Username == username, "Password"] = new_password
                    users.to_csv("C:/Users/Katleho Mofokeng/Desktop/users.csv",
                                 index=False)

                    print("Password changed successfully")

                else:
                    print("Passwords do not match")

            else:
                print("Incorrect role")

        else:
            print("Incorrect Worker ID")

    else:
        print("Username not found")


# Display the loaded records for inspection.
print(users)
print(permissions)
print(workers)


# Keep requesting login details until a valid username/password combination is entered.
# Login
login_successful = False

while login_successful == False:

    print("Login")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users.Username.values:

        current_user = users[users.Username == username]

        if password in current_user.Password.values:
            print("Login successful")
            login_successful = True

        else:
            print("Incorrect password. Please try again.")

    else:
        print("Username not found. Please try again.")


# Find the authenticated user's role and select its permissions row.
# Get user role after successful login
user_role = current_user.Role.values[0]
print("Role:", user_role)

role_permissions = permissions[permissions.Role == user_role]
print(role_permissions)


# Only show dashboard information when the role grants dashboard access.
# Dashboard
if has_access("View Dashboard"):
    print("Dashboard")


# Show menu options conditionally so users see only modules their roles allow.
# Main menu
print("Main Menu")

if has_access("View Dashboard"):
    print("1. View Dashboard")

if has_access("Worker safety data"):
    print("2. Worker Safety Data")

if has_access("Safety incidents"):
    print("3. Safety Incidents")

if has_access("Equipment data"):
    print("4. Equipment Data")

if has_access("Maintenance data"):
    print("5. Maintenance Data")

if has_access("Risk Assessment"):
    print("6. Risk Assessment")

if has_access("Generate reports"):
    print("7. Generate Reports")

if has_access("Manage user"):
    print("8. Manage Users")

# Read the selected module number.
menu_choice = input("Select an option: ")


# Collect worker details and safety indicators when the selected role is authorised.
# Worker Health and Safety Monitoring
if menu_choice == "2" and has_access("Worker safety data"):

    worker_id = input("Enter Worker ID: ")
    department = input("Enter Department: ")
    job_role = input("Enter Job role: ")
    shift = input("Enter Shift: ")

    print("PPE compliance:")
    print("1. Yes")
    print("2. No")

    ppe_choice = input("Select 1 or 2: ")

    # Convert the selected PPE option into the stored Yes/No value.
    if ppe_choice == "1":
        ppe_compliance = "Yes"
    else:
        ppe_compliance = "No"

    print("Safety training:")
    print("1. Complete")
    print("2. Incomplete")

    training_choice = input("Select 1 or 2: ")

    # Convert the training selection into Complete or Incomplete.
    if training_choice == "1":
        safety_training = "Complete"
    else:
        safety_training = "Incomplete"

    print("Fatigue level:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    fatigue_choice = input("Select 1, 2 or 3: ")

    # Convert the fatigue selection into Low, Medium, or High.
    if fatigue_choice == "1":
        fatigue_level = "Low"

    elif fatigue_choice == "2":
        fatigue_level = "Medium"

    else:
        fatigue_level = "High"

    near_misses = input("Enter number of near misses: ")
    previous_incidents = input("Enter number of previous incidents: ")

    # Build a one-row DataFrame containing the new worker's information.
    # Add new worker
    new_worker = pd.DataFrame(
        [[worker_id, department, job_role, shift, ppe_compliance,
          safety_training, fatigue_level, near_misses, previous_incidents]],
        columns=["Worker ID", "Department", "Job role", "Shift",
                 "PPE compliance", "Safety training", "Fatigue level",
                 "Near misses", "Previous incidents"]
    )

    # Append the worker record and save the updated worker CSV file.
    workers = pd.concat([workers, new_worker])

    workers.to_csv("C:/Users/Katleho Mofokeng/Desktop/workers.csv",
                   index=False)

    print("Worker information saved successfully")
    print(workers)

    print("PPE compliance:", ppe_compliance)
    print("Safety training:", safety_training)
    print("Fatigue level:", fatigue_level)

    # Print warnings for individual safety problems and a combined alert when all three occur.
    # Safety analysis and warnings
    if ppe_compliance == "No":
        print("Warning: PPE non-compliance")

    if safety_training == "Incomplete":
        print("Warning: Safety training incomplete")

    if fatigue_level == "High":
        print("Warning: High fatigue level")

    if (ppe_compliance == "No" and
            safety_training == "Incomplete" and
            fatigue_level == "High"):
        print("ALERT: Multiple safety risks detected")


# Offer authorised users the ability to view, add, or remove accounts.
# Manage Users
elif menu_choice == "8" and has_access("Manage user"):

    print("Manage Users")
    print("1. View users")
    print("2. Add user")
    print("3. Remove user")

    manage_user_choice = input("Select 1, 2 or 3: ")


    # View users
    if manage_user_choice == "1":
        print(users)


    # Add user
    elif manage_user_choice == "2":

        worker_id = input("Enter Worker ID: ")
        new_username = input("Enter username: ")
        new_password = input("Enter password: ")
        new_user_role = input("Enter Role: ")

        # Prevent adding an account with a Worker ID or username that already exists.
        if worker_id in users["Worker ID"].values:
            print("Worker ID already exists")

        elif new_username in users.Username.values:
            print("Username already exists")

        else:
            # Create and save a new account only after both uniqueness checks pass.
            new_user = pd.DataFrame(
                [[worker_id, new_username, new_password, new_user_role]],
                columns=["Worker ID", "Username", "Password", "Role"]
            )

            users = pd.concat([users, new_user])

            users.to_csv("C:/Users/Katleho Mofokeng/Desktop/users.csv",
                         index=False)

            print("User added successfully")
            print(users)


    # Remove user
    elif manage_user_choice == "3":

        # Remove the chosen account by filtering it out of the users DataFrame.
        remove_username = input("Enter username to remove: ")

        if remove_username in users.Username.values:

            users = users[users.Username != remove_username]

            users.to_csv("C:/Users/Katleho Mofokeng/Desktop/users.csv",
                         index=False)

            print("User removed successfully")
            print(users)

        else:
            print("Username not found")

    else:
        print("Invalid selection")


# These branches currently print module labels for the other group features.
# Other group modules
elif menu_choice == "1" and has_access("View Dashboard"):
    print("Dashboard module")

elif menu_choice == "3" and has_access("Safety incidents"):
    print("Safety Incidents module")

elif menu_choice == "4" and has_access("Equipment data"):
    print("Equipment Data module")

elif menu_choice == "5" and has_access("Maintenance data"):
    print("Maintenance Data module")

elif menu_choice == "6" and has_access("Risk Assessment"):
    print("Risk Assessment module")

elif menu_choice == "7" and has_access("Generate reports"):
    print("Generate Reports module")

else:
    print("Invalid selection or access denied")
    
    
# Start the incident-management section using the incident CSV file.
import pandas as pd

df = pd.read_csv(r"C:\Users\senam\Downloads\incidents.csv")
print(df)
print(df.columns.tolist())


# Collect incident details, calculate severity, and append the new incident record.
def add_incident():

    print("\n     ADD NEW INCIDENT     ")

    # Get incident information from the user
    incident_id = input("Enter Incident ID: ")
    worker_id = input("Enter Worker ID: ")

    # Department
    print("\nDepartments:")
    print("1. Mining")
    print("2. Processing")
    print("3. Maintenance")
    print("4. Engineering")

    department_choice = input("Select department (1-4): ")

    # Translate the numeric department choice into a department name.
    departments = {
        "1": "Mining",
        "2": "Processing",
        "3": "Maintenance",
        "4": "Engineering"
    }

    department = departments.get(department_choice, "Mining")

    # Date
    date = input("Enter Date (e.g. 8/21/2026): ")

    # Shift
    shift = input("Enter Shift (Day/Night): ")

    # Incident type
    print("\nIncident Types:")
    print("1. Slip/Fall")
    print("2. Equipment")
    print("3. PPE")
    print("4. Injury")

    incident_choice = input("Select incident type (1-4): ")

    # Translate the numeric incident-type choice into a descriptive category.
    incident_types = {
        "1": "Slip/Fall",
        "2": "Equipment",
        "3": "PPE",
        "4": "Injury"
    }

    incident_type = incident_types.get(incident_choice, "Other")

    # Description and cause
    description = input("Enter incident description: ")
    cause = input("Enter cause: ")

    # Likelihood and consequence
    likelihood = int(input("Enter likelihood (1-5): "))
    consequence = int(input("Enter consequence (1-5): "))

    # Multiply likelihood by consequence to obtain the incident risk score.
    # Calculate risk score
    risk_score = likelihood * consequence

    # Classify the calculated risk score using the defined severity ranges.
    # Determine severity
    if risk_score <= 4:
        severity = "Low"
    elif risk_score <= 9:
        severity = "Medium"
    elif risk_score <= 16:
        severity = "High"
    else:
        severity = "Critical"

    # Incident status
    print("\nIncident Status:")
    print("1. Open")
    print("2. Closed")
    print("3. Under Investigation")

    status_choice = input("Select status (1-3): ")

    # Translate the selected status into the incident status text.
    statuses = {
        "1": "Open",
        "2": "Closed",
        "3": "Under Investigation"
    }

    incident_status = statuses.get(status_choice, "Open")

    # Prepare a dictionary whose keys match the incident database fields.
    # Create the new incident
    new_row = {
        "Incident_ID": incident_id,
        "Worker_ID": worker_id,
        "Department": department,
        "Date": date,
        "Shift": shift,
        "Incident_Type": incident_type,
        "Description": description,
        "Cause": cause,
        "Severity": severity,
        "Incident_Status": incident_status,
        "Likelihood": likelihood,
        "Consequence": consequence
    }

    # Append the new incident to the in-memory DataFrame and write it to CSV.
    # Add the incident to the database
    global df
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # Save the updated database
    df.to_csv("risk_database.csv", index=False)

    print("\n--------------------------------")
    print("Incident successfully added!")
    print("Risk Score:", risk_score)
    print("Severity:", severity)
    print("--------------------------------")

    print("\n Updated Incident Database:")
    display(df.tail())


add_incident()


# Filter incidents according to the category selected by the user.
def filter_incidents():
    print("\n    FILTER INCIDENTS     ")
    print("1. Filter by Department")
    print("2. Filter by Incident Type")
    print("3. Filter by Severity")
    print("4. Filter by Incident Status")
    print("5. Back to Main Menu")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        department = input("Enter Department: ")
        result = df[df["Department"].str.lower() == department.lower()]

    elif choice == "2":
        incident_type = input("Enter Incident Type: ")
        result = df[df["Incident_Type"].str.lower() == incident_type.lower()]

    elif choice == "3":
        severity = input("Enter Severity: ")
        result = df[df["Severity"].str.lower() == severity.lower()]

    elif choice == "4":
        status = input("Enter Incident Status: ")
        result = df[df["Incident_Status"].str.lower() == status.lower()]

    elif choice == "5":
        return

    else:
        print("Invalid choice.")
        return

    if result.empty:
        print("\nNo incidents found matching your filter.")
    else:
        print("\n     FILTERED INCIDENTS     ")
        display(result)


# Keep the incident management menu active until the user selects Exit.
def main_menu():
    while True:
        print("\n")
        print("   INCIDENT MANAGEMENT SYSTEM")
        print("1. Add New Incident")
        print("2. View All Incidents")
        print("3. Search Incident")
        print("4. Count Total Number Of Incidents")
        print("5. Filter Incidents")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_incident()

        elif choice == "2":
            print("\n ALL INCIDENTS ")
            display(df)

        elif choice == "3":
            incident_id = input("Enter Incident ID to search: ")

            # Search for an incident by matching its Incident_ID.
            result = df[df["Incident_ID"] == incident_id]

            if result.empty:
                print("\nIncident not found.")
            else:
                print("\n INCIDENT FOUND ")
                display(result)

        # Count all incident records currently stored in the DataFrame.
        elif choice == "4":
            total_incidents = len(df)

            print("\n INCIDENT COUNT ")
            print("Total number of incidents:", total_incidents)

        elif choice == "5":
            filter_incidents() #calling filter incidents function

        elif choice == "6":
            print("\nExiting Incident Management System")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

main_menu()

# Start equipment-condition and maintenance analysis.
import pandas as pd

df = pd.read_csv("equipment.csv")

print(f"Loaded {len(df)} equipment records, {len(df.columns)} columns.")
df.head(10)


# Assess temperature and vibration separately, then return the most severe condition.
def check_equipment_status(temperature, vibration):
    """
    Monitors equipment condition based on temperature and vibration inputs.
    Returns the overall severity status and an appropriate status message.
    """
    # Temperature is critical above 100 and warning from 80 through 100.
    # Temperature Threshold Checks
    if temperature > 100:
        temp_status = "CRITICAL"
    elif 80 <= temperature <= 100:
        temp_status = "WARNING"
    else:
        temp_status = "NORMAL"

    # Vibration is critical above 8 and warning from 5 through 8.
    # Vibration Threshold Checks
    if vibration > 8:
        vib_status = "CRITICAL"
    elif 5 <= vibration <= 8:
        vib_status = "WARNING"
    else:
        vib_status = "NORMAL"

    # If either measurement is critical, the combined equipment status is critical.
    # Determine the overall status based on highest severity
    if temp_status == "CRITICAL" or vib_status == "CRITICAL":
        status = "CRITICAL"
        reasons = []

        if temp_status == "CRITICAL":
            reasons.append("temperature exceeds predefined threshold")

        if vib_status == "CRITICAL":
            reasons.append("vibration exceeds predefined threshold")

        message = f"CRITICAL: Equipment {' and '.join(reasons)}. Inspection required"

    elif temp_status == "WARNING" or vib_status == "WARNING":
        status = "WARNING"
        reasons = []

        if temp_status == "WARNING":
            reasons.append("temperature approaching predefined threshold")

        if vib_status == "WARNING":
            reasons.append("vibration approaching predefined threshold")

        message = f"WARNING: Equipment {' and '.join(reasons)}."

    else:
        status = "NORMAL"
        message = "NORMAL: Equipment operating within defined monitoring limits."

    return status, message


# Example test case
current_status, current_msg = check_equipment_status(
    temperature=95,
    vibration=4
)

print(current_status)
print(current_msg)


# Apply the monitoring function to each equipment row and store its returned values.
# applying temperature and vibration conditions to every row of the real equipment database
results = df.apply(
    lambda row: check_equipment_status(
        row["Temperature"],
        row["Vibration"]
    ),
    axis=1
)

df["Status"] = results.apply(lambda x: x[0])
df["Status_Message"] = results.apply(lambda x: x[1])

df[[
    "Equipment_ID",
    "Equipment_Type",
    "Temperature",
    "Vibration",
    "Status",
    "Status_Message"
]]


# Count the number of equipment records in each condition category.
#how many pieces of equipment fall into each status
df["Status"].value_counts()


# Display only equipment classified as warning or critical.
# Just the equipment that needs attention (WARNING or CRITICAL)
df[df["Status"] != "NORMAL"][[
    "Equipment_ID",
    "Equipment_Type",
    "Temperature",
    "Vibration",
    "Status",
    "Status_Message"
]]


# Calculate availability and flag conditions that may require maintenance attention.
# Calculates Availability and stores Maintenance Status
def check_equipment_maintenance(equipment):
    """
    Takes a dictionary describing one piece of equipment and returns:
    - availability (%)
    - a list of maintenance flags (reasons it needs attention)
    Does not print anything itself, so it can be reused for one device
    or looped across the whole equipment database.
    """

    # Total time is operating time plus downtime.
    total_time = (
        equipment["operating_time"] +
        equipment["downtime"]
    )

    # Availability is operating time divided by total time, multiplied by 100.
    availability = (
        equipment["operating_time"] /
        total_time * 100
    ) if total_time > 0 else 0

    # Collect separate maintenance flags for each applicable condition.
    flags = []

    if equipment["status"] == "Due":
        flags.append("Due for maintenance")

    if equipment["status"] == "Overdue":
        flags.append("Overdue equipment")

    if equipment["status"] == "Under Maintenance":
        flags.append("Equipment under maintenance")

    if equipment["downtime"] > 15:
        flags.append("Excessive downtime")

    if equipment["alerts"] > 2:
        flags.append("Repeated alerts")

    if availability < 85:
        flags.append("Low availability")

    return availability, flags


# Print the availability and maintenance flags for a single device.
def print_maintenance_report(equipment):
    """Prints a readable report for ONE device — handy for manual spot-checks."""

    availability, flags = check_equipment_maintenance(equipment)

    print(f"--- Monitoring Report for: {equipment['name']} ---")
    print(f"Availability: {availability:.1f}%")

    if flags:
        for f in flags:
            print(f)

    else:
        print("No maintenance concerns flagged.")


# Define a sample device to demonstrate the maintenance report.
sample_device = {
    "name": "pump-01",
    "operating_time": 120,
    "downtime": 60,
    "status": "Due",
    "alerts": 5
}

print_maintenance_report(sample_device)


# Apply maintenance calculations to every equipment record in the DataFrame.
#applying it to every row of the real equipment database
def apply_maintenance_to_df(df):

    availabilities = []
    flags_list = []

    # Convert each DataFrame row into the dictionary expected by the maintenance function.
    for _, row in df.iterrows():

        equipment = {
            "name": row["Equipment_ID"],
            "operating_time": row["Operating_Time"],
            "downtime": row["Downtime"],
            "status": row["Maintenance_Status"],
            "alerts": row["Alert_Count"],
        }

        availability, flags = check_equipment_maintenance(equipment)

        availabilities.append(round(availability, 1))
        flags_list.append("; ".join(flags) if flags else "None")

    # Add the calculated availability and maintenance notes as DataFrame columns.
    df["Calculated_Availability"] = availabilities
    df["Maintenance_Flags"] = flags_list

    return df


df = apply_maintenance_to_df(df)

df[[
    "Equipment_ID",
    "Maintenance_Status",
    "Downtime",
    "Alert_Count",
    "Calculated_Availability",
    "Maintenance_Flags"
]]

# Start the combined safety alert and dashboard section.
import pandas as pd


# Load worker, incident, and equipment data for central monitoring.
# LOAD DATA

workers = pd.read_csv("workers.csv")
incidents = pd.read_csv("incidents.csv")
equipment = pd.read_csv("equipment (1).csv")


# CHECK THAT DATA LOADED


# Each alert function maps an observed condition to an alert label.
# ALERT AND RISK LOGIC

# Temperature above 100 is critical; values from 80 are warnings.
# TEMPERATURE ALERT
def temperature_alert(temp):
    if temp > 100:
        return "Critical"
    elif temp >= 80:
        return "Warning"
    else:
        return "Normal"


# Vibration above 8 is critical; values from 5 are warnings.
# VIBRATION ALERT
def vibration_alert(vibration):
    if vibration > 8:
        return "Critical"
    elif vibration >= 5:
        return "Warning"
    else:
        return "Normal"


# Flag only incidents whose severity text is Critical.
# INCIDENT ALERT
def incident_alert(severity):
    if str(severity).strip().lower() == "critical":
        return "CRITICAL INCIDENT"
    else:
        return "NO ALERT"


# Flag workers whose PPE compliance is recorded as No.
# PPE ALERT
def ppe_alert(ppe):
    if str(ppe).strip().lower() == "no":
        return "LOW PPE COMPLIANCE"
    else:
        return "NO ALERT"


# Flag workers whose fatigue level is recorded as High.
# FATIGUE ALERT
def fatigue_alert(fatigue):
    if str(fatigue).strip().lower() == "high":
        return "HIGH FATIGUE"
    else:
        return "NO ALERT"


# Apply the alert functions to the appropriate columns in each dataset.
# APPLY ALERT FUNCTIONS
equipment["Temperature_Alert"] = equipment["Temperature"].apply(temperature_alert)

equipment["Vibration_Alert"] = equipment["Vibration"].apply(vibration_alert)

incidents["Incident_Alert"] = incidents["Severity"].apply(incident_alert)

workers["PPE_Alert"] = workers["PPE compliance"].apply(ppe_alert)

workers["Fatigue_Alert"] = workers["Fatigue level"].apply(fatigue_alert)


# Calculate the incident risk score as likelihood multiplied by consequence.
# RISK SCORE
incidents["Risk_Score"] = (
    incidents["Likelihood"] * incidents["Consequence"]
)


# Convert numerical risk scores into Low, Medium, High, or Critical categories.
# RISK LEVEL
def risk_level(score):
    if score >= 17:
        return "Critical"
    elif score >= 10:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"


incidents["Risk_Level"] = incidents["Risk_Score"].apply(risk_level)


# Collect all individual alert records in one central list.
# CENTRAL ALERT SYSTEM

central_alerts = []


# Add non-normal temperature conditions to the central alert list.
# 1. TEMPERATURE ALERTS
for index, row in equipment.iterrows():
    if str(row["Temperature_Alert"]).strip().lower() != "normal":
        central_alerts.append({
            "Source": "Equipment",
            "ID": row["Equipment_ID"],
            "Alert_Type": "Temperature",
            "Level": row["Temperature_Alert"]
        })


# Add non-normal vibration conditions to the central alert list.
# 2. VIBRATION ALERTS
for index, row in equipment.iterrows():
    if str(row["Vibration_Alert"]).strip().lower() != "normal":
        central_alerts.append({
            "Source": "Equipment",
            "ID": row["Equipment_ID"],
            "Alert_Type": "Vibration",
            "Level": row["Vibration_Alert"]
        })


# Add incidents flagged as critical to the central alert list.
# 3. CRITICAL INCIDENT ALERTS
for index, row in incidents.iterrows():
    if str(row["Incident_Alert"]).strip().lower() != "no alert":
        central_alerts.append({
            "Source": "Incident",
            "ID": row["Incident_ID"],
            "Alert_Type": "Critical Incident",
            "Level": "Critical"
        })


# Add worker PPE non-compliance warnings to the central alert list.
# 4. PPE ALERTS
for index, row in workers.iterrows():
    if str(row["PPE_Alert"]).strip().lower() != "no alert":
        central_alerts.append({
            "Source": "Worker",
            "ID": row["Worker ID"],
            "Alert_Type": "PPE Compliance",
            "Level": "Warning"
        })


# Add high-fatigue worker warnings to the central alert list.
# 5. FATIGUE ALERTS
for index, row in workers.iterrows():
    if str(row["Fatigue_Alert"]).strip().lower() != "no alert":
        central_alerts.append({
            "Source": "Worker",
            "ID": row["Worker ID"],
            "Alert_Type": "High Fatigue",
            "Level": "Warning"
        })


# Add alerts for equipment whose maintenance status is Overdue.
# 6. OVERDUE MAINTENANCE ALERTS
for index, row in equipment.iterrows():
    if str(row["Maintenance_Status"]).strip().lower() == "overdue":
        central_alerts.append({
            "Source": "Equipment",
            "ID": row["Equipment_ID"],
            "Alert_Type": "Overdue Maintenance",
            "Level": "Warning"
        })


# Add alerts for incidents classified as High risk.
# 7. HIGH-RISK OBSERVATION ALERTS
for index, row in incidents.iterrows():
    if str(row["Risk_Level"]).strip().lower() == "high":
        central_alerts.append({
            "Source": "Incident",
            "ID": row["Incident_ID"],
            "Alert_Type": "High-Risk Observation",
            "Level": "High"
        })


# Identify unusually high downtime using the dataset's 75th-percentile threshold.
# 8. EXCESSIVE DOWNTIME ALERTS
# Prototype threshold: equipment above the dataset's 75th percentile

downtime_threshold = equipment["Downtime"].quantile(0.75)

for index, row in equipment.iterrows():
    if row["Downtime"] > downtime_threshold:
        central_alerts.append({
            "Source": "Equipment",
            "ID": row["Equipment_ID"],
            "Alert_Type": "Excessive Downtime",
            "Level": "Warning"
        })


# Convert the accumulated alert dictionaries into a DataFrame.
# CONVERT ALERT LIST TO DATAFRAME

alerts_df = pd.DataFrame(central_alerts)


# Calculate summary indicators used by the central dashboard.
# CENTRAL DASHBOARD KPIs

# Count the workers, incidents, equipment records, and active alerts.
# 1. BASIC KPIs
total_workers = len(workers)
total_incidents = len(incidents)
total_equipment = len(equipment)
total_alerts = len(alerts_df)


# Summarise near misses and the percentage of workers marked PPE-compliant.
# 2. WORKER SAFETY KPIs

# Total near misses
total_near_misses = workers["Near misses"].sum()

# PPE compliance percentage
ppe_compliance_rate = (
    workers["PPE compliance"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("yes")
    .mean() * 100
)


# Count incident observations whose risk scores are at least 10.
# 3. INCIDENT RISK KPI

# Risk Score = Likelihood × Consequence
incidents["Risk_Score"] = (
    incidents["Likelihood"] * incidents["Consequence"]
)

# High and Critical risk observations
high_risk_observations = (
    incidents["Risk_Score"] >= 10
).sum()


# Summarise equipment availability and maintenance statuses.
# 4. EQUIPMENT KPIs

# Equipment currently under maintenance
under_maintenance = (
    equipment["Maintenance_Status"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("under maintenance")
    .sum()
)

# Equipment not currently under maintenance
available_equipment = total_equipment - under_maintenance

# Overdue maintenance
overdue_maintenance = (
    equipment["Maintenance_Status"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("overdue")
    .sum()
)

# Compute the mean of the equipment Availability column.
# Average equipment availability
average_availability = equipment["Availability"].mean()


# Count equipment-related alerts and the subset labelled Critical.
# 5. ALERT KPIs

# Total equipment alerts
equipment_alerts = (
    alerts_df["Source"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("equipment")
    .sum()
)

# Critical equipment alerts
critical_equipment_alerts = (
    (alerts_df["Source"].str.strip().str.lower() == "equipment") &
    (alerts_df["Level"].str.strip().str.lower() == "critical")
).sum()


# Print the final central dashboard statistics.
# DISPLAY DASHBOARD KPIs

print("CENTRAL DASHBOARD")
print("-----------------------------")

print("Total Workers:", total_workers)
print("Total Incidents:", total_incidents)
print("Total Near Misses:", total_near_misses)
print("High-Risk Observations:", high_risk_observations)
print("PPE Compliance Rate:", round(ppe_compliance_rate, 1), "%")

print()

print("Total Equipment:", total_equipment)
print("Available Equipment:", available_equipment)
print("Equipment Under Maintenance:", under_maintenance)
print("Overdue Maintenance:", overdue_maintenance)
print("Average Equipment Availability:", round(average_availability, 2), "%")

print()

print("Active Alerts:", total_alerts)
print("Equipment Alerts:", equipment_alerts)
print("Critical Equipment Alerts:", critical_equipment_alerts)