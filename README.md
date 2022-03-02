# Email

This is a service that allows you to send emails at pace! I have written this code to enable people to send multiple emails at once, with the aim of making emails an ease to send.

## Install it locally

Download the code via [GIT](https://git-scm.com/downloads)

```bash
git clone https://github.com/dhavalpandey/email.git
```

You also need to install [Python](https://www.python.org/downloads/)

```bash
# Check if it is successfully installed
python --version
```

## Usage

1. First, create a .env file in your working directory

```bash
cd . > .env
```

2. Then, add your credentials to the .env file

```.env
OUTLOOK_EMAIL="email@outlook.com"
OUTLOOK_PASSWORD="password123"
GMAIL_EMAIL="email@gmail.com"
GMAIL_PASSWORD="password123"
```

3. Edit the "email.html" file and write the content you want to send on the email inside it.

4. Time to run your code! The program will prompt you with all the information needed.

```bash
py send_mail.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
