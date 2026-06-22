# Lead Generation Workflow Example

## Goal

Design a lead generation process that converts target accounts or prospects into qualified sales conversations while keeping data quality, compliance, and human approval controls visible.

## System boundary

Inside scope:

- Define ideal customer profile and source criteria.
- Build or receive a prospect list.
- Validate, enrich, score, segment, personalize, route, and hand off leads.
- Track status, decisions, risks, and next actions.

Outside scope unless explicitly authorized:

- Scraping websites, buying lists, sending outreach, or updating CRM records.
- Making legal compliance claims.
- Collecting sensitive personal data not needed for the workflow.

## Workflow map

| Stage | Trigger | Input | Action | Decision | Output | Owner/System | Next state |
|---|---|---|---|---|---|---|---|
| 1. Define ICP | Campaign request | Target market, offer, constraints | Define fit criteria and exclusions | Is the ICP specific enough? | ICP criteria | Marketing or sales lead | Source leads |
| 2. Source leads | Approved ICP | Source list or query | Gather authorized candidates | Does the source meet policy? | Raw lead list | Human or approved tool | Deduplicate |
| 3. Deduplicate | New list received | Lead records, CRM records | Match by domain, email, account, or record ID | Is this already known? | Unique leads | Agent or CRM | Validate data |
| 4. Validate data | Unique leads | Email, account, role, geography | Check completeness and reliability | Is required data present? | Validated lead profile | Agent | Score lead |
| 5. Score lead | Validated profile | ICP criteria, intent signals, firmographics | Assign fit and priority score | Score above threshold? | Qualified, nurture, or reject label | Agent | Segment leads |
| 6. Segment leads | Scored leads | Persona, industry, pain point, priority | Group leads for messaging or routing | Needs human review? | Segment and routing tag | Agent | Draft next action |
| 7. Draft next action | Segment assigned | Offer, context, constraints | Draft recommended outreach, research note, or sales brief | Is action safe and approved? | Draft and rationale | Agent | Human approval |
| 8. Human approval | Draft ready | Draft, score, data sources, assumptions | Review and approve, edit, or reject | Approved? | Approved action or revision request | Human owner | Execute or revise |
| 9. Handoff | Approved qualified lead | Lead profile, score, notes, next action | Send to sales or nurture queue | Ready for sales? | Sales brief or nurture record | Sales/marketing | Track outcome |
| 10. Track outcome | Handoff complete | Replies, meetings, dispositions | Record result and learnings | Feedback changes criteria? | Updated criteria and metrics | Team | Improve loop |

## Decision points

| Decision | Required data | Rule | Branches | Confidence threshold | Escalation |
|---|---|---|---|---|---|
| ICP fit | Account size, industry, geography, use case | Must meet required ICP criteria and no exclusion criteria | Fit, partial fit, no fit | Medium or higher | Human review for partial fit |
| Data completeness | Email, company, role, account domain | Required fields must be present and reliable | Complete, incomplete, invalid | High | Request enrichment or reject |
| Lead score | Fit score, intent, relevance, freshness | Route to sales if above threshold set by user | Sales, nurture, reject | Medium | Human review near threshold |
| Personalization readiness | Safe context, approved claims, relevant pain point | Draft only from provided or verified information | Ready, needs research, do not use | High | Human approval before outreach |
| Compliance or privacy risk | Region, data source, consent, outreach rules | If uncertain, do not execute outreach | Safe to draft, needs review, blocked | High | Compliance or authorized owner |
| Handoff readiness | Score, notes, next action, owner | Handoff only when required fields and owner exist | Handoff, nurture, revise | High | Sales lead review |

## Agent flow

### Think

- Restate the campaign goal and success metric.
- Identify ICP criteria, exclusions, data sources, tools, owners, and constraints.
- Separate verified facts from assumptions.
- Flag privacy, compliance, and data-quality concerns.

### Decide

- Ask for missing criteria only if they change scoring or routing.
- Use explicit thresholds for qualification and escalation.
- Route uncertain, borderline, or policy-sensitive leads to human review.
- Never treat a generated score as final truth without review when impact is meaningful.

### Act

- Produce a workflow map, decision table, scoring outline, handoff checklist, and risk register.
- Draft recommended next actions without sending messages unless explicitly authorized and safe.
- Create concise sales briefs using only approved or verified data.

### Validate

- Confirm every stage has inputs, outputs, owner, and next state.
- Confirm every branch has an escalation path.
- Confirm personal data use is necessary, authorized, and minimized.
- Confirm the workflow includes a feedback loop from outcomes to ICP or scoring updates.

## Metrics

- Lead acceptance rate.
- Meeting conversion rate.
- Data completeness rate.
- Duplicate rate.
- Human approval rate.
- False-positive and false-negative qualification rate.
- Time from source to qualified handoff.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Bad source data | Validate required fields and track source reliability. |
| Over-automation | Require approval for outreach, CRM updates, and borderline qualification. |
| Privacy or compliance issues | Minimize personal data and escalate uncertainty to authorized reviewers. |
| Unclear ICP | Add a human checkpoint before sourcing or scoring. |
| Low-quality personalization | Use only provided or verified facts and label assumptions. |
