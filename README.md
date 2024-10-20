# Password-Manager
This is one of my first projects in cybersecurity that I developed to deepen my knowledge and gain practical experience. This password manager is a basic, console-based implementation in Python. I welcome your feedback and comments for improvement as well as tips to help me develop the project further.

## Table of Contents

1. [Implemented Features](#Implemented-Features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Database management](#database-management)
5. [Project structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)
8. [Credits](#credits)
9. [Disclaimer](#disclaimer)

## Implemented Features
- Database options: Create/open/delete a .key-database
- Entry options: Add/delete one/delete all/view entries (website, username, password)
- Generate a pseudogenerated password
- En- and decrypt all passwords with fernet

### Project status
- Still in progress

### Future implementations
- master passwords
- hashing
- salting

## Installation
### Installation Steps
Clone the repository and navigate into the directory
```bash
git clone https://github.com/sp8cky/Password-Manager && cd Password-Manager
```
Install dependencies
```bash
pip install -r requirements.txt
```

## Usage 
1. **Create a new database:** At startup, you can create a new password database and set a master password.
2. **Set a master password:** Once the database is created, you will be prompted to set a master password. This protects access to the database.
3. **Manage entries:**
  - After verifying the master password, you can add, view or delete entries.
  - Adding a new entry:** You can save website names, usernames and passwords.
  - **View entries:** All saved passwords can be listed.
  - Password Generator:** PWM offers an option to create randomly generated passwords.

## Database management
PWM stores your passwords in an SQLite database, which is encrypted with a `.key` file. Each database is protected with an individual key. The key is generated automatically when you create a new database.
- Delete database:** You can securely delete a database by selecting the "Delete Database" option in the main menu.
- Key files:** Make sure that the `.key` file is stored securely. Without this file you will not be able to access your database.

## Project structure
- `password_manager.py`: Main script that executes the password manager.
- `input_handler.py`: Contains functions for user input and menu control.
- `db_handler.py`: Manages database operations (creating, opening, deleting entries).
- `encryption_handler.py`: Encryption logic (encryption/decryption of passwords and master password management).

## Contributing
Feedback and Contributions: It's my first cybersecurity project, Feedback and contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.

### How to Contribute
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

## Credits:
This project was created by sp8cky.

## License:
This project is licensed under the MIT-License. See the LICENSE file for details.

## Disclaimer
This project is for educational purposes only and is provided as is. Use it at your own risk. I take no responsibility for any damages or problems that may arise from the use of the password manager.
