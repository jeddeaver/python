import csv
import yaml
import imaplib


class imapAuth:
    
    def __init__(self, message):
        settings = yaml.safe_load(open("creds.yaml"))
        hostname = settings["hostname"]
        username = settings["username"]
        aspwd = settings["app-specific-password"]
        port = 993
        server = imaplib.IMAP4_SSL(hostname)
        try:
            server.login(username, aspwd)
            server.select("INBOX")
            result, messages = server.search(None, "ALL")
            if result == "OK":
                # we have at least 1 message, so we can fetch the first one
                out = open("test.csv", "w", newline="")
                writer = csv.writer(out)
                for ce in messages[0].split():                    
                    result, data = server.fetch(ce, "(BODY.PEEK[HEADER.FIELDS (Original-Recipient)] BODY.PEEK[HEADER.FIELDS (Date)] BODY.PEEK[HEADER.FIELDS (To)] BODY.PEEK[HEADER.FIELDS (From)] BODY.PEEK[HEADER.FIELDS (Subject)] BODY.PEEK[TEXT] FLAGS)")
                    if result == "OK":
                        messageData = []
                        # I am sure there is a better way to do this.  I'd love your feedback.
                        # Original-Recipient
                        originalRecipient = data[0][1].split(b"\r\n")[0].split(b";")[1]
                        # Date
                        # To
                        # From
                        # Subject
                        # TEXT
                        date = data[1][1].split(b":")[1]
                        to = data[2][1].split(b"\r\n")[0].split(b":")[1]
                        sender = data[3][1].split(b"\r\n")[0].split(b":")[1]
                        # add check for empty subject
                        subject = data[4][1].split(b"\r\n")[0]
                        # add check for empty body
                        body = data[5][1]
                        row = [originalRecipient, date, to, sender, subject, body]
                        messageData.append(row)
                        writer.writerow(messageData)
                out.close()
        except Exception as e:
            print(e)
        finally:
            server.close()
            server.logout()


        



class imapAuth:
    token = "<>"

    def __init__(self, email, password, provider=None):
        print(self.token)

    