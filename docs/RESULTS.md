# Execution record — Smart Log Analyzer

**Status:** Local execution completed using bundled fixtures.  
**Python:** 3.13.5  
**Execution time:** 1.76 seconds in the packaging environment (not a standardized benchmark).  
**Method:** `python src/analyze_logs.py sample/app.log --top 20`

## Observed output

![Observed output](../assets/result.svg)

| Field | Observed value |
|:--|--:|
| Level counts · error | 3 |
| Level counts · info | 1 |

**Raw output:** [execution.txt](../results/execution.txt)  
**Command records and SHA-256 digests:** [execution.json](../results/execution.json)

## Interpretation

Results were computed on the included test fixtures. They demonstrate one successful invocation, not measured generalization, comparative performance, system availability or operational readiness. If the fixtures or application are synthetic, values remain synthetic or simulated.
