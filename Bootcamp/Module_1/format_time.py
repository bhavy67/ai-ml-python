# Taking input
total_seconds = int(input())

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

output = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Print the output
print(output)
