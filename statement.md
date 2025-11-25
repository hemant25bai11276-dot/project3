## problem statement:

The need for strong and unique passwords is critical for digital security, as weak or reused
passwords make accounts vulnerable to hacking. Users often struggle to manually create
complex, random passwords that meet security requirements. The problem is to provide a
simple, intuitive, and efficient tool that automatically generates secure, customizable, and
random passwords.

## scope of the project:

Generates random passwords consisting of letters (uppercase and lowercase), numbers, and symbols.

Allows the user to specify the desired length of the password.

Allows the user to choose whether character repetition is allowed in the generated password.

Displays the generated password in a read-only output box on the GUI.

Includes basic error handling for invalid input (e.g., non-numeric entries for length and repetition choice).

Provides a user-friendly graphical interface for interaction.

# In-Scope:

Implementing a graphical user interface (GUI) for easy interaction.

Allowing the user to specify the desired length of the password.

Providing an option for the user to choose between generating a password with or without repeating characters.

Utilizing a comprehensive character set (uppercase letters, lowercase letters, digits, and special symbols) for maximum randomness.

Displaying the generated password in a read-only field.

Handling basic input errors (e.g., non-integer input for length or repetition choice).

# Out-of-Scope:

Integrating with a password manager or external services.

Implementing a feature to check the strength of generated passwords.

Saving or storing the generated passwords.

Implementing complex character set customization (e.g., specifying only numbers or only letters).

## target usres:

The primary target users for this application are:

General Internet Users: Individuals who need strong passwords for their various online accounts (email, social media, banking, etc.).

Security-Conscious Users: Users who prioritize digital security and require highly random, complex passwords.

Developers/System Administrators: Professionals who occasionally need to generate secure, temporary, or machine-generated passwords for testing or system setup.

## high level features:

.Length Specification: Users can input an integer value to define the exact number of characters the password should contain.
.Character Repetition Control: sers can choose between allowing character repetition (2) or enforcing no character repetition (1) in the output password.
.Password Generation Logic: Uses Python's random module to create a password from a comprehensive set of characters (alphanumeric and symbols).
.GUI Interface (tkinter): Provides a simple window with input fields for parameters and a dedicated button to trigger the generation process.
.Read-Only Output Display: The generated password is shown in a non-editable text field for easy viewing and copying.

GUI Interface:  "A simple, intuitive graphical interface built with Tkinter."
Configurable Length:  Users can specify the exact number of characters for the password.
Character Repetition Control:  Users can choose if characters in the password can be repeated or must be unique.
Comprehensive Character Set:  "Passwords are drawn from a pool of letters (upper/lower), numbers, and symbols."
Password Display:  The generated password is shown in a read-only entry box for easy viewing and copying.
Error Handling:  "Displays an alert message for invalid inputs (e.g., non-numeric entries)."












