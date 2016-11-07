# Just to avoid error
touch mailmege_database.csv
rm mailmege_database.csv

# Copy over the header to the database
cp mailmerge_starting_database.csv mailmerge_database.csv

# Assign chores and concat to end of file
python3 assign_chores.py >> mailmerge_database.csv

# Mail the chores out
python3 mailmerge.py --no-dry-run --no-limit

