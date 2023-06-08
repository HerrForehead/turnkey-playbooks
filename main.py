from pyVim import connect

# vSphere connection details
vcenter_hostname = 'vcenter.netlab.fhict.nl'
vcenter_user = 'PRO35@fhict.nl'
vcenter_pass = 'Wmy4CqMXY'

def list_entities(entity):
    if hasattr(entity, 'childEntity'):
        # Entity is a folder, recursively list its child entities
        for child in entity.childEntity:
            list_entities(child)
    elif isinstance(entity, vim.Network):
        # Entity is a network
        print(f"Network: {entity.name}")

# Connect to vSphere
service_instance = connect.SmartConnect(
    host=vcenter_hostname,
    user=vcenter_user,
    pwd=vcenter_pass
)

try:
    # Retrieve the content
    content = service_instance.RetrieveContent()

    # Get the root folder
    root_folder = content.rootFolder

    # Recursively list child entities starting from the root folder
    list_entities(root_folder)

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Disconnect from vSphere
    connect.Disconnect(service_instance)
