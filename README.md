Python program is designed to process and display information about training rooms, their capacities, and enrollments. Below is a breakdown of the code, its functionality, and suggestions for improvement.

Code Breakdown
Main Function:

The main() function starts by prompting the user to input the training name.
It then prints a header for the table that will display room details.
The program calls the process_training_data() function to gather data about the training rooms.
Finally, it prints a summary of the training information.
Data Input:

The get_classroom_info() function collects information about a room, including the room number, maximum capacity, and current enrollment. It returns these values, and if the room number is negative, it indicates the end of input.
Processing Room Data:

The process_training_data() function continuously calls get_classroom_info() to gather data until a negative room number is provided.
It calculates empty seats, checks room availability, and maintains counts of total capacity, enrollment, available rooms, and over-enrolled rooms.
The function returns all the collected information.
Final Summary:

The final_summary() function prints out the training name and summary statistics, including the number of training rooms, total capacity, total enrollment, available rooms, and over-enrolled rooms.
