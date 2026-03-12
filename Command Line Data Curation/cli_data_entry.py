import csv
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()


def main():
    console.print("[bold cyan]Electronic Products Tracker[/bold cyan]\n")

    # Pre-created example data
    example_products = [
        ["Smartphone", "2022", "$799"],
        ["Laptop", "2021", "$1200"],
        ["Tablet", "2023", "$499"]
    ]

    # Show example data
    example_table = Table(title="Example Electronic Products")
    example_table.add_column("Device", style="cyan")
    example_table.add_column("Year", style="green")
    example_table.add_column("Cost", style="magenta")

    for product in example_products:
        example_table.add_row(product[0], product[1], product[2])

    console.print("Here are some example products you can add:\n")
    console.print(example_table)
    console.print("\nNow enter your own products:\n")
    
    products = []

    while True:
        device = input("Enter device name: ")
        year = input("Enter purchase year: ")
        cost = input("Enter cost (USD): ")
        cost_display = f"${cost}"

        products.append([device, year, cost_display])

        more = input("Add another product? (y/n): ").lower()
        if more != "y":
            break

    table = Table(title="Your Electronic Products")

    table.add_column("Device", style="cyan")
    table.add_column("Year", style="green")
    table.add_column("Cost", style="magenta")

    for product in products:
        table.add_row(product[0], product[1], product[2])

    console.print("\nHere is the data you entered:\n")
    console.print(table)

    confirm = input("\nSave this data to CSV? (y/n): ").lower()

    if confirm != "y":
        console.print("[red]Data not saved.[/red]")
        return

    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / "electronics.csv"

    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["device", "year", "cost"])
        writer.writerows(products)

    console.print("[bold green]Data saved successfully![/bold green]")
    console.print(f"File location: {file_path.resolve()}")


if __name__ == "__main__":
    main()