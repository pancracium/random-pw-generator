# RANDOM PASSWORD GENERATOR

Another program made by me (a 13yo), which this time generates random passwords (as indicated by the name).

## HOW TO USE

### LENGTH

Insert here the length you want for your random password. Insert a positive integer between 1 and 40 (both inclusive).

### UNDESIRED CHARACTERS

Insert here character you DON'T want your password to have. Remeber this field is case-sensitive.

### STRENGTH

Choose between three choices:

- Weak: Letters only.

- Medium: Letters and numbers.

- Strong: Letters, numbers and symbols (recommended).

### GENERATE BUTTON

Click this to generate your random password.

### COPY BUTTON

Click this to copy the password to your clipboard.

### SAVE BUTTON

Click this to save your random password to a file.

## How to convert to an executable:

- Download the code as a zip file and unzip it to a folder

- Open that folder with the terminal

- Run this command:
` pip install pyinstaller `

- And lastly, run this one:
` pyinstaller --onedir --noconsole --noconfirm --name "Random PW Generator" --icon "icon.ico" --add-data "icon.ico;." --add-data "tooltip.py;." --add-data "README.md;." main.py `

- Open the dist folder and run the app.
