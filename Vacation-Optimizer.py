import holidays
from datetime import datetime, timedelta

def extended_vacation_optimization(country_code, year):
    public_holidays = holidays.CountryHoliday(country_code, years=year)
    extended_breaks = []

    # Sort holidays and extend them to the nearest weekends
    for holiday in sorted(public_holidays):
        start = holiday
        end = holiday

        # Extend backwards and forwards to include weekends and adjacent holidays
        while start.weekday() > 4 or (start - timedelta(days=1)) in public_holidays:
            start -= timedelta(days=1)
        start -= timedelta(days=start.weekday() + 1)

        while end.weekday() < 5 or (end + timedelta(days=1)) in public_holidays:
            end += timedelta(days=1)
        end += timedelta(days=6 - end.weekday())

        # Check for overlapping or adjacent breaks
        if extended_breaks and extended_breaks[-1][1] + timedelta(days=4) >= start:
            extended_breaks[-1] = (extended_breaks[-1][0], end)
        else:
            extended_breaks.append((start, end))

    # Calculate vacation days for each extended break
    vacation_plans = []
    for start, end in extended_breaks:
        total_days = (end - start).days + 1
        vacation_days = sum(1 for d in range(total_days)
                            if (start + timedelta(days=d)).weekday() < 5 and 
                            (start + timedelta(days=d)) not in public_holidays)

        vacation_period = f"{start.strftime('%B %d')} (evening) - {end.strftime('%B %d')} ({vacation_days} vacation days used for {total_days} day holiday)"
        vacation_plans.append(vacation_period)

    return vacation_plans

# Example usage
country_code = 'CZ'  # Country code
year = 2024          # Year

# Find optimized extended vacations
optimized_extended_vacations = extended_vacation_optimization(country_code, year)

optimized_extended_vacations
