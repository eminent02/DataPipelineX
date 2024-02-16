import argparse

parser = argparse.ArgumentParser(description="CLI for data flow from source to destination")
parser.add_argument("flow", choices=["from"], help="Entry point for data flow")
parser.add_argument("source_type", choices=["s3", "csv", "json", "parquet", "sql"], help="Type of source data")
parser.add_argument("--source", help="Path or details of the source data")
parser.add_argument("destination_type", choices=["postgres"], help="Type of destination data")
parser.add_argument("--destination", help="Details of the destination database")

args = parser.parse_args()

print(args)

# def discover():
