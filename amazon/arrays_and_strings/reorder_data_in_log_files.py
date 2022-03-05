class Solution(object):

    def reorderLogFiles(self, logs):
        letter_logs = []
        digit_logs = []

        for log in logs:
            content = log.split(' ', 1)[1]
            if content[0].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        return sorted(letter_logs, key=lambda x:(x.split(' ', 1)[1], x.split(' ', 1)[0])) + digit_logs