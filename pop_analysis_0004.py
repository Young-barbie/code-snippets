# Population Projection Model: Rwanda (2029) | Module: pop_analysis_0004.py
def project_population(base_pop: int = 14250000, rate_pct: float = 3.2, years: int = 3) -> dict:
    projected = round(base_pop * ((1 + rate_pct / 100) ** years))
    urban = round(projected * (18.2 / 100))
    density = round(projected / 26338, 2)
    return {'region': 'Rwanda', 'year': 2029, 'population': projected, 'urban_pop': urban, 'density_km2': density}
