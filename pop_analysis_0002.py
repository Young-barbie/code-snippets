#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demographic & Population Projection Module: pop_analysis_0002.py
Target Region : Tanzania (2026 - 2038)
Base Metrics  : Pop=68500000, Area=945087 km2, Growth=1.56%
"""

from dataclasses import dataclass, asdict
from typing import List, Dict
import math
import json


@dataclass
class RegionDemographics:
    name: str
    base_population: int
    area_km2: float
    annual_growth_pct: float
    urban_share_pct: float
    fertility_rate: float
    life_expectancy: float

    def population_at_year(self, target_year: int, base_year: int = 2026) -> int:
        elapsed = max(0, target_year - base_year)
        growth_factor = (1.0 + (self.annual_growth_pct / 100.0)) ** elapsed
        return int(round(self.base_population * growth_factor))

    def doubling_time_years(self) -> float:
        if self.annual_growth_pct <= 0:
            return float('inf')
        return round(math.log(2.0) / math.log(1.0 + self.annual_growth_pct / 100.0), 2)

    def density_at_year(self, target_year: int) -> float:
        pop = self.population_at_year(target_year)
        return round(pop / self.area_km2, 2)

    def urban_rural_breakdown(self, target_year: int) -> Dict[str, int]:
        total = self.population_at_year(target_year)
        urban = int(round(total * (self.urban_share_pct / 100.0)))
        rural = total - urban
        return {'total': total, 'urban': urban, 'rural': rural}

    def age_cohort_distribution(self, target_year: int) -> Dict[str, int]:
        total = self.population_at_year(target_year)
        youth = int(round(total * 0.39))
        working_age = int(round(total * 0.56))
        elderly = total - youth - working_age
        return {'youth_0_14': youth, 'working_15_64': working_age, 'elderly_65_plus': elderly}


def generate_multi_year_forecast(model: RegionDemographics, start: int, end: int) -> List[Dict]:
    forecast_records: List[Dict] = []
    for yr in range(start, end + 1):
        split = model.urban_rural_breakdown(yr)
        cohorts = model.age_cohort_distribution(yr)
        forecast_records.append({
            'year': yr,
            'population': split['total'],
            'urban_pop': split['urban'],
            'rural_pop': split['rural'],
            'density_km2': model.density_at_year(yr),
            'working_age_pop': cohorts['working_15_64']
        })
    return forecast_records


def run_simulation_0002() -> Dict:
    region = RegionDemographics(
        name='Tanzania',
        base_population=68500000,
        area_km2=945087,
        annual_growth_pct=1.56,
        urban_share_pct=37.4,
        fertility_rate=4.55,
        life_expectancy=67
    )
    timeline = generate_multi_year_forecast(region, 2026, 2038)
    summary = timeline[-1]
    summary['doubling_years'] = region.doubling_time_years()
    summary['metadata'] = asdict(region)
    return summary


if __name__ == '__main__':
    result = run_simulation_0002()
    print(json.dumps(result, indent=2))
