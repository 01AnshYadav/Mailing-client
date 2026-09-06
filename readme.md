# Mailing Client

A simple Python script that sends an email with a text message and an image attachment using Gmail's SMTP server.

## Features

- Connects to Gmail via SMTP (TLS on port 587)
- Sends a plain text email body loaded from a file
- Attaches an image file to the email

## Requirements

- Python 3.x
- A Gmail account with an **App Password** (regular Gmail passwords won't work — see Setup below)

No external packages are needed; this uses only Python's standard library (`smtplib`, `email`).

## Project structure

```
mailing client/
├── mailing client.py   # main script
├── password.txt        # Gmail App Password (never commit this — see .gitignore)
├── email msg.txt        # body text of the email
├── email pic.png        # image attached to the email
└── .gitignore
```

## Setup

### 1. Generate a Gmail App Password

Gmail no longer accepts your normal account password for SMTP logins. You need an App Password instead:

1. Turn on **2-Step Verification**: https://myaccount.google.com/security
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Copy the 16-character password Google gives you

### 2. Add the password to `password.txt`

Create a file named `password.txt` in the project folder and paste the App Password into it (nothing else in the file).

> ⚠️ **Never commit `password.txt` to version control.** It's already listed in `.gitignore`, but double-check before pushing.

### 3. Set the message content

- Edit `email msg.txt` with whatever text you want as the email body.
- Replace `email pic.png` with whatever image you want attached (or update the filename in the script).

### 4. Update sender/recipient

Open `mailing client.py` and edit:

```python
server.login('your-email@gmail.com', password)
...
msg['To'] = 'recipient@example.com'
...
server.sendmail('your-email@gmail.com', 'recipient@example.com', text)
```

## Usage

```bash
python "mailing client.py"
```

If successful, the script will send the email silently (no output on success). If login fails, double-check that:
- You're using an **App Password**, not your regular Gmail password
- 2-Step Verification is enabled on the account
- `password.txt` contains only the password, with no extra spaces or newlines

## Security notes

- `password.txt` is excluded from git via `.gitignore` — do not remove that entry.
- Consider switching to an environment variable (`os.environ.get(...)`) instead of a plaintext file for better security once you're comfortable with that setup.
