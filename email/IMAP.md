# IMAP field names

[special thanks to atmail.com for the reference](https://www.atmail.com/blog/imap-commands/_)
 
## relevant fields (as of 3 JAN 2025)

`using the syntax BODY.PEEK[HEADER.FIELDS (<field>)] where <field> in:`

### Return-path
documentation placeholder (for now)

### Original-recipient
I'm going to use this to make sure the email was in fact addressed to me.  I've observed messages where I am not the intended recipient

### DomainKey-Signature
documentation placeholder (for now)

### Date
date message was sent

### From
original sender of the message

### Reply-to
placeholder for now - I want to explore what options exist here

### To 
At this point, I feel if there is a discrepancy between the "To" and the "Original Recipient" values, it might be a mailing list

### Message-id
probably don't need this - UID for message on server

### Subject
capturing text to train model on bad subjects

### MIME-version
may be necessary for further exploration

### Content-type
may be necessary for further exploration

## eXtended header fields
The following fields have been identified in messages from one specific server  Hanging on to see if there is utility here

**x-mid**
**x-job**
**x-rpcampaign**
**x-orgId**

**X-CSA-Complaints** 
**X-Proofpoint-Virus-Version**
**X-Proofpoint-Spam-Details**
**DKIM-Signature**
observed Content-Type:List-Unsubscribe - need to investigate

**Received**
looks ornery - contains the entire message envelope information, including receipt path.
