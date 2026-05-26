from jobspy import scrape_jobs
import csv
import os
from datetime import datetime


SEARCH_TERMS = [
    "estágio TI",
    "estágio python",
    "estágio dados",
    "estágio desenvolvimento",
    "estágio sistemas",
]
LOCATION     = "Natal, RN"
RESULTS      = 40
HOURS_OLD    = 72
OUTPUT_CSV   = "vagas_estagio_natal.csv"

CORES = {
    "reset"  : "\033[0m",
    "verde"  : "\033[92m",
    "amarelo": "\033[93m",
    "azul"   : "\033[94m",
    "cinza"  : "\033[90m",
    "negrito": "\033[1m",
    "ciano"  : "\033[96m",
    "vermelho": "\033[91m",
}
C = CORES

def cor(texto, *estilos):
    return "".join(CORES[e] for e in estilos) + texto + CORES["reset"]

def linha(char="─", n=65):
    print(cor(char * n, "cinza"))

def cabecalho():
    os.system("cls" if os.name == "nt" else "clear")
    linha("═")
    print(cor("   BUSCADOR DE VAGAS DE ESTÁGIO — NATAL, RN", "negrito", "ciano"))
    print(cor(f"  Atualizado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}", "cinza"))
    linha("═")


def buscar_vagas():
    print(cor("\n⏳ Buscando vagas... aguarde.\n", "amarelo"))
    todas = []
    ids_vistos = set()

    for termo in SEARCH_TERMS:
        print(cor(f"  Pesquisando: {termo}", "cinza"))
        try:
            jobs = scrape_jobs(
                site_name=["indeed", "linkedin", "google"],
                search_term=termo,
                google_search_term=f"{termo} próximo de Natal, RN",
                location=LOCATION,
                results_wanted=RESULTS,
                hours_old=HOURS_OLD,
                country_indeed="brazil",
            )
            for _, row in jobs.iterrows():
                uid = str(row.get("id", "")) or f"{row.get('company','')}-{row.get('title','')}"
                if uid not in ids_vistos:
                    ids_vistos.add(uid)
                    todas.append(row)
        except Exception as e:
            print(cor(f"  ⚠  Erro em '{termo}': {e}", "vermelho"))

    return todas

def exibir_vagas(vagas):
    linha()
    print(cor(f"    {len(vagas)} vagas encontradas\n", "verde", "negrito"))

    for i, v in enumerate(vagas, 1):
        titulo   = str(v.get("title",   "Sem título"))[:60]
        empresa  = str(v.get("company", "Empresa não informada"))[:40]
        local    = str(v.get("location",""))[:40] or LOCATION
        site     = str(v.get("site",    ""))
        url      = str(v.get("job_url", ""))
        email    = str(v.get("emails",  "") or "")
        data     = str(v.get("date_posted", "") or "")

        print(cor(f"  [{i:02d}] ", "cinza") + cor(titulo, "negrito", "azul"))
        print(f"        {cor(empresa, 'verde')}")
        if local:
            print(f"         {cor(local, 'cinza')}")
        if data:
            print(f"         {cor(data, 'cinza')}")
        if site:
            print(f"         {cor(site.capitalize(), 'amarelo')}")
        if email:
            print(f"         {cor(email, 'ciano')}")
        if url and url != "nan":
            print(f"        {cor(url[:80], 'cinza')}")
        linha("·")


def resumo_empresas(vagas):
    linha("═")
    print(cor("   EMPRESAS QUE ESTÃO CONTRATANDO (para contato direto)\n", "negrito", "ciano"))

    empresas = {}
    for v in vagas:
        emp = str(v.get("company", "Não informado"))
        if emp not in empresas:
            empresas[emp] = {
                "vagas"  : [],
                "emails" : set(),
                "urls"   : [],
                "sites"  : set(),
            }
        empresas[emp]["vagas"].append(str(v.get("title", "")))
        email = str(v.get("emails", "") or "")
        if email and email != "nan":
            empresas[emp]["emails"].add(email)
        url = str(v.get("job_url", "") or "")
        if url and url != "nan":
            empresas[emp]["urls"].append(url)
        site = str(v.get("site", "") or "")
        if site:
            empresas[emp]["sites"].add(site)

    for emp, dados in sorted(empresas.items()):
        print(cor(f"  {emp}", "verde", "negrito"))
        for vaga in set(dados["vagas"]):
            print(f"     • {vaga}")
        if dados["emails"]:
            print(f"      {cor(', '.join(dados['emails']), 'ciano')}")
        if dados["sites"]:
            print(f"    {cor(', '.join(dados['sites']), 'amarelo')}")
        if dados["urls"]:
            print(f"     {cor(dados['urls'][0][:75], 'cinza')}")
        print()


def salvar_csv(vagas):
    campos = [
        "title", "company", "location", "date_posted",
        "site", "job_url", "emails", "description",
        "job_type", "salary_source", "interval",
        "min_amount", "max_amount", "currency",
    ]

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=campos,
            quoting=csv.QUOTE_NONNUMERIC,
            escapechar="\\",
            extrasaction="ignore",
        )
        writer.writeheader()
        for v in vagas:
            row = {c: v.get(c, "") for c in campos}
            writer.writerow(row)

    linha("═")
    print(cor(f"   CSV salvo: {cor(OUTPUT_CSV, 'verde')}", "negrito"))
    print(cor(f"     {len(vagas)} vagas  |  Abra no Excel, LibreOffice ou Google Sheets", "cinza"))
    linha("═")
    print()


if __name__ == "__main__":
    cabecalho()
    vagas = buscar_vagas()

    if not vagas:
        print(cor("\n  Nenhuma vaga encontrada. Tente aumentar hours_old ou mudar os termos.\n", "vermelho"))
    else:
        cabecalho()
        exibir_vagas(vagas)
        resumo_empresas(vagas)
        salvar_csv(vagas)