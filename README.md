# Introduction

This is a simple project to learn how to create appointment scheduler by using Twilio

# local_settings.py

You have to create `local_settings.py` file in the project's root folder. The file has to contain the following variables:

- BASE_DIR
- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DATABASES
- TIME_ZONE
- TWILIO_SID
  - We get this from Twilio
- TWILIO_AUTH_TOKEN
  - We get this from Twilio
- TWILIO_SENDER_PHONE_NUMBER
  - We get this from Twilio. Using this to send sms
- TWILIO_VERIFIED_PHONE_NUMBER
  - We set this number in Twilio Console. We can't send sms to unverified numbers with demo account.


# Examples
### You can see the scheduled jobs on `http://127.0.0.1:8000/appointment/`
![](./resources/list-of-jobs.png)

### Here is an example of sent sms
![](./resources/sms.jpg)

You can change the sms text from `appointment/models.py/get_sms_content`