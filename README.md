# Instagram Follow-Back Automation Script

This Python script automates the task of following back users on Instagram who follow you. It uses the `instagrapi` library to interact with Instagram's API and follows users who are not already in your following list.

---

## **Features**

- **Authentication:** Logs into your Instagram account securely using environment variables.
- **Follower Extraction:** Fetches the list of users who follow you.
- **Following Extraction:** Fetches the list of users you are currently following.
- **Follow-Back Logic:** Follows users who follow you but are not in your following list.
- **Error Handling:** Handles common Instagram API exceptions (e.g., rate limits, login challenges).

---

## **Prerequisites**

Before using this script, ensure you have the following:

1. **Python 3.8 or higher** installed on your system.
2. An **Instagram account** (preferably a dummy account for testing).
3. **Environment variables** set up for your Instagram credentials.

---

## **Installation**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/p-w0rld/ig-followback-automation.git
   cd ig-followback-automation
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   If you don’t have a `requirements.txt` file, install the required packages manually:

   ```bash
   pip install instagrapi python-dotenv pillow
   ```

4. **Set Up Environment Variables:**
   Rename `.env.template` to `.env` in the root directory and add your Instagram credentials:
   ```plaintext
   IG_USERNAME=your_instagram_username
   IG_PASSWORD=your_instagram_password
   ```

---

## **Usage**

1. **Run the Script:**

   ```bash
   python follow_user.py
   ```

2. **What Happens:**
   - The script logs into your Instagram account.
   - It fetches your followers and the users you are following.
   - It follows users who follow you but are not in your following list.

---

## **Configuration**

### **Environment Variables**

- `IG_USERNAME`: Your Instagram username.
- `IG_PASSWORD`: Your Instagram password.

### **Script Customization**

- **Login Retries:** The `login` function retries authentication up to 3 times by default. You can modify this in the `login` function.
- **Challenge Handling:** The script currently prints a placeholder message for login challenges (e.g., 2FA). You can implement challenge resolution logic as needed.

---

## **Code Overview**

### **Main Functions**

1. **`main()`:**

   - Authenticates with the Instagram API.
   - Fetches followers and following lists.
   - Follows users who are not already in your following list.

2. **`login(cl: Client, username, password, attempts=1, max_retries=3)`:**

   - Handles authentication with retries and error handling.

3. **`get_followers(cl: Client) -> dict`:**

   - Fetches the list of users who follow you.

4. **`get_following(cl: Client) -> dict`:**

   - Fetches the list of users you are following.

5. **`follow_user(cl: Client, user: int) -> bool`:**
   - Follows a specific user.

---

## **Error Handling**

The script handles common Instagram API exceptions, including:

- `ChallengeRequired`: Occurs when Instagram requires additional verification (e.g., 2FA).
- `BadPassword`: Incorrect login credentials.
- `FeedbackRequired`: Occurs when Instagram detects suspicious activity.
- `PleaseWaitFewMinutes`: Rate limiting by Instagram.

---

## **Limitations**

- **Rate Limits:** Instagram imposes strict rate limits. Avoid running the script too frequently to prevent account restrictions.
- **Login Challenges:** The script does not currently handle login challenges (e.g., 2FA). You will need to implement this functionality.
- **Ethical Use:** Avoid spamming users or violating Instagram’s terms of service.

---

## **Contributing**

Contributions are welcome! If you’d like to improve this script, please:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Disclaimer**

This script is for educational purposes only. Use it at your own risk. The developers are not responsible for any account restrictions or bans imposed by Instagram.

---

## **Support**

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/p-w0rld/ig-followback-automation).

---
