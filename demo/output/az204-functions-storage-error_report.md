# Exported Lab Rescue Agent Report

Lab Rescue Agent Demo Report
=============================
Scenario: az204-functions-storage-error
Certification: AZ-204
Role: Cloud Developer

Agent 1: Lab Triage Agent
- Confidence: high
- Diagnosis: Failure pattern matches a configuration issue: Missing AzureWebJobsStorage application setting

Evidence reviewed:
- Deployment completed with warnings
- Function host started but HTTP trigger did not become available
- Error: AzureWebJobsStorage is missing or empty
- Host initialization failed because storage connection could not be resolved

Mapped skill areas:
- Azure Functions
- Application settings
- Storage account configuration
- Deployment verification

Citations:
- engineering_certification_guide.md
- azure_functions_lab_recovery.md

Agent 2: Recovery Planner Agent
- Summary: Recovery plan targets the confirmed lab failure: Missing AzureWebJobsStorage application setting

Fix steps:
- Confirm the Function App belongs to the synthetic lab scenario.
- Inspect current application settings before changing configuration.
- Add or repair the AzureWebJobsStorage setting using synthetic lab storage values only.
- Restart the Function App after the setting is corrected.

Rollback steps:
- Record the previous app setting value before applying changes.
- Restore the previous value if the host still fails to start.
- Restart the Function App again after rollback.

Verification steps:
- Confirm the function host starts without storage configuration errors.
- Confirm the HTTP trigger endpoint responds.
- Confirm deployment logs no longer mention missing AzureWebJobsStorage.

Safety notes:
- Use synthetic lab data only
- Do not expose real connection strings
- Use placeholder-free environment examples in documentation

Recovery citations:
- engineering_certification_guide.md
- azure_functions_lab_recovery.md

Agent 3: Learning Path Agent
- Certification: AZ-204
- Role: Cloud Developer
- Readiness impact: This failure raises readiness risk until the learner can recover the lab and explain the configuration dependency.

Study focus:
- Azure Functions practice and recovery review
- Application settings practice and recovery review
- Storage account configuration practice and recovery review
- Deployment verification practice and recovery review

Recommended learner actions:
- Repeat the failed lab after applying the recovery plan.
- Write a short explanation of root cause, fix, rollback, and verification.
- Complete a focused practice check on Azure Functions configuration.
- Review approved synthetic knowledge sources before the next lab attempt.

Learning citations:
- engineering_certification_guide.md
- azure_functions_lab_recovery.md

Agent 4: Study Plan Agent
- Summary: Create a capacity-aware AZ-204 recovery plan for Cloud Developer using 4 focused hours per week.
- Weekly study hours: 4
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
- High meeting load detected; use short protected focus blocks instead of long study sessions.
- Limited study capacity; prioritize recovery verification before broad topic review.

Study plan citations:
- engineering_certification_guide.md
- azure_functions_lab_recovery.md
- team_learning_signals.json

Agent 5: Assessment Agent
- Readiness target: AZ-204 grounded practice readiness
- Scoring guidance: Pass when the learner explains root cause, fix, rollback, verification, and safety constraints.

Grounded practice questions:
- Q1: What setting is commonly required for an Azure Functions host to start storage-backed runtime services?
  Expected: AzureWebJobsStorage must be present and valid for the synthetic lab Function App.
  Skill: Application settings
  Citation: azure_functions_lab_recovery.md
- Q2: What should the learner verify after repairing the Function App setting?
  Expected: The host starts without storage errors and the HTTP trigger responds.
  Skill: Deployment verification
  Citation: azure_functions_lab_recovery.md
- Q3: Why should connection strings not be printed or committed during recovery?
  Expected: They are secrets and must not appear in logs or source control.
  Skill: Security hygiene
  Citation: engineering_certification_guide.md

Assessment citations:
- engineering_certification_guide.md
- azure_functions_lab_recovery.md

Agent 6: Manager Insights Agent
- Team ID: TEAM-A
- Summary: TEAM-A shows readiness risk around AZ-204 because this failed lab maps to: Azure Functions, Application settings, Storage account configuration, Deployment verification.

Readiness signals:
- Synthetic team size reviewed: 3
- Learners below 75 percent practice readiness: 2
- Learners with failed or review lab outcomes: 2
- Current learner study capacity: 4 hours per week
- Assessment target: AZ-204 grounded practice readiness

Risk areas:
- Azure Functions configuration recovery
- Application setting verification before code changes
- Rollback discipline after failed recovery attempts
- Grounded explanation of root cause and verification evidence

Recommended manager actions:
- Protect short focus blocks for learners with high meeting load.
- Assign a targeted recovery practice session for AZ-204.
- Review whether learners can explain root cause, fix, rollback, and verification steps.
- Use aggregate readiness signals only; do not expose private learner details in manager summaries.

Privacy notes:
- Uses synthetic learner and employee identifiers only.
- Summarizes aggregate readiness signals instead of exposing sensitive personal data.
- Does not use real employee records, customer data, credentials, or private logs.

Manager citations:
- engineering_certification_guide.md
- azure_functions_lab_recovery.md
- team_learning_signals.json

Grounded sources loaded:
- engineering_certification_guide.md: 1406 characters
- azure_functions_lab_recovery.md: 1493 characters

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
- azure_functions_lab_recovery.md
- team_learning_signals.json

Workflow status:
- Seven-agent enterprise readiness demo completed with safety verification.
