INSTALLED_APPS += ["taiga_contrib_ldap_auth_ext"]

LDAP_SERVER = "ldap://mail.we3d.vn"
LDAP_PORT = 389

LDAP_BIND_DN = "uid=zimbra,cn=admins,cn=zimbra"
LDAP_BIND_PASSWORD = "vboIynkDf"

LDAP_SEARCH_BASE = 'ou=people,dc=domain,dc=com'

LDAP_USERNAME_ATTRIBUTE = "uid"
LDAP_EMAIL_ATTRIBUTE = "mail"
LDAP_FULL_NAME_ATTRIBUTE = "givenName"

LDAP_SAVE_LOGIN_PASSWORD = True

LDAP_MAP_USERNAME_TO_UID = None