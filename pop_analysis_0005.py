taclass, asdict
from typing import List, Dict
import math
import json

@dataclass
class PopulationModel:
    region: str
    base_population: int
    area_km2: float
    growth_rate_pct: float
    urban_share_pct: float
    fertility_rate: float
    life_expectancy: float

    def project_total(self, years: int) -> int:
        factor = (1.0 + self.growth_rate_pct / 100.0) ** max(0, years)
        return int(round(self.base_population * factor))

    def doubling_time(self) -> float:
        if self.growth_rate_pct <= 0:
            return float('inf')
        return round(math.log(2.0) / math.log(1.0 + self.growth_rate_pct / 100.0), 2)

    def urban_rural_split(self, years: int) -> Dict[str, int]:
        total = self.project_total(years)
        urban = int(round(total * (self.urban_share_pct / 100.0)))
        return {'total': total, 'urban': urban, 'rural': total - urban}

    def population_density(self, years: int) -> float:
        return round(self.project_total(years) / self.area_km2, 2)

    def age_cohorts(self, years: int) -> Dict[str, int]:
        total = self.project_total(years)
        youth = int(round(total * 0.39))
        working = int(round(total * 0.56))
        return {'youth': youth, 'working': working, 'elderly': total - youth - working}

def build_forecast(model: PopulationModel, start_yr: int, end_yr: int) -> List[Dict]:
    rows: List[Dict] = []
    for yr in range(start_yr, end_yr + 1):
        elapsed = yr - start_yr
        split = model.urban_rural_split(elapsed)
        cohorts = model.age_cohorts(elapsed)
        rows.append({
            'year': yr,
            'population': split['total'],
            'urban_pop': split['urban'],
            'density_km2': model.population_density(elapsed),
            'working_age': cohorts['working']
        })
    return rows

def run_model_0005() -> Dict:
    model = PopulationModel(
        region='Ethiopia',
        base_population=129700000,
        area_km2=1104300,
        growth_rate_pct=1.48,
        urban_share_pct=23.7,
        fertility_rate=3.99,
        life_expectancy=66.9
    )
    series = build_forecast(model, 2026, 2041)
    latest = series[-1]
    latest['doubling_years'] = model.doubling_time()
    latest['profile'] = asdict(model)
    return latest

if __name__ == '__main__':
    output = run_model_0005()
    print(json.dumps(output, indent=2))
