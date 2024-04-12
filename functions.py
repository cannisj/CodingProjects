import psutil
import wmi 

def get_hardware_info():
    c = wmi.WMI() # Create a connection to WMI
    system_info = {} # Initialize a dictionary to store the system information

    # Get CPU Information 
    try:
        processor = c.Win32_Processor()[0] # Fetch processor details using WMI
        system_info['Processor'] = processor.Name
        system_info['Cores'] = processor.NumberOfCores
    except wmi.x_wmi: # Catch potential WMI errors
        print("Error retrieving detailed hardware information using WMI.")
        system_info['Processor'] = "Unknown" # Set default values if WMI fails

    # Get RAM Information
    mem = psutil.virtual_memory() # Fetch RAM details using psutil
    system_info['Total Memory'] = f"{mem.total / (1024**3):.2f} GB"

    # Get Disk Information 
    system_info['Disks'] = []
    for disk in psutil.disk_partitions(): # Iterate through all disk partitions
        disk_info = {}
        disk_info['Device'] = disk.device
        disk_info['Mount Point'] = disk.mountpoint
        disk_info['File System'] = disk.fstype
        disk_info['Total Size'] = f"{psutil.disk_usage(disk.mountpoint).total / (1024**3):.2f} GB"
        system_info['Disks'].append(disk_info)

    return system_info

def get_software_info():
    try:
        c = wmi.WMI()
        software_list = []
        for software in c.Win32_Product(): # Query WMI for installed software
            software_list.append(software.Name)
        return software_list
    except wmi.x_wmi:
        print("Error retrieving software information using WMI.")
        return [] # Return an empty list if WMI fails

def get_network_info():
    try:
        c = wmi.WMI()
        network_adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True) # Query WMI for enabled network adapters
        network_info = []
        for adapter in network_adapters: # Iterate through network adapters
            adapter_info = {}
            adapter_info['Description'] = adapter.Description
            adapter_info['IP Addresses'] = adapter.IPAddress 
            adapter_info['MAC Address'] = adapter.MACAddress
            network_info.append(adapter_info)
        return network_info
    except wmi.x_wmi:
        print("Error retrieving network information using WMI.")
        return [] S