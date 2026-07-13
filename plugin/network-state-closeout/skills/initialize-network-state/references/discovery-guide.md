# Consent-based network discovery

Read this file only after the user has agreed to local read-only discovery during initialization.

## What may be saved

Save confirmed structural facts only in the active private skill:

- Device aliases, roles, platforms, trust zones, availability and LAN/public/overlay addresses.
- Subnets, routes, DNS relationships, gateways, VLANs and stable network boundaries.
- SSH host aliases, target hosts, users, ports, `ProxyJump` relationships and identity-file paths.
- Docker contexts, hosts, networks, container or service names, published ports and stable dependencies.
- Nginx, Caddy or Traefik listeners, domains, upstreams, TLS state and certificate paths.
- Tailscale, WireGuard, ZeroTier or other virtual-network device aliases, addresses, advertised routes and access direction.
- VPS or cloud provider, region, role, hostname, addresses, exposed services and access path.
- Verification time, method and a short redacted signal.

These facts are private. Keep them in `~/.codex/skills/private-network-state` and its confirmed GitHub private repository only; do not copy the full inventory into the public plugin or unrelated project documents.

## What must never be saved

Never save or stage passwords, passphrases, private-key contents, VPN private or preshared keys, tokens, API keys, cookies, sessions, recovery codes, one-time codes, subscription URLs, credential-bearing URLs, complete environment files, Docker secrets, cloud credentials or raw password-manager/keychain output.

Keep only a safe reference such as an identity-file path, keychain item name, password-manager entry name, environment-variable name or secret-manager alias. Do not preserve the value in notes, temporary files, command output captures, diffs or Git history.

## Local read-only directions

Select commands for the current operating system and installed tools. Prefer narrow formatted output over full dumps.

| Direction | Look for | Avoid |
|---|---|---|
| Host network | Interfaces, addresses, routes, gateways, DNS and listening ports | Packet capture, active probing or saved raw dumps |
| SSH | `Host`, `HostName`, `User`, `Port`, `ProxyJump`, `IdentityFile` path | Reading private keys, agents, passphrases or copying whole configs |
| Docker | `docker ps --format`, network names, IPAM subnets, published ports, compose service names | Full `docker inspect`, environment values, secret mounts or full rendered Compose config |
| Reverse proxy | `listen`, `server_name`, upstreams, `proxy_pass`, TLS state and certificate paths | Authentication headers, embedded credentials, private-key contents or full config copies |
| Virtual network | Device aliases, overlay addresses, routes, peers by safe alias and reachability | Auth keys, WireGuard `showconf`, private/preshared keys or raw identity exports |
| VPS and cloud | Locally known aliases, provider, region, role, addresses, domains and access paths | Cloud credential files, provider API calls or remote login without separate consent |

Useful local sources may include interface and route commands, current DNS configuration, selected fields from `~/.ssh/config`, safe Docker list/format commands, reverse-proxy configuration directives, and status commands from installed virtual-network clients. Do not install tools solely for discovery.

## Expanded scope requires new consent

Ask separately before:

- Scanning a LAN, subnet, port range or neighboring devices.
- Logging in to any remote host; use SSH first when authorized.
- Querying a router, NAS, VPS control panel or cloud-provider API.
- Reading configuration owned by another user or requiring elevated privileges.

State exactly which hosts, ranges, commands or services the added permission covers.

## Write and verify

1. Extract only useful fields in memory; do not save raw command output.
2. Discard any encountered secret without quoting it back to the user.
3. Map devices to `references/devices.md`, services to `services.md`, directional access to `access-paths.md`, and stable boundaries to `topology.md`.
4. Use `unknown` for unconfirmed fields and ask only about high-value gaps.
5. Run `validate_profile.py`, inspect the exact candidate diff, and confirm that only approved structural facts are present before any commit.
6. Report collected categories and remaining gaps without repeating private endpoints in the final response.
