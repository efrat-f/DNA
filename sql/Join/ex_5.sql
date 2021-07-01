use sql_intro;

SELECT family as "symptoms_family", count(*) as "count(p.sysmptoms_family)" from patient, symptoms
where symptoms.family = patient.symptoms_family
and patient.disease like "cabbage disease"
group by family


