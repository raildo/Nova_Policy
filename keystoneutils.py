from keystoneclient.v3 import client
from keystoneclient.v2_0 import client as clientv2

import sys


def create_client(v, username, password, project_name, project_domain_name, user_domain_name, auth_url):
    if v == "2":
        return clientv2.Client(username=username, password=password, tenant_name=project_name, auth_url=(auth_url + "/v2.0"))
    else:
        return client.Client(username=username, password=password, project_name=project_name, project_domain_name=project_domain_name, user_domain_name=user_domain_name, auth_url=(auth_url + "/v3"))

def find_user(client, name):
    return client.users.find(name=name)


def find_project(client, name):
    return client.tenants.find(name=name)


def find_domain(client, name):
    return client.domains.find(name=name)


def find_role(client, name):
    return client.roles.find(name=name)

def create_domain(client, name):
    try:
        d = client.domains.create(name=name)
    except Exception:
        d = find_domain(client, name)
    return d


def create_project(client, name):
    try:
        if (client.version == 'v2.0'):
            p = client.tenants.create(tenant_name=name)
        else:
            p = client.projects.create(name, description='optional')
    except Exception:
        p = find_project(client, name)
    return p


def create_user(client, name, password, email, default_project):
    try:
        u = client.users.create(name=name, password=password,
                                email=email,
                                tenant_id=default_project,
                                enabled=True)
    except Exception:
        u = find_user(client, name)
    return u


def create_group(client, name, domain):
    try:
        u = client.users.create(name=name,
                                description='optional',
                                domain=domain)
    except Exception:
        u = find_user(client, name)
    return u


def create_role(client, name):
    try:
        r = client.roles.create(name=name)
    except Exception:
        r = find_role(client, name)
    return r

def remove_role(client, role):
    client.roles.delete(role)

def remove_project(client, project):
    if (client.version == 'v2.0'):
        client.tenants.delete(project)

def remove_user(client, user):
    if (client.version == 'v2.0'):
        client.users.delete(user)

def get_roles_for_user(client, user, project):
    if (client.version == 'v2.0'):
        client.roles.roles_for_user(user=user, tenant=project)

def grant_project_role(client, role, user, project):
    if (client.version == 'v2.0'):
        client.roles.add_user_role(user=user, role=role, tenant=project)


def grant_domain_role(client, role, user, domain):
    client.roles.grant(role, user=user, domain=domain)


def grant_group_project_role(client, role, user, project):
    client.roles.grant(role, user=user, project=project)


def grant_group_domain_role(client, role, user, domain):
    client.roles.grant(role, user=user, domain=domain)
