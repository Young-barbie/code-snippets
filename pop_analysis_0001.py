# Population Projection Model: Kenya (2026) | Module: pop_analysis_0001.py
def project_population(base_pop: int = 56400000, rate_pct: float = 3.09, years: int = 0) -> dict:
    projected = round(base_pop * ((1 + rate_pct / 100) ** years))
    urban = round(projected * (29.5 / 100))
    density = round(projected / 580367, 2)
    return {'region': 'Kenya', 'year': 2026, 'population': projected, 'urban_pop': urban, 'density_km2': density}
