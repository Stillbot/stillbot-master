#!/usr/bin/env python
import os
import sys
import signal


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stillbot_master.settings")

    from django.core.management import execute_from_command_line

    """
    This code may be useful somewhere in the stillbot-master standalone daemon

    LOCK_FILE = '/tmp/stillbot-master.lock'
    from stillbot_master import arduino
    import threading
    def shutdown(signal, frame):
        try:
            my_pid = str(os.getpid())
            with open(LOCK_FILE, 'r') as lf:
                lf_pid = lf.readline().strip()
                if lf_pid == my_pid:
                    os.unlink(LOCK_FILE)
                else:
                    django.dispatch.Signal().send('system')
                    sys.exit(0)
        except:
            pass
        else:
            print('Closing connection to stillbot-slave..')
            sys.exit(0)
    signal.signal(signal.SIGINT, shutdown)

    if not os.path.exists(LOCK_FILE):
        with open(LOCK_FILE, 'w') as f:
            f.write(str(os.getpid()))
        print('Starting up stillbot-master..')
        bot = threading.Thread(target=arduino.run)
        bot.setDaemon(True)
        bot.start()
    else:
        print('(stillbot-master already running)')
    """

    execute_from_command_line(sys.argv)
