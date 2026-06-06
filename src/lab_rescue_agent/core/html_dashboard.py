"""Static HTML dashboard export for Lab Rescue Agent."""

from __future__ import annotations

from html import escape
from pathlib import Path


def html_list(items: list[str]) -> str:
    if not items:
        return "<li>none</li>"
    return "\n".join(f"<li>{escape(str(item))}</li>" for item in items)


def build_dashboard_html(report: str, summary: dict, foundry_status: str) -> str:
    scenario_id = escape(str(summary.get("scenario_id", "")))
    certification = escape(str(summary.get("certification", "")))
    role = escape(str(summary.get("role", "")))
    safety_status = escape(str(summary.get("safety_status", "")))
    workflow = [str(item) for item in summary.get("workflow", [])]

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Lab Rescue Agent Dashboard - {scenario_id}</title>
  <style>
    body {{
      margin: 0;
      font-family: Arial, sans-serif;
      background: #0b1020;
      color: #eef2ff;
    }}
    header {{
      padding: 32px;
      background: linear-gradient(135deg, #1d4ed8, #7c3aed, #db2777);
    }}
    main {{
      padding: 28px;
      max-width: 1180px;
      margin: auto;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin: 20px 0;
    }}
    .card {{
      background: #111827;
      border: 1px solid #334155;
      border-radius: 14px;
      padding: 18px;
      box-shadow: 0 12px 30px rgba(0,0,0,.25);
    }}
    .pass {{
      color: #22c55e;
      font-weight: 800;
      letter-spacing: .08em;
    }}
    .chip {{
      display: inline-block;
      padding: 6px 10px;
      border-radius: 999px;
      background: #1e293b;
      border: 1px solid #475569;
      margin: 4px 4px 4px 0;
      font-size: 13px;
    }}
    pre {{
      white-space: pre-wrap;
      background: #020617;
      color: #dbeafe;
      border: 1px solid #334155;
      border-radius: 14px;
      padding: 18px;
      overflow-x: auto;
    }}
    h1, h2 {{
      margin-top: 0;
    }}
    .muted {{
      color: #cbd5e1;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Lab Rescue Agent</h1>
    <p>Seven-agent certification lab recovery dashboard</p>
  </header>
  <main>
    <section class="grid">
      <div class="card">
        <h2>Scenario</h2>
        <p>{scenario_id}</p>
      </div>
      <div class="card">
        <h2>Certification</h2>
        <p>{certification}</p>
      </div>
      <div class="card">
        <h2>Role</h2>
        <p>{role}</p>
      </div>
      <div class="card">
        <h2>Safety Status</h2>
        <p class="pass">{safety_status.upper()}</p>
      </div>
    </section>

    <section class="card">
      <h2>Agent Workflow</h2>
      <ol>
        {html_list(workflow)}
      </ol>
    </section>

    <section class="card">
      <h2>Foundry Readiness</h2>
      <pre>{escape(foundry_status)}</pre>
    </section>

    <section class="card">
      <h2>Full Safety-Verified Report</h2>
      <pre>{escape(report)}</pre>
    </section>

    <p class="muted">Synthetic demo data only. No real employee data, customer data, credentials, connection strings, tokens, or private logs.</p>
  </main>
</body>
</html>
"""


def write_dashboard(path: Path, report: str, summary: dict, foundry_status: str) -> Path:
    path.write_text(build_dashboard_html(report, summary, foundry_status), encoding="utf-8")
    return path
