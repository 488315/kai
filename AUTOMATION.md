# Keeping the distillation current

## Current status

Updates are manual. This repository does not configure a scheduled job, connect to private services, or claim daily synchronization.

## Reviewed update procedure

1. Gather only intentionally public evidence or content Kai explicitly approves for publication.
2. Identify the existing statement that needs revision and the public source supporting it.
3. Edit the affected living document. Keep durable principles separate from current status.
4. Review every changed file and the staged diff for private content and unsupported attribution.
5. Exercise applicable cases in evals/CASES.md. Record the actual host, inputs, observations, and remaining limitations outside this public repository if the evidence contains private data.
6. Commit the bounded update, publish through the authorized workflow, and verify the remote files and loader URLs.
7. Update CURRENT's review date only when a review actually occurs.

## Requirements for future automation

Any future implementation must use an explicit public-source allowlist, preserve provenance, draft reviewable changes, reject incomplete or inconsistent input, and avoid automatic invention of personal views. Maintainer review is required before changes to Kai's viewpoints are published.

Fetch failure must preserve the last valid committed docs and report the failed refresh. Private-source access must not be introduced implicitly. A running scheduler alone would not prove that source review or publication works.

This section is a design requirement, not a claim that these capabilities have been implemented.
