import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def scrape_holidays(country_url):
    page = requests.get(country_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    holidays_table = soup.find("table", {"id": "holidays-table"})
    if not holidays_table:
        return {}

    holidays = {}
    for row in holidays_table.find_all("tr"):
        date_cell = row.find("th", {"class": "nw"})
        cells = row.find_all("td")
        
        if date_cell and len(cells) >= 2:
            raw_date = date_cell.text + " 2024"
            date = datetime.strptime(raw_date, '%b %d %Y').date()
            name = cells[1].text.strip()
            holiday_type = cells[2].text.strip() if len(cells) > 2 else "Unknown"
            holidays[date] = {'name': name, 'type': holiday_type}

    return holidays

def extended_vacation_optimization(country_url, year):
    public_holidays = scrape_holidays(country_url)
    extended_breaks = []

    for holiday_date in sorted(public_holidays):
        start = holiday_date
        end = holiday_date
        included_holidays = [public_holidays[holiday_date]['name']]

        while start.weekday() > 4 or (start - timedelta(days=1)) in public_holidays:
            start -= timedelta(days=1)
            if (start in public_holidays) and (public_holidays[start]['name'] not in included_holidays):
                included_holidays.append(public_holidays[start]['name'])
        start -= timedelta(days=start.weekday() + 1)

        while end.weekday() < 5 or (end + timedelta(days=1)) in public_holidays:
            end += timedelta(days=1)
            if (end in public_holidays) and (public_holidays[end]['name'] not in included_holidays):
                included_holidays.append(public_holidays[end]['name'])
        end += timedelta(days=6 - end.weekday())

        if extended_breaks and extended_breaks[-1][1] + timedelta(days=4) >= start:
            extended_breaks[-1] = (extended_breaks[-1][0], end, extended_breaks[-1][2] + included_holidays)
        else:
            extended_breaks.append((start, end, included_holidays))

    vacation_plans = [["Start Date", "End Date", "Vacation Days Used", "Total Days", "Included Holidays"]]
    for start, end, holidays_in_period in extended_breaks:
        total_days = (end - start).days + 1
        vacation_days = sum(1 for d in range(total_days)
                            if (start + timedelta(days=d)).weekday() < 5 and 
                            (start + timedelta(days=d)) not in public_holidays)
        holidays_str = ", ".join(holidays_in_period)
        vacation_plans.append([start.strftime('%B %d'), end.strftime('%B %d'), vacation_days, total_days, holidays_str])

    return vacation_plans

def print_markdown_table(data):
    separator = "|"
    headers = data[0]
    header_line = separator.join(headers)
    separator_line = separator.join(["---"] * len(headers))
    print(header_line)
    print(separator_line)
    for row in data[1:]:
        print(separator.join(map(str, row)))

country_url = 'https://www.timeanddate.com/holidays/czech/'
optimized_extended_vacations = extended_vacation_optimization(country_url, 2024)
print_markdown_table(optimized_extended_vacations)
