from dataframe import DataFrame

# Create DataFrame instance
df = DataFrame()

# Read CSV file
df.read_csv("sachin.txt", names=["Date", "Country", "Runs", "Balls"], delimiter=" ")

# Displays first 5 rows
print("First 5 Rows\n")
df.head()

# Displays last 5 rows
print("\nLast 5 Rows\n")
df.tail()

# Displays Runs and Balls
runs = df.getColumn("Runs")
balls = df.getColumn("Balls")

print("\nRuns        Balls")
print("------------------")
for runs_balls in range(len(runs)):
    print(f"{int(runs[runs_balls]):>10} {int(balls[runs_balls]):>10}")

# Add strike_rate column
strike_rate = [
    round((int(runs) / int(balls)) * 100, 2) if int(balls) > 0 else 0
    for runs, balls in zip(runs, df.getColumn("Balls"))
]
df.addColumn("Strike Rate", strike_rate)

# Display updated DataFrame (first 10 rows)
print("\nUpdated DataFrame (First 10 Rows) \n")
print("Date         | Country      | Runs       | Balls      | Strike Rate")
print("---------------------------------------------------------------")
for index in range(10):
    row = {
        "Date": df.frame["Date"][index],
        "Country": df.frame["Country"][index],
        "Runs": int(df.frame["Runs"][index]),
        "Balls": int(df.frame["Balls"][index]),
        "Strike Rate": df.frame["Strike Rate"][index],
    }
    print(
        f"{row['Date']:<12} | {row['Country']:<12} | {row['Runs']:>10} | {row['Balls']:>10} | {row['Strike Rate']:>12.2f}"
    )