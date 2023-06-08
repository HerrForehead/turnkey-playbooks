from pyVim import connect
from pyVmomi import vim

# vSphere connection details
vcenter_hostname = 'vcenter.netlab.fhict.nl'
vcenter_user = 'PRO35@fhict.nl'
vcenter_pass = 'Wmy4CqMXY'

def retrieve_network_devices():
    try:
        # Connect to vSphere
        service_instance = connect.SmartConnectNoSSL(
            host=vcenter_hostname,
            user=vcenter_user,
            pwd=vcenter_pass
        )

        # Retrieve the content
        content = service_instance.RetrieveContent()

        # Get the root folder
        root_folder = content.rootFolder

        # Retrieve all datacenters in the vSphere inventory
        datacenters = root_folder.childEntity
        for datacenter in datacenters:
            # Retrieve all networks in the datacenter
            networks = datacenter.networkFolder.childEntity
            for network in networks:
                print(f"Network: {network.name}")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        # Disconnect from vSphere
        connect.Disconnect(service_instance)

# Retrieve and display network devices
retrieve_network_devices()
