# excel-to-cvs
Converts xlxs files into cvs
Opens cvs and stores each row into an array
Writes back the array into a new cvs file

*Bug to note: resulting new cvs file will
add quotation marks in the last element of
the row; most likely due to the element being
read as "...\r\n".

Simple framework as of now, will be subject
to further modification when applied in 
irl experience

