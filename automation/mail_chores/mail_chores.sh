# Just to avoid error
touch mailmerge_database.csv
rm mailmerge_database.csv

# Copy over the header to the database
cp mailmerge_starting_database.csv mailmerge_database.csv

# Assign chores and concat to end of file
echo 'Runing some python3'
python3 assign_chores.py | grep . | sort >> mailmerge_database.csv
cat mailmerge_database.csv
echo "Is this okay?"
read input
if [ $input == "yes" ]; then
  echo "Doing some things"
  mailmerge --no-dry-run --no-limit
else
  echo "Nope"
fi


