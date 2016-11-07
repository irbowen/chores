touch mailmege_database.csv
rm mailmege_database.csv
cp mailmerge_starting_database.csv mailmerge_database.csv
python3 assign_chores.py >> mailmerge_database.csv

python3 mailmerge.py --dry-run --no-limit
