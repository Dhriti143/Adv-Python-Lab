# LAB 2 - Railway Ticket Reservation System

## Overview

This Python program implements a railway ticket reservation system for a busy rail network. The system includes functionalities for loading train and passenger data from CSV files, checking seat availability, updating seat availability after confirming bookings, and generating reports for the railway administration.

## Files

1. **trains.csv:**
   - Contains data about trains, each row representing a train with unique alphanumeric code, train name, source station, destination station, and total seats.

2. **passengers.csv:**
   - Contains data about passengers, including passenger name, train ID, and the number of tickets they want to book.

3. **railway_reservation_system.py:**
   - The main Python program that implements the railway ticket reservation system.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/.git
   cd RailwayReservationSystem
   cd Lab2
  
2. **Run the Program:**

```bash
python railway_reservation_system.py
```
3. **Follow On-screen Prompts:**

The program will guide you through loading train and passenger data, checking seat availability, and generating reports.
Fare Rules
Fare rules can be adjusted based on your preference, and they are defined in the program for calculating the total fare for each booking.

## Sample CSV Files
trains.csv:
```bash
TrainID,TrainName,SourceStation,DestinationStation,TotalSeats
T123,ExpressOne,StationA,StationB,100
T456,SwiftExpress,StationC,StationD,150
T789,SuperFast,StationE,StationF,120
```
passengers.csv:
```bash
PassengerName,TrainID,NumTickets
Alice,T123,2
Bob,T456,1
Charlie,T789,3
```
## Error Handling
The program gracefully handles various types of errors, including invalid train IDs, passenger names, insufficient seats, etc. It provides informative error messages to guide users.

## Notes
 - The passenger data is assumed not to exceed the available seats on any train.
 - Modify fare rules according to your preference.
 - Ensure Python 3.x is installed.
For detailed comments explaining each step of the implementation, refer to the code within railway_reservation_system.py.
