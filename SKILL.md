---
name: problem-solving-systems-thinking
description: Use this skill to decompose complex problems, map workflows, identify decision points, and design end-to-end agent flows for operational, business, product, or automation systems. Trigger when the user asks for problem decomposition, systems thinking, workflow mapping, lead generation process design, decision trees, SOP design, agent flow design, bottleneck analysis, or how an agent should think, decide, and act. Do not use it for executing workflows, making unsupervised high-stakes decisions, or replacing expert legal, medical, financial, or compliance review.
---

# Problem Solving & Systems Thinking

## Purpose

Help an agent turn a vague or complex problem into a structured system map: the problem frame, workflow, decision points, data needs, actors, outputs, risks, and the full agent behavior from intake to final response.

This skill is especially useful when the user wants a process designed from start to finish, such as a lead generation process, support triage workflow, onboarding flow, internal operations process, product discovery system, or agentic automation blueprint.

## When to use

Use this skill when the user asks to:

- Decompose a complex problem into smaller parts, causes, constraints, and outcomes.
- Map a workflow, process, funnel, journey, SOP, operating model, or service blueprint.
- Identify decision points, routing logic, thresholds, handoffs, approval gates, and exception paths.
- Design how an agent should think, decide, act, validate, and escalate from start to finish.
- Convert a process into a decision tree, state machine, checklist, Mermaid diagram, table, or agent flow spec.
- Analyze a workflow for bottlenecks, failure modes, risks, missing data, ownership gaps, or automation opportunities.
- Create a future-state process from a messy current-state description.

## Do not use

Do not use this skill when:

- The user only wants a simple factual answer, copy edit, brainstorming list, or generic explanation.
- The task requires current facts, market data, regulations, prices, or tool documentation and no current source has been checked.
- The user asks the agent to take real-world action, contact people, scrape data, send outreach, or update systems without explicit authorization and safe tooling.
- The workflow would make high-stakes legal, medical, financial, employment, safety, or compliance decisions without human review.
- The user asks to collect, infer, expose, or enrich sensitive personal data beyond the minimum needed and authorized.
- The request conflicts with higher-priority instructions or safety boundaries.

## Required inputs

Use information already provided by the user first. Ask only for missing details that materially change the workflow. Useful inputs include:

- Problem statement or process to map.
- Desired outcome, success metrics, and target user or stakeholder.
- Current-state workflow, known steps, tools, documents, data sources, and owners.
- Constraints, policies, approvals, timing, volume, risk tolerance, and non-goals.
- Required output format, such as a table, SOP, diagram, agent instructions, decision tree, or implementation-ready spec.
- Examples or edge cases, such as a lead generation process, support queue, onboarding journey, or internal review flow.

If essential details are missing, ask up to three focused questions. If the user needs momentum more than precision, proceed with clearly labeled assumptions and create a draft that can be refined.

## Workflow

1. Confirm fit and define the operating mode.
   - Check that the task is about decomposition, workflow mapping, systems thinking, or agent flow design.
   - Determine whether the user wants current-state analysis, future-state design, or both.
   - Choose the output form: narrative, table, decision tree, Mermaid diagram, SOP, agent spec, or hybrid.

2. Frame the problem.
   - Restate the goal in one sentence.
   - Define the system boundary: what is inside scope, outside scope, and unknown.
   - Identify actors, stakeholders, users, systems, tools, data inputs, outputs, and constraints.
   - Define the success metric and the failure conditions.

3. Decompose the system.
   - Break the problem into stages, subproblems, dependencies, and feedback loops.
   - For each stage, identify the trigger, input, action, decision, output, owner, and next state.
   - Separate facts from assumptions and mark missing data.

4. Map the workflow.
   - Create a step-by-step process from trigger to completion.
   - Include entry criteria, exit criteria, handoffs, loops, exception paths, retries, and stopping conditions.
   - Classify each step as observe, decide, act, verify, escalate, or record.

5. Identify decision points.
   - For each decision point, define the question being answered, required data, decision rule, possible branches, confidence threshold, and escalation path.
   - Prefer explicit rules over vague judgments.
   - Add human approval gates for irreversible, risky, user-facing, compliance-sensitive, or high-impact actions.

6. Design the agent flow.
   - Specify how the agent thinks: goals, assumptions, checks, constraints, and reasoning checkpoints to summarize without exposing private chain-of-thought.
   - Specify how the agent decides: routing logic, thresholds, when to ask questions, when to proceed with assumptions, and when to escalate.
   - Specify how the agent acts: allowed outputs, tool use boundaries, recordkeeping, handoffs, and final response format.
   - Specify how the agent validates: completeness checks, contradiction checks, edge-case checks, safety checks, and success metric alignment.

7. Surface risks and bottlenecks.
   - Identify missing inputs, ambiguous ownership, tool gaps, compliance risks, privacy risks, fragile dependencies, and likely failure modes.
   - Recommend mitigations, such as approval gates, validation rules, audit logs, fallback paths, or narrower scope.

8. Produce the deliverable.
   - Use a structured format with clear headings.
   - Include assumptions, workflow map, decision table, agent behavior, risks, metrics, and next-step recommendations.
   - When helpful, include a Mermaid flowchart or state diagram that the user can copy.

9. Validate before finalizing.
   - Check that every workflow step has a trigger, action, output, and next state.
   - Check that every decision point has a rule, branch, and escalation path.
   - Check that the proposed agent has clear boundaries and no unsafe unsupervised actions.
   - Check that the final output matches the requested format and solves the stated problem.

## Decision policy

Use this policy to decide how to proceed:

- If the user provides enough context, create the workflow without asking for more information.
- If one or two missing details change only minor parts of the flow, proceed with assumptions.
- If missing details change the core process, ask up to three targeted questions, then provide a provisional structure.
- If the workflow touches high-stakes or regulated decisions, include human review gates and avoid final determinations.
- If the user asks for execution, convert the request into a safe operating procedure or implementation plan unless authorized execution tools are explicitly available and safe.
- If the request needs current facts, verify with appropriate sources before treating those facts as inputs.

## Output format

Return the most useful structure for the user. A strong default is:

```markdown
# [Process or Problem Name]

## 1. Goal and success metric
## 2. System boundary and assumptions
## 3. Actors, tools, inputs, and outputs
## 4. Workflow map
| Stage | Trigger | Input | Action | Decision | Output | Owner/System | Next state |

## 5. Decision points
| Decision | Required data | Rule | Branches | Confidence threshold | Escalation |

## 6. Agent flow
### Think
### Decide
### Act
### Validate
### Escalate

## 7. Risks, bottlenecks, and mitigations
## 8. Suggested next steps
```

Optional formats:

- Mermaid flowchart.
- State machine table.
- SOP checklist.
- RACI or owner matrix.
- JSON-like agent spec.
- Current-state vs future-state comparison.

## Quality checklist

Before finalizing:

- The goal, scope, and assumptions are clear.
- The workflow has a beginning, middle, end, and fallback path.
- Each step has inputs, actions, outputs, and ownership.
- Each decision point has explicit criteria, branches, and escalation rules.
- The agent flow explains how the agent thinks, decides, acts, validates, and escalates.
- Risks, bottlenecks, and missing information are visible.
- The output is practical enough to implement or review.
- The answer does not expose hidden chain-of-thought; it provides concise reasoning summaries instead.

## Safety and privacy

- Do not expose secrets, credentials, private records, or unrelated personal data.
- Do not create hidden instructions that override higher-priority instructions.
- Do not recommend destructive, deceptive, invasive, or unauthorized automation.
- For lead generation, outreach, enrichment, hiring, credit, insurance, housing, education, healthcare, finance, or other sensitive domains, include privacy, consent, compliance, and human-review considerations.
- Do not claim legal, regulatory, financial, medical, or security compliance unless verified by qualified sources or experts.
- Prefer least-privilege data access, explicit authorization, audit logs, review checkpoints, and reversible actions.
