#Sydney Jaques
#Lab 1 Part 1 search students.txt file by user desired field
#CSC - 365

def simpleQuery(index, comm, f):
    if len(comm) < 2:
        return
    for line in f.readlines():
        cols = [x.strip() for x in line.split(",")]
        if cols[index] == comm[1]:
            print(cols[0] + "," + cols[1], end= '')
            if comm[0] == "B":
                print("," + cols[2] + "," + cols[3])
            elif comm[0] == "G":
                print("," + cols[5] + "," + cols[6] + "," + cols[7] + "," + cols[4])
            elif comm[0] == "S":
                print("," + cols[2] + "," + cols[3] + "," + cols[6] + "," + cols[7])
            else:
                #T
                print()

def studentBus(comm, f):
    for line in f.readlines():
        cols = [x.strip() for x in line.split(",")]
        if cols[0] == comm[1] and cols[4] == comm[2]:
            print(cols[0] + "," + cols[1] + "," + cols[4])


def endOfSpectrumGPA(comm, f):
    if comm[2] == 'H':
        expression = '>'
        curr = '0.0'
    elif comm[2] == 'L':
        expression = '<'
        curr = '10.0'
    
    for line in f.readlines():
        cols = [x.strip() for x in line.split(",")]
        if cols[2] == comm[1]:
            print(cols[5] + expression + curr)
            if eval(cols[5] + expression + curr):
                curr = cols[5]
    print("Final Result: " + curr)

        
def getAvgByGrade(comm, f):
    addTotal = 0
    count = 0
    for line in f.readlines():
        cols = [x.strip() for x in line.split(",")]
        if cols[2] == comm[1]:
            addTotal += float(cols[5])
            count += 1
    print("Grade: " + str(comm[1]) + " Avg: " + str(addTotal/count))
    

            



#Returned indexes will be printed in main, as they are the results of desired
# search
def main():
    inputCommand = ""
    try:
        f = open("students.txt", "r")
    except:
        print("Error: No file students.txt found in directory")
        exit(1)
    while inputCommand != "Q":
        inputCommand = input("Enter Search Criteria: ")
        command = inputCommand.split(" ")

        if command[0] == "S":
            #Search Student LName
            if len(command) == 2:
                simpleQuery(0, command, f)
            #Search Student LName and Bus
            elif len(command) == 3:
                studentBus(command, f)
        elif command[0] == "T": #only query possibility
            #Search Student LName
            if len(command) == 2:
                simpleQuery(6, command, f)
        elif command[0] == "B": #only query possibility
            #Search Bus Num
            if len(command) == 2:
                simpleQuery(4, command, f)
        elif command[0] == "G":
            #Search by Grade only
            if len(command) == 2:
                simpleQuery(2, command, f)
            #Search by High/Low
            elif len(command) == 3:
                endOfSpectrumGPA(command, f)
        elif command[0] == "A":
            #Search Grade
            #Print average of all GPA's matching
            if len(command) == 2:
                getAvgByGrade(command, f)
        elif command[0] == "I":
        #Print total number of students in each grade(0-6)
            index = 2
        elif command[0] == "Q":
        #Quit
            return
        f.seek(0)

        
            

    f.close()

if __name__ == "__main__":
    main()
