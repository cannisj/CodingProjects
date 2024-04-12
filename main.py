import functions as func

def print_info(data, title):
    print(f"\n--- {title} ---")
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}")
    elif isinstance(data, list): 
        for item in data:
            if isinstance(item, dict): # Handle nested dictionaries for network adapters
                for key, value in item.items():
                    print(f"{key}: {value}")
            else:
                print(item) # Print other list items (if any)
    else:
        print("Unsupported data type")

if __name__ == "__main__":
    # Retrieves system information using functions from 'functions.py'
    hardware_info = func.get_hardware_info()
    software_list = func.get_software_info()
    network_info = func.get_network_info()

    # Calls the print_info function to display results neatly 
    print_info(hardware_info, "Hardware Information")
    print("\n--- Installed Software (List) ---") 
    for software in software_list:
        print(software)

    print_info(network_info, "Network Information")