import csv


def reverse_records(csv_filename, new_filename):
    csv_file = open(csv_filename, "r")
    reader = csv.reader(csv_file)
    header = next(reader)
    data2d = list(reader)
    newdata2d = data2d[::-1]
    csv_file.close()
    new_file = open(new_filename, "w")
    writer = csv.writer(new_file)
    writer.writerow(header)
    writer.writerows(newdata2d)
    new_file.close()
