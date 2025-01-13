# Logger module to track actions
def log_action(action):
    with open('action_log.txt', 'a') as log_file:
        log_file.write(action + '\n')
