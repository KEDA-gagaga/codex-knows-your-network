---
name: initialize-network-state
description: Initialize or adopt a private global network-state skill in the active Codex skills cache, optionally discover the user's network structure after informed consent, or connect another device by cloning the same GitHub private repository into its .codex/skills directory. Use for first setup, consent-based SSH/Docker/reverse-proxy/overlay/VPS inventory, private GitHub onboarding, or another-device installation; not routine updates.
---

# Initialize Network State

Create or adopt one private global skill. Never inspect network configuration, run discovery commands, scan the network, or contact another host before obtaining the required consent.

## Core model

- The active directory under `.codex/skills` is the only editable local source.
- Cross-project use comes from Codex loading that global skill in different projects.
- Cross-device use comes from installing this plugin, then cloning the same GitHub private repository into the other device's `.codex/skills` cache.
- Project copies, Documents folders, and alternate clones are never daily working copies.
- GitHub private repositories are currently the only cross-device synchronization route described by this plugin.

## Choose one setup path

1. New private skill: initialize an absent or empty target.
2. Existing private skill: validate it without applying templates.
3. First synchronized device: create or adopt the skill, then connect an empty confirmed GitHub private repository.
4. Additional device: install the plugin and clone the confirmed private repository directly into the active target; do not initialize first.

Use the default target path unless the user provides another one. Ask only for a short profile name and scope when they are not already clear, and whether GitHub private synchronization is wanted. Only when synchronization is selected, determine whether this is the first or an additional device; ask only if the request and target do not make that clear.

## Active path

Resolve the target from an explicit path, `NETWORK_STATE_HOME`, or:

```text
~/.codex/skills/private-network-state
```

For a new skill, run:

```bash
python3 <network-state-skill-directory>/scripts/init_profile.py --path <private-skill-directory>
```

Update `profile.md` with the confirmed profile name and scope. Do not invent device or service facts.

## Offer consent-based discovery

After the private skill exists, explain what may and may not be saved, make the explicit privacy promise below, then ask whether the user wants local read-only discovery. On an additional device, clone and validate the existing private skill first; never initialize an empty target before cloning.

Promise in equivalent, unambiguous language:

> I will only save network-structure facts you authorize. I will never place passwords, passphrases, tokens, API keys, private-key contents, VPN private or preshared keys, cookies, recovery codes, one-time codes, subscription URLs, or credential-bearing URLs into the private skill, closeout cards, Git staging, commits, or the GitHub repository. If encountered, I will discard the value and keep only a safe reference name or path when useful.

If the user declines, keep the initialized cards empty and continue to validation. If the user agrees, read `references/discovery-guide.md`, inspect only the approved local read-only sources, ask only for important missing facts, and write confirmed structural facts directly into the matching cards.

Local discovery consent does not authorize active subnet scanning, provider API calls, or logging in to another host. Obtain separate explicit authorization for each expanded scope. Prefer SSH for an authorized remote inspection.

## GitHub private synchronization

When selected, read `references/github-private-sync.md` and follow its first-device or additional-device path. Repository creation, remote replacement, and destructive Git actions require explicit authorization. Routine validated commits and pushes do not require confirmation each time.

A local-only update remains available after synchronization is configured: update and locally commit the active cache without fetching or pushing. A later cross-device synchronization must run the complete gate again.

## Validate

```bash
python3 <network-state-skill-directory>/scripts/validate_profile.py --path <private-skill-directory>
```

On POSIX systems, prefer directory mode `0700` and file mode `0600`. Report the active path, created/adopted/cloned result, discovery consent and collected categories, GitHub synchronization status, and validation result without revealing endpoints or repository URLs.
