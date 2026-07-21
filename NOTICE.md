# NOTICE

terrapot incorporates and interoperates with third-party open-source software.
This file records what those components are, where they came from, and under what
terms they are used.

The license for this project as a whole is in `LICENSE` at the repository root.
That license does not apply to the third-party components listed below, each of
which retains its own.

---

## DShield-ISC — `isc-agent` (vendored, unmodified)

| | |
|---|---|
| **Location in this repository** | `isc-agent-src/` |
| **Upstream project** | DShield Sensor — SANS Internet Storm Center |
| **Upstream repository** | https://github.com/DShield-ISC/dshield |
| **Upstream path** | `srv/web/isc_agent/` |
| **Upstream commit** | `3b3ce095f5193faa39b7622cd23d2d05c30ff092` (2026-06-18) |
| **Date copied into this repository** | 2026-07-08 |
| **License** | GNU General Public License, version 2 |
| **License text** | `isc-agent-src/LICENSE` |
| **Modifications** | None — copied verbatim |

These five files are unmodified copies of their upstream counterparts. That claim
is verifiable rather than asserted. SHA-256 checksums as vendored:

```
af40c30987cfdc80819bfbddc473613187efb9087d8e2aab92ba883830caf85c  __main__.py
c0db361dc97fd320bdb6ad4ab210c2573b8b76bdf3cff51aa9245400c52eedf2  agent.py
44702905997ab9a9220bcf039302694ba03c1330cb451af173cb4ab02e3a6b71  core.py
90fbee79c8d9a6d53b16327c2ffc3f89ff098759978e2e840a0623f90ed7f742  ncat_manager.py
60d4d2c64338bc75703c70a57588064ddc8d336f0ee60aea54dbf6b0cbdcde7e  stunnel_manager.py
```

To confirm, from the repository root:

```
sha256sum isc-agent-src/*.py
```

Because these files are unmodified, GPL-2.0 section 2 (modified works) does not
apply. They are redistributed under section 1, which requires that the copyright
notice, warranty disclaimer, and license text accompany them — satisfied by
`isc-agent-src/LICENSE` together with this notice.

`isc-agent` runs as a separate process in its own container. No code in this
project imports, links against, or derives from it; interaction is limited to a
configuration file written at container start and HTTP over a published port.
The remainder of this repository is an aggregate work in the sense of GPL-2.0
section 2, and is not governed by GPL-2.0.

**With thanks to** Johannes Ullrich and the SANS Internet Storm Center for the
DShield sensor and the threat-intelligence platform behind it.

---

## Cowrie — SSH/Telnet honeypot (partly vendored, modified)

| | |
|---|---|
| **Upstream project** | Cowrie |
| **Upstream repository** | https://github.com/cowrie/cowrie |
| **License** | BSD 3-Clause |
| **License text** | `cowrie-config/LICENSE` |
| **Copyright** | 2009–2024 Upi Tamminen; 2017–2024 Michel Oosterhof |

Cowrie itself is used as an official, unmodified Docker image (`cowrie/cowrie:latest`),
pulled at runtime and never redistributed by this project.

Two files under `cowrie-config/` are derived from Cowrie's shipped defaults and **are**
redistributed here:

| File in this repository | Derived from | Change |
|---|---|---|
| `cowrie-config/data/fs.pickle` | Cowrie's default `src/cowrie/data/fs.pickle` | One filesystem entry added: `/root/.aws/credentials`, with empty contents |
| `cowrie-config/etc/cowrie.cfg` | Cowrie's `src/cowrie/data/etc/cowrie.cfg.dist` | `filesystem = data/fs.pickle` uncommented and set |

The `fs.pickle` change was verified rather than assumed. Cowrie's default contains 28,966
filesystem entries; the copy in this repository contains 28,967, with the single added
entry being the decoy AWS credentials path used by this project's canary mechanism. That
file is a template only — it defines the path but holds no credentials. Real canary
credentials are injected at boot time by `inject_canary.py` and are never committed.

Cowrie's license text in `cowrie-config/LICENSE` was taken from upstream commit
`65ded95b2d2b6555be8e4eb95315036a4db361f9`.

BSD 3-Clause is permissive. It requires that the copyright notice, conditions, and
warranty disclaimer accompany redistributed source — satisfied by `cowrie-config/LICENSE`
together with this notice — and prohibits using the authors' names to promote this
project. It imposes no requirements on the rest of this repository, and no obligation to
document modifications.

**With thanks to** Michel Oosterhof and Cowrie's contributors, and to Upi Tamminen, whose
Kippo project Cowrie grew out of.

---

## Grafana Labs — Grafana, Loki, Promtail (referenced, not vendored)

| Component | Image | License |
|---|---|---|
| Grafana | `grafana/grafana:latest` | AGPL-3.0 |
| Loki | `grafana/loki:latest` | AGPL-3.0 |
| Promtail | `grafana/promtail:latest` | AGPL-3.0 |

All three are official upstream images, pulled at deploy time and run unmodified. No
Grafana Labs source or binaries are redistributed by this project.

Note that `grafana/grafana` is the Grafana **Open Source** image, not Grafana Enterprise
(`grafana/grafana-enterprise`). Grafana's own documentation confirms this, and further
notes that the separate `grafana/grafana-oss` repository stopped being updated as of
Grafana 12.4.0 in favor of `grafana/grafana`.

The AGPL's network-interaction clause (section 13) applies to *modified* versions offered
to users over a network. This project modifies none of these programs. The dashboard JSON,
datasource definitions, and Loki/Promtail configuration files in this repository are
configuration consumed by those programs, not changes to them.

**With thanks to** Grafana Labs and the maintainers of Grafana, Loki, and Promtail.

---

## Also used, not redistributed

Terraform, Docker, nginx, Certbot, Checkov, and the GitHub Actions referenced in
`.github/workflows/` are used as tools or pulled as published images. No source or
binaries from any of them are included in this repository.

Thinkst Canary / canarytokens.org is credited for the canary token mechanism and the
hosted token service. No Thinkst code is included here; operators supply their own
generated token.
