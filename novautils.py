from novaclient.v1_1 import client

def create_client(username, password, projectid, auth_url):
    return client.Client(username,
                         password,
                         project_id=projectid,
                         tenant_id=projectid,
                         auth_url=auth_url)


def get_all_servers(client):
    return client.servers.list()

def get_server(client, name):
    return client.servers.get(name)

def create_server(client, name, image, flavor):
    return client.servers.create(name, image, flavor)

def delete_server(client, name):
    return client.servers.delete(name)

def get_all_flavors(client):
    return client.flavors.list()

## FLAVORS
def create_flavor(client, name, ram, vcpus, disk, flavorid, public=True):
    return client.flavors.create(name, ram, vcpus,
                                 disk, flavorid=flavorid,
                                 is_public=public)

def delete_flavor(client, name):
    return client.flavors.delete(name)

def get_flavor(client, name):
    return client.flavors.get(name)

def add_flavor_tenant_access(client, flavor, tenant):
    return client.flavor_access.add_tenant_access(flavor, tenant)

def remove_flavor_tenant_access(client, flavor, tenant):
    return client.flavor_access.remove_tenant_access(flavor, tenant)

def list_flavor_tenant_access(client, flavor=None, tenant=None):
    return client.flavor_access.list(flavor=flavor, tenant=tenant)

## SERVER ACTIONS
def change_password(client, server, password):
    return client.servers.change_password(server, password)

def reboot(client, server, reboot_type='SOFT'):
    return client.servers.reboot(server, reboot_type)

def rebuild(client, server, image):
    return client.servers.rebuild(server, image)

def  resize(client, server, flavor):
    return client.servers.resize(server, flavor)

def  confirm_resize(client, server):
    return client.servers.confirm_resize(server)

def get_server_status(client, server):
    server = get_server(client, server)
    return server.status

def stop(client, server):
    return client.servers.stop(server)

def start(client, server):
    return client.servers.start(server)

def pause(client, server):
    return client.servers.pause(server)

def unpause(client, server):
    return client.servers.unpause(server)

def suspend(client, server):
    return client.servers.suspend(server)

def resume(client, server):
    return client.servers.resume(server)

def lock(client, server):
    return client.servers.lock(server)

def unlock(client, server):
    return client.servers.unlock(server)

def host_list(client):
    return client.hosts.list()

def get_host(client, host):
    return client.hosts.get(host)

def shutdown_host(client, host):
    return client.hosts.host_action(host, "SHUTDOWN")

def reboot_host(client, host):
    return client.hosts.host_action(host, "REBOOT")

def start_host(client, host):
    return client.hosts.host_action(host, "STARTUP")
