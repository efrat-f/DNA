# Goal
The goal of the system is to load, analyze, manipulate and save DNA sequences.
# Description
DNA sequences are composed of four types of nucleotides;</br>
The nucleotides are marked A (Adenine), G (Guanine), C (Cytosine) and T (Thymine).</br>
A full DNA molecule usually consists of two strands, connected to each other in base-pair connections: As with Ts,  and Cs with Gs.</br>
Three successive nucleotides generate a codon, which might be chemically "read" in various ways.</br>
The system will interact with the user through a CLI (Command Line Interface) that uses the standard I/O. Using that interface, the user will be able to load DNA sequences from files, to analyze them, to manipulate them (e.g. by extracting sequence slices or by modifying the sequence), and to store modified sequences and reports.</br>
The commands are detailed in the following sections.</br>
## The Command Line Interface (CLI)
The prompt of the CLI is usually > cmd >>></br>
### Sequences
The application's most important elements are sequences.</br>
These are DNA sequences (composed of the four characters A, C, T and G).</br>
Each sequence that is held in the app's memory has a name and sequence number.</br>
When referring to a sequence in commands, unless otherwise defined, it is possible to refer it either by its ID or by its name.</br>
Reference to the sequence number is done using the hash character #</br>
For example:</br>
#107 means sequence number 107.</br>
Reference to the sequence name is done using the at character @</br>
For example:</br>
@dolly-dna refers to the sequence named dolly-dna.</br>
## Common CLI markings
● [argument] - Words starting with "[", ending with "]" represent optional arguments.</br>
● \<argument> - Words starting with "<", ending with ">" represent required arguments. </br>
● arg1|arg2 - Pipe sign ("|") between words represents that each one of them can be used.</br>
Example using bash command cp:</br>
cp [-r|-f] \<source> [\<source2> [\<source3> ...]] \<destination></br>
Means that:</br>
● cp can be used with flag -r or with flag -f, but they both are optional.</br>
● After the flags (if they exist) must be the source files. At least one, but can be many.</br>
● At the end must be the destination.</br>
## Sequence Creation Commands
The following commands are being used to ​generate new sequences​:
### new
`> cmd >>> new <sequence> [@<sequence_name>]`</br>
Creates a new sequence, as described by the followed sequence.</br>
If the ​@\<sequence_name> is used, then this will be the name of the new sequence.</br>
Otherwise, a default name will be provided - ​seq1 (or ​seq2, ​seq3 and so on, if the
name is already taken).</br>
The new sequence, its name and its number (internal ID, starting with 1) are printed.</br>
For example:</br>
`> cmd >>> new ATACTGCCTGAATAC @short_seq`</br>
will create that sequence;</br>
if this is the first sequence, it will be numbered "1" and the following will be printed:</br>
`[1] short_seq: ATACTGCCTGAATAC`</br>
### load
`> cmd >>> load <file_name> [@<sequence_name>]`</br>
loads the sequence from the file, assigns it with a number (ID) and a default name, if one was not provided (based on the file name, possibly postfixed with a number if the name already exists), and prints it.</br>
For example:</br>
`> cmd >>> load my_dna_seq.rawdna`</br>
will load the sequence from the file my_dna_seq.rawdna and will print its assigned ID, its name and the sequence (no more than 40 chars;</br>
So, a typical output might be:</br>
`[14] my_dna_seq: AACGTTTTTGAACACCAGTCAACACATTG`</br>
### dup
`> cmd >>> dup \<seq> [@\<new_seq_name>]`</br>
duplicates the sequence.</br>
If a new name is not provided, then it will be based on the name of ​\<seq>, suffixed by ​_1 (or ​_2, ​_3, ... if the name is already taken).</br>
For example:</br>
`> cmd >>> dup #22`</br>
will result in</br>
`[23] conseq_1_1: ATACTGCCTGAATACAGCATAGCATTGCCT`</br>
## Sequence Manipulation Commands
The following commands ​manipulate existing sequences​:</br>
Their default behavior is to modify the source sequence in-place (that is, the original ID and name of the sequence are left the same, only its content is modified).</br>
● If a colon ​: appears after the command's argument, then the original</br>
sequence is left untouched, and a new sequence is generated with the
manipulation results.</br>
● If an argument of the form ​@\<new_seq_name> is provided after the colon, then this is the name of the new sequence.</br>
● Otherwise, if ​@@ instead, then the name of the new sequence is automatically generated by the app.</br>
Each command might generate a different default name.</br>
When a sequence is required as a source, both ID (​#<seq_id>) or name (​@seq_name) are acceptable, unless otherwise defined.</br>
### slice
`> cmd >>> slice <seq> <from_ind> <to_ind> [: [@<new_seq_name>|@@]]`</br>
Slices the sequence, so that starts in \<from_ind> (0-based index) and ends in \<to_ind>(inclusive).</br>
If @\<new_seq_name> is provided, the results will create a new sequence with that name.</br>
If @@ is provided, the results will create a new sequence with auto-generate name, based on the name of the original sequence, with the suffix _s1 (or, if that name is already occupied, with the suffix _s2, and so on).</br>
For example:</br>
Assuming that the former short_seq's ID is 1, the following command:</br>
`> cmd >>> slice #1 4 9`</br>
will change the sequence to TGCCT (Letters at indices 4,5,6,7,8) and print the output:</br>
`[1] short_seq: TGCCT`</br>
If @@ was provided to the same command, then sequence 1 would have not changed, and a new sequence would have been generated instead.</br>
A typical call, then, might look like:</br>
`> cmd >>> slice #1 4 8 : @@`</br>
`[19] short_seq_s1: TGCCT`</br>
#### replace
`> cmd >>> replace <seq> <index> <new_letter> [: [@<new_seq_name>|@@]]`</br>
replaces the letter in the (0-based) index of \​<seq> by \<new_letter>.
If ​@\<new_seq_name> is provided, the original sequence is left untouched and the result is put in a newly created sequence with that name.</br>
If ​@@ is provided, the name is based on the original sequence, with the suffix ​_r1 (or, if that name is already existing, ​_r2 and so on).</br>
The command might get more than a single replacement. In that case, after \​<seq> there will be more than one pair of ​<index> and ​\<new_letter>.</br>
For example:</br>
`> cmd >>> replace @short_seq_s1 0 A 3 A : @repl_seq`</br>
will result in the following output:</br>
`[20] repl_seq: AGCAT`</br>
## Sequence Management Commands
This is a list of commands that manage existing sequences (without manipulating them).</br>
### del
`> cmd >>> del \<seq>`</br>
deletes that sequence.</br>
Before deleting it, the user is asked to confirm that:</br>
Confirmation is done by entering y or Y, Entering n or N cancels the deletion. Any other input will result in a message that asks the user again to confirm the deletion.</br>
Once confirmed, the sequence is deleted and a message is printed. Otherwise, a cancellation message is printed.</br>
So, a deletion scenario might look like:</br>
>\> cmd >>> del #23</br>
Do you really want to delete conseq_1_1:</br> ATACTGCCTGAATACAGCATAGCATTGCCT?</br>
Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.</br>
\> confirm >>> x</br>
You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.</br>
\> confirm >>> Y</br>
Deleted: [23] conseq_1_1: ATACTGCCTGAATACAGCATAGCATTGCCT</br>
### save
`> cmd >>> save <seq> [<filename>]`</br>
saves sequence <seq> to a file.</br>
If \<filename> is not provided, the sequence name is being used.</br>
The filename is suffixed by .rawdna.</br>
## Sequence Analysis Commands
### findall
finds a sub-sequence within a sequence, return all the indices where the sub-sequence appears.</br>
It has two flavors:</br>
1. Takes an expressed sub-sequence:</br>
`> cmd >>> findall <seq> <expressed_sub_seq>`</br>
returns the (0-based) index of the appearance of \<expressed_sub_seq> in the sequence \<seq>.
2. Refers an existing sub-sequence:</br>
`> cmd >>> findall <seq_to_find_in> <seq_to_be_found>`</br>

Thus, for example:</br>
If seq #11 is as appears above, and sequence #25 is CTTGGA, it might look like:
work very similar to ​find, only they </br>
Thus, for example:</br>
Using the above sequence for sequence #11, it might look like:</br>
>\> cmd >>> findall #11 GA</br>
8 16</br>
\> cmd >>> find #11 #25</br>
4
## Batch Commands
### Batch Creation
`> cmd >>>batch <batch_name>`</br>
Batch mode allows the user to define a series of actions that will take place one after another.</br>
In order to define a batch, the user enters the command batch, followed by the name of that new batch. Then, it enters into batch mode, where any command is not being activated immediately, but rather, entered into the batch.</br>
The command end ends the batch mode.</br>
For example:</br>
>\> cmd >>> batch my_batch</br>
\> batch >>> load basil_dna.rawdna @basil</br>
\> batch >>> pair basil @basil_pair</br>
\> batch >>> find ## TGATTCTC : @start_slice</br>
\> batch >>> find ## TTTTAAAATTTTCCCC</br>
\> batch >>> calc __ + 4</br>
\> batch >>> slice @basil_pair @start_slice __ @basil_interesting_part</br>
\> batch >>> save ##</br>
\> batch >>> end</br>
\> cmd >>></br>

This batch (when run) will load a sequence from the file basil_dna.rawdna and will keep it under the name basil.</br>
Then, it will create its pair and keep it under the name basil_pair.
After that, it will slice it from the first index of the sub-sequence TGATTCTC to four nucleodites after the first index of the sub-sequence TTTTAAAATTTTCCCC (that is, it will include the first four T of that sequence). That slice will be kept under the name basil_interesting_part and then will be saved to disk using that name (with the .rawdna suffix).</br>
When the batch mode ends, the batch is added to the list of active batches - nothing is being activated yet.</br>
### Running Batches
The command run \<@batchname> runs a batch, that is, executes it as if the commands were entered manually.</br>
### Listing Batches
The command batchlist shows a list of all the batch names.</br>
### Showing a Batch
The command batchshow \<@batch_name> shows the content of that batch.
### Saving a batch is done using the command batchsave, followed by the filename.
If the filename is omitted, then the batch name is being used as the filename, with the suffix .dnabatch</br>
The batch is saved exactly as it is written in the CLI (without the prompt, of course).</br>
Thus, for example:</br>
The above script will be saved as:</br>
> load basil_dna.rawdna @basil</br>
pair basil @basil_pair</br>
find ## TGATTCTC : @start_slice</br>
find ## TTTTAAAATTTTCCCC</br>
calc __ + 4</br>
slice @basil_pair @start_slice __ @basil_interesting_part</br>
save ##</br>
### Loading Batches
Loading a batch is done using the command batchload, followed by the filename to be loaded.</br>
The loaded batch will have that name (without the .dnabatch suffix, if appears).</br>
If the command is followed by : @\<batch_name>, then it will be kept as batch_name</br>