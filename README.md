# Problem Solving & Systems Thinking

## Overview

This skill helps an agent decompose complex problems, map workflows, identify decision points, and design an agent's end-to-end flow from intake through validation and final response.

Use it when a user asks for process design, systems thinking, workflow mapping, lead generation flow design, decision trees, SOP design, bottleneck analysis, or agent behavior design.

## What it creates

The skill can produce:

- Problem decompositions and system boundaries.
- Current-state and future-state workflow maps.
- Decision tables with rules, branches, thresholds, and escalation paths.
- Agent flow specs covering how the agent thinks, decides, acts, validates, and escalates.
- Mermaid diagrams, SOPs, state machines, RACI-style handoff tables, and implementation-ready process specs.
- Risk, bottleneck, and missing-information analysis.

## Example user prompts

- "Map our lead generation process from prospecting to sales handoff."
- "Decompose this messy customer onboarding problem and design the workflow."
- "Create a decision tree for support ticket triage."
- "Design how an agent should think, decide, and act for invoice review."
- "Turn this process into a state machine with escalation paths."

## Contents

- `SKILL.md`: agent-facing instructions, trigger description, boundaries, workflow, decision policy, output formats, quality checks, and safety rules.
- `README.md`: human-readable overview and usage notes.
- `agents/openai.yaml`: OpenAI metadata, default prompt, invocation policy, and file dependencies.
- `references/style-guide.md`: style rules, output patterns, terminology, edge cases, and anti-patterns.
- `references/lead-generation-example.md`: worked example for mapping a lead generation workflow.
- `assets/workflow-map-template.md`: reusable workflow mapping template.
- `scripts/example_helper.py`: deterministic helper that checks whether a Markdown workflow map includes key sections.
- `assets/.gitkeep`: keeps the assets directory in version control.

## Package structure

```text
problem-solving-systems-thinking/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- assets/
|   |-- .gitkeep
|   `-- workflow-map-template.md
|-- references/
|   |-- style-guide.md
|   `-- lead-generation-example.md
`-- scripts/
    `-- example_helper.py
```

## Suggested default output

```markdown
# [Process or Problem Name]

## 1. Goal and success metric
## 2. System boundary and assumptions
## 3. Actors, tools, inputs, and outputs
## 4. Workflow map
## 5. Decision points
## 6. Agent flow
## 7. Risks, bottlenecks, and mitigations
## 8. Suggested next steps
```

## Safety notes

The skill is for analysis, design, and planning. It should not execute workflows, contact people, scrape data, update systems, or make high-stakes determinations without explicit authorization, safe tooling, and human review where appropriate.
