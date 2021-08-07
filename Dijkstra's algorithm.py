routes = {
"AB" : "2",
"AC" : "6",
"BC" : "2",
"BD" : "3",
"BE" : "2",
"CD" : "1",
"DE" : "2",
"DF" : "5",
"EF" : "3",
}
start = "A"
finish = "F"

def secondRow(table):
    row2 = {}
    row2[start + "_"] = "_"

    for i in table[0][1:]:
        try:
            row2[i] = routes[start + i]
        except:
            try:
                row2[i] = routes[i + start]
            except:
                row2[i] = "X"

    sortedRow2 = dict(sorted(row2.items(), key=lambda x:x[1]))
    boxedColumn = list(sortedRow2.keys())[0]
    return row2, [boxedColumn]

def row(table, rowNumber, boxed):
    rowAbove = table[rowNumber-2]
    row = {}
    row[boxed[-1] + "_"] = "_"
    for i in boxed:
        row[i] = rowAbove[i]
        #Filling in boxed columns
    for column in table[0][1:]:
        filled = 0
        for boxedColumn in boxed:
            if column == boxedColumn:
                filled = 1
                break
        if filled == 0:
            #Not a column with boxed values
            try:
                value = routes[boxed[-1] + column]
            except:
                try:
                    value = routes[column + boxed[-1]]
                except:
                    value = "X"
            if value != "X":
                if rowAbove[column] != "X":
                    if int(value) + int(row[boxed[-1]]) < int(rowAbove[column]):
                    #print(f"Column: {column}\nValue: {str(int(value) + int(row[boxed[-1]]))}\nValue above: {rowAbove[column]}")
                        row[column] = str(int(value) + int(row[boxed[-1]]))
                    else:
                        row[column] = rowAbove[column]
                else:
                    row[column] = str(int(value) + int(row[boxed[-1]]))
            else:
                row[column] = rowAbove[column]
    sortedRow = dict(sorted(row.items(), key=lambda x:x[1]))
    for i in list(sortedRow.keys()):
        if i in boxed:
            continue
        else:
            boxed.append(i)
            break
    return row, boxed

def main():
    vertices = []
    for i in routes.keys():
        for l in i:
            if l in vertices:
                pass
            else:
                vertices.append(l)
    vertices.sort()
    table = []
    columnTitles = [i for i in vertices if i != start]
    table.append(columnTitles)
    table[0].insert(0, "_")
    secondRowValues, boxed = secondRow(table)
    table.append(secondRowValues)
    execution(table, boxed, 2)
    return

def execution(table, boxedColumns, rowNumber):
    rowNumber += 1
    if finish in boxedColumns:
        backTracking(table)
    else:
        boxed = boxedColumns
        rowValue, boxed = row(table, rowNumber, boxed)
        table.append(rowValue)
        execution(table, boxed, rowNumber)

def backTracking(table):
    shortestPath = table[-1][finish]
    #for i in table:
        #print(i)
    print(f"Shortest Path Length: {shortestPath}")
    path = [finish]
    objective = shortestPath
    column = finish
    pathFound = False
    while True:
        for row in table[1:]:
            if row[column] == objective:
                column = list(row)[0][0]
                path.append(column)
                if column == start:
                    pathFound = True
                    break
                objective = row[column]
                break
        if pathFound == True:
            break
    print(path[::-1])
    

    





main()
