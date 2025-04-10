
# SeleniumFollowerBot

A Python-based Instagram follower bot that uses Selenium to automatically follow users on Instagram using multiple accounts. The bot bypasses Instagram's security verification by using Atomic Mail for verification code handling and also bypasses cookie checks.

## Features
- **Multi-Account Support:** Automatically logs in with multiple accounts and follows a target user.
- **Atomic Mail Integration:** Uses Atomic Mail accounts to bypass Instagram's security verification.
- **Cookie Handling:** Automatically bypasses Instagram's cookie verification.
- **Selenium and Python:** Written in Python using the Selenium library, with additional support from `chromedriver_autoinstaller`, `random`, `time`, and `pyperclip`.

## Installation

### Prerequisites
- Python 3.x
- Selenium
- `chromedriver_autoinstaller`
- `random`, `time`, `pyperclip`

### Installing Dependencies
1. Clone the repository or download the script.
2. Install the required Python libraries by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure Accounts:**
   Before running the bot, make sure to edit the `username_list` in the script with the usernames of the Instagram accounts you want to use. Add new accounts with:
   ```python
   username_list.append("your_username")
   ```

2. **Run the Script:**
   After configuring the accounts, you can run the bot by executing:
   ```bash
   python SeleniumFollowerBot.py
   ```

3. **Login Information:**
   The bot requires login information, which should be placed directly in the script:
   ```python
   insta(username_list[0], "your_instagram_password", "target_username", "your_atomic_mail", "your_atomic_mail_password")
   ```

4. **Automatic Updates:**
   The script uses `chromedriver_autoinstaller`, so it automatically ensures you have the latest version of ChromeDriver.

## Notes
- The bot is designed to bypass Instagram’s verification prompts by using Atomic Mail for accessing verification codes.
- You must use **Atomic Mail accounts** for the verification process.
- The bot also automatically handles cookie-related verification checks from Instagram.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
