use sql_intro;

/* drop TABLE ethnicity;
drop TABLE gender;
drop TABLE disease;
 */

CREATE TABLE ethnicity(
id INTEGER primary key, 
name VARCHAR(20)); 

CREATE TABLE gender(
id INTEGER primary key, 
name VARCHAR(20)); 

CREATE TABLE symptoms( 
family INTEGER PRIMARY KEY,
fever boolean,
blue_whelth boolean,
low_bp boolean); 

CREATE TABLE disease(
name VARCHAR(20) PRIMARY KEY, 
survival_rate FLOAT); 

CREATE TABLE patient(
id INTEGER primary key AUTO_INCREMENT, 
ethnicity INTEGER,
gender INTEGER,
symptoms_family INTEGER,
disease VARCHAR(20),
FOREIGN KEY (ethnicity) REFERENCES ethnicity(id)
ON DELETE CASCADE,
FOREIGN KEY (gender) REFERENCES gender(id)
ON DELETE CASCADE,
FOREIGN KEY (symptoms_family) REFERENCES symptoms(family)
ON DELETE CASCADE,
FOREIGN KEY (disease) REFERENCES disease(name)
ON DELETE CASCADE);

