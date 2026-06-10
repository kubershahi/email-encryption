map_server = 'my.imap.server'
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(imap_user, imap_password)

start_message_uid = 169
if start_message_uid:
    command = "UID {}:*".format(start_message_uid)
    result, data = mail.uid('search', None, "UID", start_message_uid + ':*')
else:
    result, data = mail.uid('search', None, "ALL") # this returns list of all messages
