import unittest
import keystoneutils
import novautils
import time

class NovaPolicyTests(unittest.TestCase):

    PROJECT                   = "Project"
    OTHER_PROJECT             = "OtherProject"

    CLOUD_ADMIN_ROLE          = "cloud_admin"
    CLOUD_ADMIN_PASSWD        = "stack123"
    CLOUD_ADMIN_USER          = "BigBoss"
    CLOUD_ADMIN_OTHER_USER    = "OtherBigBoss"

    PROJECT_ADMIN_ROLE        = "project_admin"
    PROJECT_ADMIN_PASSWD      = "stack123"
    PROJECT_ADMIN_USER        = "Boss"
    PROJECT_ADMIN_OTHER_USER  = "OtherBoss"

    PROJECT_MEMBER_ROLE       = "project_member"
    PROJECT_MEMBER_PASSWD     = "stack123"
    PROJECT_MEMBER_USER       = "Minion"
    PROJECT_MEMBER_OTHER_USER = "OtherMinion"

    ADMIN_USER                = "admin"
    ADMIN_PASSWD              = "supersecret"
    ADMIN_PROJECT             = "admin"
    ADMIN_PROJECT_DOMAIN      = "Default"
    ADMIN_DOMAIN              = "Default"

    MY_SERVER_PASSWORD = "pass"
    OTHER_SERVER_PASSWORD = "nopass"
    LAST_SERVER_PASSWORD = "maypass"


    KEYSTONE_AUTH_URL = "http://10.1.0.68:5000"
    NOVA_AUTH_URL = "http://10.1.0.68:8774"

    # Authenticate with admin
    admin_client = keystoneutils.create_client("2", username=ADMIN_USER,
                                                        password=ADMIN_PASSWD,
                                                        project_name=ADMIN_PROJECT,
                                                        project_domain_name=ADMIN_PROJECT_DOMAIN,
                                                        user_domain_name=ADMIN_DOMAIN,
                                                        auth_url=KEYSTONE_AUTH_URL)

    project       = keystoneutils.create_project(admin_client, PROJECT)
    other_project = keystoneutils.create_project(admin_client, OTHER_PROJECT)


    cloud_admin_role     = keystoneutils.create_role(admin_client, CLOUD_ADMIN_ROLE)
    cloud_admin          = keystoneutils.create_user(admin_client, CLOUD_ADMIN_USER      , CLOUD_ADMIN_PASSWD, '', project.id)
    other_cloud_admin    = keystoneutils.create_user(admin_client, CLOUD_ADMIN_OTHER_USER, CLOUD_ADMIN_PASSWD, '', other_project.id)
    keystoneutils.grant_project_role(admin_client, role=cloud_admin_role, user=cloud_admin      , project=project)
    keystoneutils.grant_project_role(admin_client, role=cloud_admin_role, user=other_cloud_admin, project=other_project)

    project_admin_role   = keystoneutils.create_role(admin_client, PROJECT_ADMIN_ROLE)
    project_admin        = keystoneutils.create_user(admin_client, PROJECT_ADMIN_USER      , PROJECT_ADMIN_PASSWD, '', project.id)
    other_project_admin  = keystoneutils.create_user(admin_client, PROJECT_ADMIN_OTHER_USER, PROJECT_ADMIN_PASSWD, '', other_project.id)
    keystoneutils.grant_project_role(admin_client, project_admin_role, project_admin, project)
    keystoneutils.grant_project_role(admin_client, project_admin_role, project_admin, other_project)

    project_member_role  = keystoneutils.create_role(admin_client, PROJECT_MEMBER_ROLE)
    project_member       = keystoneutils.create_user(admin_client, PROJECT_MEMBER_USER      , PROJECT_MEMBER_PASSWD, '', project.id)
    other_project_member = keystoneutils.create_user(admin_client, PROJECT_MEMBER_OTHER_USER, PROJECT_MEMBER_PASSWD, '', other_project.id)
    keystoneutils.grant_project_role(admin_client, project_member_role, project_member, project)
    keystoneutils.grant_project_role(admin_client, project_member_role, other_project_member, other_project)

    cloud_client         = keystoneutils.create_client("2", username=CLOUD_ADMIN_USER,
                                                          password=CLOUD_ADMIN_PASSWD,
                                                          project_name=PROJECT,
                                                          project_domain_name=ADMIN_PROJECT_DOMAIN,
                                                          user_domain_name=ADMIN_DOMAIN,
                                                          auth_url=KEYSTONE_AUTH_URL)
    other_cloud_client   = keystoneutils.create_client("2", username=CLOUD_ADMIN_OTHER_USER,
                                                          password=CLOUD_ADMIN_PASSWD,
                                                          project_name=OTHER_PROJECT,
                                                          project_domain_name=ADMIN_PROJECT_DOMAIN,
                                                          user_domain_name=ADMIN_DOMAIN,
                                                          auth_url=KEYSTONE_AUTH_URL)

    project_client       = keystoneutils.create_client("2", username=PROJECT_ADMIN_USER,
                                                          password=PROJECT_ADMIN_PASSWD,
                                                          project_name=PROJECT,
                                                          project_domain_name=ADMIN_PROJECT_DOMAIN,
                                                          user_domain_name=ADMIN_DOMAIN,
                                                          auth_url=KEYSTONE_AUTH_URL)
    other_project_client = keystoneutils.create_client("2", username=PROJECT_ADMIN_OTHER_USER,
                                                          password=PROJECT_ADMIN_PASSWD,
                                                          project_name=OTHER_PROJECT,
                                                          project_domain_name=ADMIN_PROJECT_DOMAIN,
                                                          user_domain_name=ADMIN_DOMAIN,
                                                          auth_url=KEYSTONE_AUTH_URL)

    member_client        = keystoneutils.create_client("2", username=PROJECT_MEMBER_USER,
                                                          password=PROJECT_MEMBER_PASSWD,
                                                          project_name=PROJECT,
                                                          project_domain_name=ADMIN_PROJECT_DOMAIN,
                                                          user_domain_name=ADMIN_DOMAIN,
                                                          auth_url=KEYSTONE_AUTH_URL)

    other_member_client  = keystoneutils.create_client("2", username=PROJECT_MEMBER_OTHER_USER,
                                                          password=PROJECT_MEMBER_PASSWD,
                                                          project_name=OTHER_PROJECT,
                                                          project_domain_name=ADMIN_PROJECT_DOMAIN,
                                                          user_domain_name=ADMIN_DOMAIN,
                                                          auth_url=KEYSTONE_AUTH_URL)

    ADMIN_PROJECT_ID = keystoneutils.find_project(admin_client, ADMIN_PROJECT).id
    PROJECT_ID = keystoneutils.find_project(admin_client, PROJECT).id
    OTHER_PROJECT_ID = keystoneutils.find_project(admin_client, OTHER_PROJECT).id

    #create_client(username, password, project_name, auth_url):
    nova_admin_client         = novautils.create_client(username=ADMIN_USER,
                                                        password=ADMIN_PASSWD,
                                                        projectid=ADMIN_PROJECT_ID,
                                                        auth_url=KEYSTONE_AUTH_URL + "/v2.0")

    #nova_cloud_client         = novautils.create_client(cloud_client        , KEYSTONE_AUTH_URL)
    #other_nova_cloud_client   = novautils.create_client(other_cloud_client  , KEYSTONE_AUTH_URL)
    #nova_project_client       = novautils.create_client(project_client      , KEYSTONE_AUTH_URL)
    #other_nova_project_client = novautils.create_client(other_project_client, KEYSTONE_AUTH_URL)
    #nova_member_client        = novautils.create_client(member_client       , KEYSTONE_AUTH_URL)
    nova_cloud_client = novautils.create_client(username=CLOUD_ADMIN_USER,
                                                          password=CLOUD_ADMIN_PASSWD,
                                                          projectid=PROJECT_ID,
                                                          auth_url=KEYSTONE_AUTH_URL + "/v2.0")
    nova_other_cloud_client = novautils.create_client(username=CLOUD_ADMIN_OTHER_USER,
                                                          password=CLOUD_ADMIN_PASSWD,
                                                          projectid=OTHER_PROJECT_ID,
                                                          auth_url=KEYSTONE_AUTH_URL + "/v2.0")
    nova_project_admin_client  = novautils.create_client(username=PROJECT_ADMIN_USER,
                                                          password=PROJECT_ADMIN_PASSWD,
                                                          projectid=PROJECT_ID,
                                                          auth_url=KEYSTONE_AUTH_URL + "/v2.0")
    other_nova_project_admin_client  = novautils.create_client(username=PROJECT_ADMIN_OTHER_USER,
                                                          password=PROJECT_ADMIN_PASSWD,
                                                          projectid=OTHER_PROJECT_ID,
                                                          auth_url=KEYSTONE_AUTH_URL + "/v2.0")
    nova_member_client  = novautils.create_client(username=PROJECT_MEMBER_USER,
                                                          password=PROJECT_MEMBER_PASSWD,
                                                          projectid=PROJECT_ID,
                                                          auth_url=KEYSTONE_AUTH_URL + "/v2.0")
    other_nova_member_client  = novautils.create_client(username=PROJECT_MEMBER_OTHER_USER,
                                                          password=PROJECT_MEMBER_PASSWD,
                                                          projectid=OTHER_PROJECT_ID,
                                                          auth_url=KEYSTONE_AUTH_URL + "/v2.0")
    FLAVOR_TINY_ID = "1"
    FLAVOR_SMALL_ID = "2"
    FLAVOR_NAME = "MY_FLAVOR"
    FLAVOR_ID = "11"
    OTHER_FLAVOR_NAME = "MY_OTHER_FLAVOR"
    OTHER_FLAVOR_ID = "111"
    LAST_FLAVOR_NAME = "MY_LAST_FLAVOR"
    LAST_FLAVOR_ID = "1111"
    FLAVOR_RAM = 1024
    FLAVOR_VCPUS = 1
    FLAVOR_DISK = 1024

    IMAGE_ID = '9045e59e-a580-4065-8650-bdb662ae4d8d'

    COUNT = '40'
    print "####################"
    print COUNT
    CLOUD_ADMIN_SERVER = "Cloud_admin_server" + COUNT
    PROJECT_ADMIN_SERVER = "Project_admin_server" + COUNT
    PROJECT_MEMBER_SERVER = "Project_member_server" + COUNT

    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$   VAI CRIAR ESSA BAGACA"
    SERVER_MEMBER = novautils.create_server(nova_cloud_client,
                           PROJECT_MEMBER_SERVER,
                           IMAGE_ID,
                           FLAVOR_TINY_ID)
    time.sleep(60)
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   ESSA PASSOU, BABACA"

    #IMAGE = nova_cloud_client.images.list()[0]
    #FLAVOR = nova_admin_client.flavors.list()[0]
    #print image

    def assertAnyRaise(self, callableObj):
        try:
            callableObj()
        except:
            return
        raise AssertionError('should raise an exception')

    def tearDown(self):

        '''#Remove Cloud Admin
        keystoneutils.remove_user(self.admin_client, self.cloud_admin)
        keystoneutils.remove_user(self.admin_client, self.other_cloud_admin)
        keystoneutils.remove_role(self.admin_client, self.cloud_admin_role)

        #Remove Project Admin
        keystoneutils.remove_user(self.admin_client, self.project_admin)
        keystoneutils.remove_user(self.admin_client, self.other_project_admin)
        keystoneutils.remove_role(self.admin_client, self.project_admin_role)

        #Remove member
        keystoneutils.remove_project(self.admin_client, self.project)
        keystoneutils.remove_project(self.admin_client, self.other_project)
        keystoneutils.remove_user(self.admin_client, self.project_member)
        keystoneutils.remove_user(self.admin_client, self.other_project_member)
        keystoneutils.remove_role(self.admin_client, self.project_member_role)'''

    def setUp(self):


        '''self.cloud_admin_image                  = glanceutils.create_image(self.glance_cloud_client      , "BigBoss_Image"     , visibility="public")
        self.cloud_admin_image_private          = glanceutils.create_image(self.glance_cloud_client      , "BigBoss_Image_Private")
        self.other_cloud_admin_image            = glanceutils.create_image(self.other_glance_cloud_client, "OtherBigBoss_Image", visibility="public")
        self.other_cloud_admin_image_private    = glanceutils.create_image(self.other_glance_cloud_client, "OtherBigBoss_Image_Private")

        self.project_admin_image                = glanceutils.create_image(self.glance_project_client      , "Boss_Image"     , visibility="public")
        self.project_admin_image_private        = glanceutils.create_image(self.glance_project_client      , "Boss_Image_Private")
        self.other_project_admin_image          = glanceutils.create_image(self.other_glance_project_client, "OtherBoss_Image", visibility="public")
        self.other_project_admin_image_private  = glanceutils.create_image(self.other_glance_project_client, "OtherBoss_Image_Private")

        self.project_member_image               = glanceutils.create_image(self.glance_member_client      , "Image"     , visibility="public")
        self.project_member_image_private       = glanceutils.create_image(self.glance_member_client      , "Image_Private")
        self.other_project_member_image         = glanceutils.create_image(self.other_glance_member_client, "OtherImage", visibility="public")
        self.other_project_member_image_private = glanceutils.create_image(self.other_glance_member_client, "OtherImage_Private")'''

        #print(glanceutils.check_get_image_list_has_images(self.glance_admin_client))'''


    ###################################
    ###            FLAVORS
    ###################################

    # Create and remove Flavor
    def test_project_admin_create_delete_flavors(self):
        novautils.create_flavor(self.nova_project_admin_client,
                                self.FLAVOR_NAME, self.FLAVOR_RAM,
                                self.FLAVOR_VCPUS, self.FLAVOR_DISK,
                                self.FLAVOR_ID)

        novautils.get_all_flavors(self.nova_project_admin_client)

        novautils.delete_flavor(self.nova_project_admin_client,
                        self.FLAVOR_ID)
    def test_cloud_admin_create_delete_flavors(self):
        novautils.create_flavor(self.nova_cloud_client,
                                self.OTHER_FLAVOR_NAME, self.FLAVOR_RAM,
                                self.FLAVOR_VCPUS, self.FLAVOR_DISK,
                                self.OTHER_FLAVOR_ID)

        novautils.delete_flavor(self.nova_cloud_client,
                        self.OTHER_FLAVOR_ID)

    def test_project_member_create_delete_flavors(self):
        self.assertAnyRaise(lambda:
          novautils.create_flavor(self.other_nova_member_client,
                                self.LAST_FLAVOR_NAME, self.FLAVOR_RAM,
                                self.FLAVOR_VCPUS, self.FLAVOR_DISK,
                                self.LAST_FLAVOR_ID))

        self.assertAnyRaise(lambda:
          novautils.delete_flavor(self.other_nova_member_client,
                  self.LAST_FLAVOR_ID))

    # List
    def test_list_flavors(self):
        novautils.get_all_flavors(self.nova_project_admin_client)
        novautils.get_all_flavors(self.nova_cloud_client)
        novautils.get_all_flavors(self.other_nova_member_client)

    # Flavor Detail
    def test_get_public_flavor(self):
        novautils.get_flavor(self.nova_project_admin_client, self.FLAVOR_TINY_ID)
        novautils.get_flavor(self.nova_cloud_client, self.FLAVOR_TINY_ID)
        novautils.get_flavor(self.other_nova_member_client, self.FLAVOR_TINY_ID)

    def test_get_private_flavor_project_member(self):

        novautils.get_all_flavors(self.nova_cloud_client)

        novautils.create_flavor(self.nova_cloud_client,
                                self.LAST_FLAVOR_NAME, self.FLAVOR_RAM,
                                self.FLAVOR_VCPUS, self.FLAVOR_DISK,
                                self.LAST_FLAVOR_ID, public=False)

        #The cloud admin can give access
        novautils.add_flavor_tenant_access(self.nova_cloud_client,
                                          self.LAST_FLAVOR_ID,
                                          self.PROJECT_ID)

        # Any member can get the details
        novautils.get_flavor(self.nova_cloud_client, self.LAST_FLAVOR_ID)

        novautils.get_flavor(self.nova_project_admin_client,
                             self.LAST_FLAVOR_ID)

        # A member from another project cannot access
        self.assertAnyRaise(lambda:
          novautils.get_flavor(self.other_nova_member_client, self.LAST_FLAVOR_ID))

        novautils.delete_flavor(self.nova_cloud_client,
                self.LAST_FLAVOR_ID)

    def test_add_access_private_flavor(self):

        novautils.create_flavor(self.nova_cloud_client,
                                self.OTHER_FLAVOR_NAME, self.FLAVOR_RAM,
                                self.FLAVOR_VCPUS, self.FLAVOR_DISK,
                                self.OTHER_FLAVOR_ID, public=False)

        #The project admin can give access
        novautils.add_flavor_tenant_access(self.nova_project_admin_client,
                                          self.OTHER_FLAVOR_ID,
                                          self.PROJECT_ID)

        #The project member can't give access
        self.assertAnyRaise(lambda:
          novautils.add_flavor_tenant_access(self.nova_member_client,
                                            self.OTHER_FLAVOR_ID,
                                            self.PROJECT_ID))

        novautils.get_flavor(self.other_nova_member_client, self.OTHER_FLAVOR_ID)

        novautils.delete_flavor(self.nova_cloud_client,
                self.OTHER_FLAVOR_ID)

    def test_remove_access_private_flavor(self):

        novautils.create_flavor(self.nova_cloud_client,
                                self.OTHER_FLAVOR_NAME, self.FLAVOR_RAM,
                                self.FLAVOR_VCPUS, self.FLAVOR_DISK,
                                self.OTHER_FLAVOR_ID, public=False)

        #The project admin can give access
        novautils.add_flavor_tenant_access(self.nova_project_admin_client,
                                          self.OTHER_FLAVOR_ID,
                                          self.PROJECT_ID)

        #The cloud admin can give access
        novautils.add_flavor_tenant_access(self.nova_cloud_client,
                                          self.OTHER_FLAVOR_ID,
                                          self.OTHER_PROJECT_ID)

        #The project member can't remove access
        self.assertAnyRaise(lambda:
          novautils.remove_flavor_tenant_access(self.nova_member_client,
                                            self.OTHER_FLAVOR_ID,
                                            self.PROJECT_ID))

        #The project admin can remove access
        novautils.remove_flavor_tenant_access(self.nova_project_admin_client,
                                          self.OTHER_FLAVOR_ID,
                                          self.PROJECT_ID)

        #The cloud admin can remove access
        novautils.remove_flavor_tenant_access(self.nova_cloud_client,
                                          self.OTHER_FLAVOR_ID,
                                          self.OTHER_PROJECT_ID)

        #The cloud gives access and the project admin deletes the flavor
        novautils.add_flavor_tenant_access(self.nova_cloud_client,
                                          self.OTHER_FLAVOR_ID,
                                          self.OTHER_PROJECT_ID)

        novautils.delete_flavor(self.nova_project_admin_client,
                self.OTHER_FLAVOR_ID)

    def test_list_private_flavor_info(self):

        novautils.create_flavor(self.nova_cloud_client,
                                self.LAST_FLAVOR_NAME, self.FLAVOR_RAM,
                                self.FLAVOR_VCPUS, self.FLAVOR_DISK,
                                self.LAST_FLAVOR_ID, public=False)

        #The cloud admin gives access
        novautils.add_flavor_tenant_access(self.nova_cloud_client,
                                          self.LAST_FLAVOR_ID,
                                          self.PROJECT_ID)

        novautils.list_flavor_tenant_access(self.nova_cloud_client,
                                         flavor=self.LAST_FLAVOR_ID)

        # A project admin can list
        novautils.list_flavor_tenant_access(self.nova_project_admin_client,
                                  flavor=self.LAST_FLAVOR_ID)

        # A member from the project cannot list
        self.assertAnyRaise(lambda:
          novautils.list_flavor_tenant_access(self.nova_member_client,
                                    flavor=self.LAST_FLAVOR_ID))

        novautils.delete_flavor(self.nova_cloud_client,
                self.LAST_FLAVOR_ID)


    #########################
    ### SERVERS
    #########################


    ###  LIST

    def test_cloud_admin_list_server(self):
        server_cloud_admin = novautils.create_server(self.nova_cloud_client,
                                self.CLOUD_ADMIN_SERVER,
                                self.IMAGE_ID,
                                self.FLAVOR_TINY_ID)

        server_project_admin = novautils.create_server(self.nova_project_admin_client,
                                self.PROJECT_ADMIN_SERVER,
                                self.IMAGE_ID,
                                self.FLAVOR_TINY_ID)

        servers = novautils.get_all_servers(self.nova_cloud_client)
        self.assertTrue(server_cloud_admin in servers)
        self.assertTrue(server_project_admin in servers)

        servers_member_same_project = novautils.get_all_servers(self.nova_member_client)
        self.assertTrue(server_cloud_admin in servers_member_same_project)
        self.assertTrue(server_project_admin in servers_member_same_project)

        servers_member_other_project = novautils.get_all_servers(self.other_nova_member_client)
        self.assertFalse(server_cloud_admin in servers_member_other_project)
        self.assertFalse(server_project_admin in servers_member_other_project)

        servers_same_project = novautils.get_all_servers(self.nova_project_admin_client)
        self.assertTrue(server_cloud_admin in servers_same_project)
        self.assertTrue(server_project_admin in servers_same_project)

        servers_another_project = novautils.get_all_servers(self.other_nova_project_admin_client)
        self.assertFalse(server_cloud_admin in servers_another_project)
        self.assertFalse(server_project_admin in servers_another_project)

        server_cloud_id = server_cloud_admin.id
        server_project_id = server_project_admin.id
        novautils.delete_server(self.nova_project_admin_client,
                                  server_project_id)
        novautils.delete_server(self.nova_cloud_client,
                                  server_cloud_id)



    ### GET

    def test_cloud_admin_get_server(self):
        server_cloud_admin = novautils.create_server(self.nova_cloud_client,
                                self.CLOUD_ADMIN_SERVER,
                                self.IMAGE_ID,
                                self.FLAVOR_TINY_ID)
        server_project_admin = novautils.create_server(self.nova_project_admin_client,
                                self.PROJECT_ADMIN_SERVER,
                                self.IMAGE_ID,
                                self.FLAVOR_TINY_ID)

        server_cloud_id = server_cloud_admin.id
        server_project_id = server_project_admin.id

        server_cloud = novautils.get_server(self.nova_cloud_client, server_cloud_id)
        self.assertTrue(server_cloud_admin , server_cloud)

        server_project = novautils.get_server(self.nova_project_admin_client, server_project_id)
        self.assertTrue(server_project_admin , server_project)

        self.assertAnyRaise(lambda:
            novautils.get_server(self.other_nova_project_admin_client, server_project_id))

        novautils.delete_server(self.nova_project_admin_client,
                                  server_project_id)
        novautils.delete_server(self.nova_cloud_client,
                                  server_cloud_id)


    ### CREATE
    def test_cloud_admin_create_server(self):
        server = novautils.create_server(self.nova_cloud_client,
                                self.CLOUD_ADMIN_SERVER,
                                self.IMAGE_ID,
                                self.FLAVOR_TINY_ID)
        server_id = server.id

        ## Member de outro projeto nao pode mata-la
        self.assertAnyRaise(lambda:
          novautils.delete_server(self.other_nova_member_client,
                                  server_id))
        self.assertAnyRaise(lambda:
          novautils.delete_server(self.other_project_admin,
                                  server_id))

        novautils.delete_server(self.nova_cloud_client,
                                  server_id)

    def test_project_admin_create_server(self):
        server = novautils.create_server(self.nova_project_admin_client,
                                self.PROJECT_ADMIN_SERVER,
                                self.IMAGE_ID,
                                self.FLAVOR_TINY_ID)

        server_id = server.id

        ## Member de outro projeto nao pode mata-la
        self.assertAnyRaise(lambda:
          novautils.delete_server(self.other_nova_member_client,
                                 server_id))
        self.assertAnyRaise(lambda:
          novautils.delete_server(self.other_project_admin,
                                  server_id))

        novautils.delete_server(self.nova_project_admin_client,
                                  server_id)

    def test_cloud_admin_delete_server(self):
        server = novautils.create_server(self.nova_project_admin_client,
                                self.PROJECT_ADMIN_SERVER,
                                self.IMAGE_ID,
                                self.FLAVOR_TINY_ID)

        server_id = server.id

        ## Member de outro projeto nao pode mata-la
        self.assertAnyRaise(lambda:
          novautils.delete_server(self.other_nova_member_client,
                                 server_id))
        self.assertAnyRaise(lambda:
          novautils.delete_server(self.other_project_admin,
                                  server_id))

        novautils.delete_server(self.nova_cloud_client,
                                  server_id)


    def test_project_admin_list_servers(self):
        novautils.get_all_servers(self.nova_project_admin_client)

    def test_cloud_admin_list_servers(self):
        novautils.get_all_servers(self.nova_cloud_client)

    def test_project_member_list_servers(self):
        novautils.get_all_servers(self.other_nova_member_client)

    #########################
    ### SERVER ACTIONS
    #########################

    '''def test_resize(self):

          print "COMECOOOOOOOOOOOOOOOOOOOOOOOU"

          wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)

          print '11111111111111111111111111'

                   #Everyone on the project can reboot
          novautils.resize(self.nova_member_client,
                                  self.SERVER_MEMBER,
                                  self.FLAVOR_SMALL_ID)


          print '2222222222222222222222'
          #novautils.pause(self.nova_member_client,
          #                       self.SERVER_MEMBER)


          print '3333333333333333333333333333333333'

          wait_for_verify_resize(self.nova_cloud_client, self.SERVER_MEMBER)


          print '4444444444444444444444444444'
          novautils.confirm_resize(self.nova_cloud_client, self.SERVER_MEMBER)

          print '55555555555555555555555555555'

          novautils.start(self.nova_cloud_client, self.SERVER_MEMBER)

          print '66666666666666666666666666666666666666666666'


          wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)

          ### O ERRO TA NESSA CHAMDA AI... DA UMA OLHADA NO LOG...


          #wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)

          print '7777777777777777777777777777777'

          novautils.pause(self.nova_member_client,
                                  self.SERVER_MEMBER)

          wait_for_paused(self.nova_cloud_client, self.SERVER_MEMBER)

          novautils.resize(self.nova_cloud_client,
                                    self.SERVER_MEMBER,
                                    self.FLAVOR_TINY_ID)

          novautils.confirm_resize(self.nova_cloud_client, self.SERVER_MEMBER)

          wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)

          # Member from another project can't
          self.assertAnyRaise(lambda:
            novautils.resize(self.other_member_client,
                                      self.SERVER_MEMBER,
                                      self.FLAVOR_SMALL_ID))

          print "ACABOOOOOOOOOOOOOOOOOOOOOOOOOOU"'''


def test_stop(self):
      wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)
      novautils.stop(self.nova_member_client,
                                  self.SERVER_MEMBER)
      wait_for_status(self.nova_cloud_client, self.SERVER_MEMBER, "SHUTOFF")
      self.assertTrue(self.SERVER_MEMBER.status == "SHUTOFF")


def test_pause(self):
      wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)
      novautils.pause(self.nova_member_client,
                                  self.SERVER_MEMBER)
      wait_for_status(self.nova_cloud_client, self.SERVER_MEMBER, "PAUSED")
      self.assertTrue(self.SERVER_MEMBER.status == "PAUSED")

def test_suspend(self):
      wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)
      novautils.suspend(self.nova_member_client,
                                  self.SERVER_MEMBER)
      wait_for_status(self.nova_cloud_client, self.SERVER_MEMBER, "SUSPENDED")
      self.assertTrue(self.SERVER_MEMBER.status == "SUSPENDED")



def wait_for_status(client, instance, status):
      # Wait for the instance to be active
      state = novautils.get_server_status(client, instance.id)
      while (state != status ):
        time.sleep(30)
        state = novautils.get_server_status(client, instance.id)
        if state == "ERROR":
          raise AssertionError('Instance Error')

def wait_for_active(client, instance):
      # Wait for the instance to be active
      state = novautils.get_server_status(client, instance.id)
      while (state != "ACTIVE" ):
        time.sleep(30)
        state = novautils.get_server_status(client, instance.id)
        if state == "ERROR":
          raise AssertionError('Instance Error')

def wait_for_verify_resize(client, instance):
      # Wait for the instance to shutten
      state = novautils.get_server_status(client, instance.id)
      while (state != "VERIFY_RESIZE" ):
        time.sleep(30)
        state = novautils.get_server_status(client, instance.id)
        if state == "ERROR":
          raise AssertionError('Instance Error')





def main():
     unittest.main()

if __name__ == '__main__':
     main()


'''def test_reboot(self):

      wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)

     #Everyone on the project can reboot
      novautils.reboot(self.nova_member_client,
                              self.SERVER_MEMBER)

      wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)


      novautils.reboot(self.nova_cloud_client,
                                self.SERVER_MEMBER)

      wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)

      # Member from another project can't
      self.assertAnyRaise(lambda:
        novautils.reboot(self.other_member_client,
                                  self.SERVER_MEMBER))'''

'''def test_rebuild(self):

      wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)

     #Everyone on the project can reboot
      novautils.rebuild(self.nova_member_client,
                              self.SERVER_MEMBER,
                              self.IMAGE_ID)

      wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)


      novautils.rebuild(self.nova_cloud_client,
                                self.SERVER_MEMBER,
                                self.IMAGE_ID)

      wait_for_active(self.nova_cloud_client, self.SERVER_MEMBER)

      # Member from another project can't
      self.assertAnyRaise(lambda:
        novautils.rebuild(self.other_member_client,
                                  self.SERVER_MEMBER,
                                  self.IMAGE_ID))'''
