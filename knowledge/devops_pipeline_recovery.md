# DevOps Pipeline Recovery Guide Synthetic

Source type: approved synthetic lab recovery guide
Certification: AZ-400
Skill areas: CI/CD release gates, environment approvals, deployment governance, release verification

## Recovery pattern: environment approval blocks deployment

When a CI/CD pipeline build succeeds but deployment remains pending, inspect environment approvals and gates before changing pipeline logic.

Common evidence:
- Build completes successfully
- Deployment job is created
- Release remains pending before the target environment
- Logs mention approval or gate requirements

Likely cause:
- The target environment requires approval before deployment can continue

Safe recovery steps:
1. Confirm the pipeline and environment are intended synthetic lab resources.
2. Inspect the current environment approval configuration.
3. Add or request the required synthetic approver.
4. Resume or re-run the deployment after approval is granted.
5. Verify the gated stage completes successfully.

Rollback steps:
1. Record the previous approval configuration before changing it.
2. Restore the previous configuration if deployment behavior is unexpected.
3. Cancel the pending synthetic deployment if approval configuration remains incorrect.

Verification checks:
- Pipeline waits at the expected approval gate
- Approval allows the deployment to continue
- Deployment logs show successful completion of the gated stage

Safety notes:
- Do not bypass real production approvals
- Do not expose real environment names
- Use synthetic pipeline identifiers only for demos
