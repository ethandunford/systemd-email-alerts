
def run(argv):
    try:
        print('Setting up email alerts')
        if re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', argv[1]) is not None:
            print('Email address is valid -> {0}'.format(argv[1]))
            command = 'sed -i \'s/youremail@youremail.com/{0}/g\' unit-status-mail.sh'.format(argv[1])
            os.system(command)
            os.system('sudo cp unit-status-mail.sh /bin/unit-status-mail.sh')
            os.system('sudo chmod +x /bin/unit-status-mail.sh')
            os.system('sudo cp unit-status-mail@.service /etc/systemd/system/unit-status-mail@.service')
            print('Installing Send Mail')
            os.system('sudo apt-get install sendmail')
            print('Sending test check junk folder')
            os.system('/bin/unit-status-mail.sh test email')
        else:
            print('Email address is not valid')
    except Exception:
        print('Provide a email')


if __name__ == '__main__':
    from sys import argv
    import os
    import re
    args = run(argv)
