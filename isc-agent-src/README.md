# isc-agent (vendored third-party source)

**This directory is not part of terrapot's own codebase.**

These files are an unmodified copy of the `isc_agent` source from the DShield
Sensor project, maintained by the SANS Internet Storm Center.

| | |
|---|---|
| **Upstream** | https://github.com/DShield-ISC/dshield |
| **Upstream path** | `srv/web/isc_agent/` |
| **Commit** | `3b3ce095f5193faa39b7622cd23d2d05c30ff092` |
| **License** | GPL-2.0 — see [`LICENSE`](./LICENSE) in this directory |
| **Modifications** | None |

Full provenance, checksums, and licensing rationale are in
[`NOTICE.md`](../NOTICE.md) at the repository root.

## Verifying these files are unmodified

From the repository root:

```
sha256sum isc-agent-src/*.py
```

Compare the output against the checksums recorded in `NOTICE.md`.

## A note for anyone modifying this project

**Do not edit these files in place.** They are deliberately kept byte-identical
to upstream, which is what allows this project to redistribute them under
GPL-2.0 section 1 rather than section 2, and what keeps the rest of the
repository outside GPL-2.0's scope as an aggregate work.

If you need different behavior from the web honeypot, build it as a separate
process in front of this one — a proxy or wrapper living outside this directory.
