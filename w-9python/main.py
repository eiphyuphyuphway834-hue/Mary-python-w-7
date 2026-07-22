from ticket import create_ticket
from display import display_ticket


def main():

    # Receive data from ticket.py
    student_name, student_id, issue, location, priority = create_ticket()

    # Assign technician based on priority
    if priority.lower() == "high":
        technician = "Ahmad"
    elif priority.lower() == "medium":
        technician = "Siti"
    else:
        technician = "Ali"

    # Display ticket
    display_ticket(
        student_name,
        student_id,
        issue,
        location,
        priority,
        technician
    )


if __name__ == "__main__":
    main()