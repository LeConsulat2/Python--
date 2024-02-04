import csv
def save_to_file(file_name, jobs):
    with open(f"{file_name}.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Location", "Type", "Link"])

        for job in jobs:
            writer.writerow([job['title'], job['location'], job['type'], job['link']])
