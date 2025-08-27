# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Volitality of gold under various indicator, and forcasting of gold price

1. price Price volitality (historical patterns)
2. central government demand (various countries governemnt are purchasing gold to divserify the connection of gold to USD
3. compare top central government demand countries' inflation, GDP,CPI.... 
--> focus country: US, becuase gold is priced in USD
4. Commodities: oil, energy, food (important commoditites that iis heavily traded amongst countries)
5. other worldwide favored assets: stock (stock and bonds, Cryptocurrency, Real Estate,Other Precious Metals)
--> when people favors need vs desire
--> when people purchase these (4/5) isntead of gold
7. inflation expectation
---> use single country inflation if no world in 1 data exist
8. world crisis that impacts gold price heavily (ie. war, financial crisis, pandemics...)

## Stakeholder & User
<Who decides? Who uses the output? Timing & workflow context>

Who Decides: No one really decides the price of gold, it the indicators' and investors' demand that drives the changes in gold price

Users: Portfolio managers, traders, economists monitoring safe-haven assets (gold is a safe asset becuase of it rarity and unproducibility) 

Workflow: Quarterly/annual reports, real time price monitor of gold and it comparison assets, real time data of world crisis

## Useful Answer & Decision
<Descriptive / Predictive / Causal; metric; artifact to deliver>
1. Type: Predictive and causal
2. Metrics:
--> GDP growth, inflation rate, unemployment, trade balance
--> Gold demand from central banks, oil benchmark prices, volatility index (VIX).
--> Correlation/causal strength of drivers on gold price movement (how heavily they impact gold price)
3. Deliverables:
--> Predictive model of gold price volatility.
--> Comparative dashboard of macro drivers (GDP, inflation, oil).
   
## Assumptions & Constraints
<Bullets: data availability, capacity, latency, compliance, etc.>
1. Data availability:
   Assumptions: 20+ years of official macroeconomic time series (GDP, CPI, PPI, trade, investment), gold spot/futures prices, oil benchmark, central bank gold reserves (IMF/World Gold Council)
   Constraint: limited real-time data
3. Technical capacity: Python
4. Latency tolerance: less frequent macro/governnetal level data sufficients to analysis, need more real-time/event driven updates for global crisis
5. Compliance & privacy: Only aggregated macro and market data used 


## Known Unknowns / Risks
<Bullets: what’s uncertain; how you’ll test or monitor>
1. Data revisions, Lag, New Report (GDP back-adjustments)
2. Unexpected global shocks
3. governemtnal policy shift (
4. Structural changes (use stock/bond sell/purchase to monitor)


## Lifecycle Mapping
Goal → Stage → Deliverable
Build forecasting models → Modeling → GDP, inflation, and CPI predictive model
1. understand data
2. find relationship between indicators and gold
3. build model - Predictive model of gold price.
4. vlidating - Crisis simulations, scenario testing

## Repo Plan
/data/ -> raw, processed, external/not up to date data
/src/ --> 
/notebooks/ --> analysis, visual, model
/docs/ --> documentation, reports
