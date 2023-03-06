import argparse

from integrations import monitor, desktop, office

parser = argparse.ArgumentParser()
parser.add_argument('action', help='action to execute on the bulbs (on, off)')
args = parser.parse_args()

action = args.action

if action == 'on':
    monitor.turn_on()
    desktop.turn_on()
    office.on()
elif action == 'off':
    monitor.turn_off()
    desktop.turn_off()
    office.off()
else:
    print('Invalid action')
