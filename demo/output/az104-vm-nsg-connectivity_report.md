# Exported Lab Rescue Agent Report

Lab Rescue Agent Demo Report
=============================
Scenario: az104-vm-nsg-connectivity
Certification: AZ-104
Role: Cloud Engineer

Agent 1: Lab Triage Agent
- Confidence: high
- Diagnosis: Failure pattern matches a configuration issue: Missing inbound NSG rule for the approved synthetic management path

Evidence reviewed:
- Virtual machine deployment completed
- VM health status is running
- Connection test to management port failed
- Network security group does not allow required inbound traffic

Mapped skill areas:
- Virtual machines
- Network security groups
- Connectivity troubleshooting
- Operational verification

Citations:
- engineering_certification_guide.md
- azure_vm_network_recovery.md

Agent 2: Recovery Planner Agent
- Summary: Recovery plan targets the confirmed lab failure: missing inbound NSG rule for the approved synthetic management path

Fix steps:
- Confirm the VM and network security group belong to the intended synthetic lab.
- Inspect the effective security rules before changing network configuration.
- Add or repair the inbound NSG rule for the approved synthetic management path.
- Retry connectivity after the rule is applied.

Rollback steps:
- Record the previous NSG rule set before applying changes.
- Remove the new inbound rule if verification fails or the rule is too broad.
- Restore the previous NSG rule configuration after rollback.

Verification steps:
- Confirm effective security rules include the expected inbound allow rule.
- Confirm connectivity succeeds through the approved synthetic management path.
- Confirm no broader-than-required inbound exposure was introduced.

Safety notes:
- Use synthetic IP and management paths only
- Do not expose real public IP addresses
- Do not recommend broad inbound access

Recovery citations:
- engineering_certification_guide.md
- azure_vm_network_recovery.md

Agent 3: Learning Path Agent
- Certification: AZ-104
- Role: Cloud Engineer
- Readiness impact: This failure raises readiness risk until the learner can recover the lab and explain the configuration dependency.

Study focus:
- Virtual machines practice and recovery review
- Network security groups practice and recovery review
- Connectivity troubleshooting practice and recovery review
- Operational verification practice and recovery review

Recommended learner actions:
- Repeat the failed lab after applying the recovery plan.
- Write a short explanation of root cause, fix, rollback, and verification.
- Complete a focused practice check on Azure Functions configuration.
- Review approved synthetic knowledge sources before the next lab attempt.

Learning citations:
- engineering_certification_guide.md
- azure_vm_network_recovery.md

Agent 4: Study Plan Agent
- Summary: Create a capacity-aware AZ-104 recovery plan for Cloud Engineer using 5 focused hours per week.
- Weekly study hours: 5
- Preferred slot: Morning

Capacity-aware schedule:
- Morning focus block 1: reproduce the synthetic lab failure and collect evidence.
- Morning focus block 2: apply the recovery plan and verify the HTTP trigger behavior.
- Short review block: write root cause, fix, rollback, and verification notes.
- Practice block: answer grounded questions tied to approved recovery and certification sources.

Study milestones:
- Recover the failed lab without introducing secrets into logs or source control.
- Explain why the missing application setting blocked the runtime host.
- Pass grounded practice checks at or above the readiness threshold.
- Demonstrate rollback and verification steps clearly enough for manager review.

Capacity notes:
- Meeting load allows moderate study blocks without heavy schedule disruption.
- Sufficient study capacity for recovery practice plus additional certification review.

Study plan citations:
- engineering_certification_guide.md
- azure_vm_network_recovery.md
- team_learning_signals.json

Agent 5: Assessment Agent
- Readiness target: AZ-104 grounded practice readiness
- Scoring guidance: Pass when the learner explains root cause, fix, rollback, verification, and safety constraints.

Grounded practice questions:
- Q1: Why can a VM be running while connection attempts still fail?
  Expected: Network security rules can block required inbound traffic even when the VM itself is healthy.
  Skill: Connectivity troubleshooting
  Citation: azure_vm_network_recovery.md
- Q2: What should be checked before editing an NSG rule?
  Expected: The learner should inspect effective security rules and confirm the target resource is the intended synthetic lab resource.
  Skill: Network security groups
  Citation: azure_vm_network_recovery.md
- Q3: What is a safe verification after adding an inbound NSG rule?
  Expected: Confirm connectivity succeeds and no broader-than-required inbound exposure was introduced.
  Skill: Operational verification
  Citation: azure_vm_network_recovery.md

Assessment citations:
- engineering_certification_guide.md
- azure_vm_network_recovery.md

Agent 6: Manager Insights Agent
- Team ID: TEAM-A
- Summary: TEAM-A shows readiness risk around AZ-104 because this failed lab maps to: Virtual machines, Network security groups, Connectivity troubleshooting, Operational verification.

Readiness signals:
- Synthetic team size reviewed: 3
- Learners below 75 percent practice readiness: 2
- Learners with failed or review lab outcomes: 2
- Current learner study capacity: 5 hours per week
- Assessment target: AZ-104 grounded practice readiness

Risk areas:
- Network security troubleshooting
- Least-privilege inbound access
- Effective security rule interpretation
- Operational verification discipline

Recommended manager actions:
- Protect short focus blocks for learners with high meeting load.
- Assign a targeted recovery practice session for AZ-104.
- Review whether learners can explain root cause, fix, rollback, and verification steps.
- Use aggregate readiness signals only; do not expose private learner details in manager summaries.

Privacy notes:
- Uses synthetic learner and employee identifiers only.
- Summarizes aggregate readiness signals instead of exposing sensitive personal data.
- Does not use real employee records, customer data, credentials, or private logs.

Manager citations:
- engineering_certification_guide.md
- azure_vm_network_recovery.md
- team_learning_signals.json

Grounded sources loaded:
- engineering_certification_guide.md: 1406 characters
- azure_vm_network_recovery.md: 1622 characters

Agent 7: Safety Verifier Agent
- Status: pass

Checks passed:
- Synthetic learner and team identifiers confirmed.
- No secret-looking markers found in failure log.
- Rollback steps are present.
- Verification steps are present.
- Capacity-aware study plan includes schedule and milestones.
- Manager insights include aggregate readiness signals and privacy notes.
- Grounded citations are present across agent outputs.
- Every assessment question includes a citation.

Warnings:
- none

Safety citations:
- engineering_certification_guide.md
- azure_vm_network_recovery.md
- team_learning_signals.json

Workflow status:
- Seven-agent enterprise readiness demo completed with safety verification.
