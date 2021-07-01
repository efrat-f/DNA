use sql_intro;

SELECT ethnicity.name, count(*) as "count(p.sysmptoms_family)" from ethnicity, patient
where ethnicity.id = patient.ethnicity
and patient.disease like "lettuce disease"
group by name
