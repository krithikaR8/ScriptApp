import time
def my_script():
    
    import pandas as pd
    df = pd.read_excel(r"E:\dumy\extracted_values.xlsx",header=4)
    df
    df.columns
    print(df)
    
    # Add your script logic here
    df.to_excel(r"E:\dumy\output.xlsx", engine='openpyxl')
    print("Script execution started")
    
    # Simulate a 10-second process
    for i in range(10, 0, -1):
        print("Processing... Time remaining:", i, "seconds")
        time.sleep(1)
   