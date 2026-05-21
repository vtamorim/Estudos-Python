from jobspy import scrape_jobs
import csv

jobs = scrape_jobs (
    site_name=["indeed", "linkedin", "google","glassdoor"],
    search_term="estágio TI OR estágio python OR estágio dados",
    google_search_term="Estágio TI próximo de Natal, RN",
    location = "Natal, RN",
    results_wanted=40,
    hours_old=72,
    country_indeed='brazil',

)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
if not jobs.empty:
    print(jobs[["company","title"]])
else:
    print("Nenhuma vaga encontrada")
jobs.to_csv("jobs.csv" , quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)