import csv

train_data = []
passenger_data = []
revenue = {}
total_cost = 0

# Function to check availability and book seats
def check_availability(name, trainId, seats):
    global total_cost
    for i in range(len(train_data)):
        if train_data[i][0] == trainId:
            if int(train_data[i][4]) > seats:
                fare = seats * int(train_data[i][5])
                print(f"Booking Confirmed for {name}.\nTotal fare: Rs.{fare}/-\n")
                train_data[i][4] = int(train_data[i][4]) - seats
                total_cost += fare
                if trainId in revenue:
                    revenue[trainId] += fare
                else:
                    revenue[trainId] = fare
                return True
            else:
                print("Not enough seats available.")
                return False
    print("Invalid Train ID")
    return False

# Reading train data from 'trains.csv'  
with open('trains.csv', 'r') as trains:
    next(trains)
    read = csv.reader(trains)
    list1 = list(read)
    train_data = list1

# Reading passenger data and booking seats as per availability
with open('passengers.csv', 'r') as p:
    next(p)
    read = csv.reader(p)
    for row in read:
        name = row[0]
        trainId = row[1]
        seats = int(row[2])
        check_availability(name, trainId, seats)

# Writing updated train data to 'report1.csv'
with open('report1.csv', 'w') as r:
    fields = ['Train ID', 'Train Name', 'Source Station', 'Destination Station', 'Total Seats', 'fareperseat']
    write = csv.writer(r)
    write.writerow(fields)
    write.writerows(train_data)

# Writing revenue data to 'report2.csv'
with open('report2.csv', 'w') as r:
    fields = ['Train ID', 'Revenue']
    writer = csv.DictWriter(r, fieldnames=fields)
    writer.writeheader()
    # Revenue data as rows
    for train_id, revenue_amount in revenue.items():
        writer.writerow({'Train ID': train_id, 'Revenue': revenue_amount})
    # Total revenue generated as a separate row
    writer.writerow({'Train ID': 'Total revenue generated', 'Revenue': total_cost})