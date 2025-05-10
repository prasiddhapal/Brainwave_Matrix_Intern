# Brainwave_Matrix_Intern
# 💪 **Password Strength Checker** 💪


This is a  password strength checker application developed as part of my internship at **Brainwave Matrix Solutions**. It provides users with real-time feedback on the strength of their passwords, helping them choose more secure options.

## ✨ **Features** ✨

* **⚡ Real-time Feedback:** As the user types their password, the application instantly assesses its strength.
* **📊 Visual Indicator:** A color-coded progress bar visually represents the password strength:
    * **🟢 Strong password** (as seen in the output below)
    * ![Screenshot 2025-05-10 214923](https://github.com/user-attachments/assets/b4eabbd9-a985-41c3-9b6c-12687daac712)

        ![Strong Password Output])
        ```text
        Password Strength: Strong
        Password looks great!
        ```
    * **🟡 Moderate password** (as seen in the output below)
       ![Screenshot 2025-05-10 215116](https://github.com/user-attachments/assets/f0173c9f-4222-4331-9101-ca7e0eca05e5)

        ```text
        Password Strength: Moderate
        Suggestions:
        Add numbers.
        Add special characters (!@#$% etc).
        ```
    * **🔴 Weak password** (as seen in the output below)
        ![Weak Password Output]
      ![Screenshot 2025-05-10 215044](https://github.com/user-attachments/assets/2227da65-4f14-414c-9241-522c7c606f7b)

        ```text
        Password Strength: Weak
        Suggestions:
        Avoid common passwords like 'password'.
        ```
* **🔒 Common Password Check:** The application includes a check against a list of common passwords,** including those found in lists from previous data breaches**. This significantly enhances security assessment by identifying passwords that are highly vulnerable to hacking.
* **💡 Suggestions:** When a weak or moderate password is detected, the application provides helpful suggestions to improve its strength.

## ⚙️ **Installation** ⚙️

1.  Make sure you have Python installed on your system.
2.  Clone this repository.
3.  Ensure the `common_passwords.txt` file is in the same directory as the script.
4.  Navigate to the project directory in your terminal.
5.  Run the script using: `python pswd.py` *(assuming your script is named `pswd.py`)*

## 🚀 **Usage** 🚀

1.  Run the application.
2.  Enter your password in the provided text field.
3.  The application will automatically assess the strength and display the result along with any suggestions.

## 🤝 **Contributing** 🤝

Contributions are welcome! Please feel free to submit pull requests with improvements or bug fixes.

## 👨‍💻 **Developed By** 👨‍💻

**Prasiddha Pal** - Intern at[Brainwave Matrix Solutions

## 🙏 **Acknowledgements** 🙏

* *(Mention any libraries you used, e.g., Tkinter for the GUI)*
* *(Acknowledge the source of your common password list, if applicable, or mention that it's a compilation of common passwords)*

---

Thank you for checking out my project! 😊
