# Just to avoid error
touch mailmege_database.csv
rm mailmege_database.csv

# Copy over the header to the database
cp mailmerge_starting_database.csv mailmerge_database.csv

# Assign chores and concat to end of file
python3 assign_chores.py | sort >> mailmerge_database.csv
grep . mailmege_database.csv | sort > mailmege_database.csv
# sed -i '/^$/d' mailmerge_database.csv

# Mail the chores out
mailmerge --dry-run --no-limit
