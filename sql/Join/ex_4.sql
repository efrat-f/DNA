use sql_intro;

SELECT id, survival_rate from patient, disease
where patient.disease = disease.name
order by id