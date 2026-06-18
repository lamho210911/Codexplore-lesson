from codexlore import emailProcess, printMsg
def main():
    emails = [
        'qyd@gmail.com',
        'youtube@codexplore.dev',
        'liverpool@winner.com'
    ]

    for email in emails:
        username, email_domain = emailProcess(email)
        printMsg(username, email_domain)


if __name__ == "__main__":
    main()