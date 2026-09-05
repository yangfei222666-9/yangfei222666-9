# Yang Fei (Xiaojiu)

**Agent Reliability · Evals · Developer Tools**

I build deterministic checks and test cases for a narrow problem in AI-agent workflows: when an agent says `done`, `ready`, or `synced`, does the closeout include an explicit evidence pointer and state what remains unverified?

我关注 AI 工作流里的“假完成”：检查成功声明是否带显式证据指针和未验证边界，再把候选问题交给人沿着代码、命令和输出复核。

## Start here

| Path | What it shows | Current boundary |
| --- | --- | --- |
| **[memory-auditor](https://github.com/yangfei222666-9/memory-auditor)** | Zero-dependency Python CLI that flags evidence-free completion claims, overclaims, and duplicate rules | Findings are review candidates, not truth; current [v5 package](https://github.com/yangfei222666-9/memory-auditor/releases/tag/repro-v0-v5) is a prerelease and still needs independent human acceptance |
| **[Agent Reliability proof](https://github.com/yangfei222666-9/taiji/blob/main/docs/portfolio/agent-reliability-proof.md)** | False-pass gate, negative tests, scoped failure research, exact commands, and explicit `cannot_claim` boundaries | Public code and CI evidence do not establish production readiness, customer adoption, or hiring validation |
| **External engineering receipts** | A reviewed contribution merged into a third-party repository; a bug report referenced by a merged external fix; incident evidence cited by a community handbook | These are bounded public outcomes, not employer, vendor, or maintainer endorsements |

## Five-minute reproduction

```bash
git clone https://github.com/yangfei222666-9/memory-auditor.git
cd memory-auditor
python3 -B memory_auditor.py examples/sample-ledger.jsonl
```

On the current public `main`, the synthetic 10-line sample should produce four `no_evidence` candidates. The command reads the sample and does not modify it. A different result or unclear instruction is useful feedback; please retain the exact command, environment, exit code, and raw summary.

## External evidence

- **Reviewed and merged contribution:** [creativedswork/dsh-expmem PR #2](https://github.com/creativedswork/dsh-expmem/pull/2) was revised after repository review into an incremental audit-fixture contribution, approved, and merged. The narrow claim is contribution to an externally reviewed fixture and evidence contract, not authorship of ExpMem.
- **Issue-to-fix trace:** [tt-a1i/archify issue #76](https://github.com/tt-a1i/archify/issues/76) reported two renderer failures. The first failure was explicitly referenced and fixed by merged [PR #80](https://github.com/tt-a1i/archify/pull/80). I reported the two reproducible cases; I did not author the fix.
- **Community documentation reference:** evidence from [DeepSeek Harness discussion #4911](https://github.com/deepseek-ai/deepseek-harness/discussions/4911) was cited in the community handbook release `v0.5.265`. The handbook is an independent community project, not official DeepSeek documentation, and the reference is not an independent reproduction.
- **Community directory inclusion:** [dsh-voice-gate](https://github.com/yangfei222666-9/dsh-voice-gate) was accepted into an external DeepSeek Harness resource directory through merged [PR #406](https://github.com/0xsline/awesome-deepseek-harness/pull/406). Directory inclusion does not prove sustained users or production operation.

## What I work on

- Agent completion and evidence contracts
- Deterministic validators, negative tests, and failure injection
- CLI and GitHub Actions workflows
- Incident reproduction, source tracing, and bounded technical reports
- Human approval boundaries, provider isolation, and reviewer-readable evidence
- Chinese technical governance writing and bilingual engineering handoffs

Supporting projects:

- [dsh-voice-gate](https://github.com/yangfei222666-9/dsh-voice-gate) — a text-in / reply-out integration for DeepSeek Harness
- [dsh-skill-multi-model-review](https://github.com/yangfei222666-9/dsh-skill-multi-model-review) — multi-model candidate review with explicit non-authority boundaries
- [xiaojiu-ops-brain](https://github.com/yangfei222666-9/xiaojiu-ops-brain) — a public, curated subset of a file-backed memory and operating-rules system

## Feedback and collaboration

I am currently looking for:

1. independent reproduction feedback on `memory-auditor`;
2. small open-source workflows willing to test a false-pass check in shadow mode;
3. concrete counterexamples where an agent's completion claim and its evidence disagree.

Please open an issue with sanitized input, the exact command, expected versus actual behavior, and the first point of failure:

[memory-auditor issues](https://github.com/yangfei222666-9/memory-auditor/issues) · [taiji issues](https://github.com/yangfei222666-9/taiji/issues) · [dsh-voice-gate issues](https://github.com/yangfei222666-9/dsh-voice-gate/issues)

## Boundaries

- AI tools assist research, implementation, testing, translation, and review; I own the goals, acceptance criteria, stop conditions, and final claims.
- Public code, passing tests, CI, releases, downloads, and community replies are separate evidence types. None alone proves adoption or production readiness.
- I do not claim official OpenAI or DeepSeek affiliation, independent human validation, customer adoption, or an industry standard unless a named external receipt establishes it.
