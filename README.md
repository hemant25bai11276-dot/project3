# Random Passward Genarator:

A simple and secure random password generator that can helps users create strong and unpredictable passwords
using uppercase letters(ABCD...), lowercase letters(abcd...), digits(0123...), special characters(!@#$...).
Its purpose is to generate secure, randomized passward. The user can input the desired length of the password and specify whether or not character repetition is allowed. The application then generates the password from a predefined set of characters (letters, numbers, and symbols) and displays it in a read-only field.

## Features:

user can select the desired passward length.

user can select that reapeatation is allow or not.

Customizable Length: Users can specify the exact number of characters for their password.

Repetition Control: Users can choose between two modes:

No Repetition (Input 1): Each character in the password will be unique.

Allow Repetition (Input 2): Characters can be repeated in the password.

Character Set: The password is generated from a comprehensive string including uppercase letters, lowercase letters, digits (0-9), and common symbols (!@#$%^&*()/?,.).

Simple GUI: A user-friendly graphical interface built with Tkinter for easy interaction.

### Technologies used:
 python.
 standard libraries: 'random' , 'string' and 'secrets'for stronger randomness.
GUI Library: Tkinter (Standard Python library for creating desktop applications)

### Steps to Install & Run the Project

You only need to have Python 3 installed on your system. Tkinter is typically included with standard Python distributions.

Installation and Running
Save the Code: Save the provided Python code into a file named, for example, password_generator.py.

Open Terminal/Command Prompt: Navigate to the directory where you saved the file.

Run the Script: Execute the script using the Python interpreter:

The graphical user interface (GUI) window titled "Random Passward Generator" will appear.

### working about repeatation or not:

Test Case 1: Simple Password Generation

Input: Length: 10, Repetition: 2

Action: Click the "Generate Passward" button.

Expected Result: A 10-character password will be displayed. Characters may repeat.

Test Case 2: No Repetition (Unique Characters)

Input: Length: 8, Repetition: 1

Action: Click the "Generate Passward" button.

Expected Result: An 8-character password will be displayed. All characters should be unique.

 ### Text:

 Enter the desired passward length.
 Select the repeatation in passward or not.
 The programm will display a random passward based on your choice.


### Basic Generation:

For example generate a random passward(e.g.,10 characters).
The programm will dispaly a strong random passward.
Example output: hs3$Rz5@W?

## Instructions for testing

Follow these steps to test the different functionalities of the application:

Test Case 1: Generating a Password with Character Repetition
In the GUI, enter a number for the desired length (e.g., 12).

In the "Repetition?" field, enter 2 (for otherwise/allow repetition).

Click the "Generate Passward" button.

Expected Result: A password of length 12 should be displayed, and characters may repeat.

Test Case 2: Generating a Password without Character Repetition
In the GUI, enter a number for the desired length (e.g., 8).

In the "Repetition?" field, enter 1 (for no repetition).

Click the "Generate Passward" button.

Expected Result: A password of length 8 should be displayed, and all characters in the password should be unique.

Test Case 3: Error Handling (Missing Inputs)
Leave both the length and Repetition? fields empty.

Click the "Generate Passward" button.

Expected Result: A pop-up Error message box should appear with the text: "please enter the key in the required inputs".

Test Case 4: Testing Maximum Length (Without Repetition)
The character set (character_string) has 78 unique characters.

Enter a length of 79.

Enter 1 for no repetition.

Click "Generate Passward".
 
 # Here is a screenshot of the output of an programm
<img width="552" height="400" alt="Screenshot 2025-11-22 183119" src="https://github.com/user-attachments/assets/f4869360-9ac0-47e3-a325-ea65c416bcb0" />

 
 


