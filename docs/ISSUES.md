# Issues

## 2026-10-05: dependency sync could not reach PyPI in the sandbox

- **What I saw:** `uv sync` failed while fetching `https://pypi.org/simple/hatchling/` with `No such host is known`.
- **What was actually wrong:** the restricted execution environment had no DNS/network access for PyPI; the buyer logic had not run yet.
- **How I found it:** the resolver named the failed build dependency and URL directly.
- **What I changed:** kept all work in recorded mode, ran the repository key scanner independently, and deferred execution until the locked dependencies could be installed.
- **What it cost:** time only; no key was loaded, no transaction was prepared, signed, or submitted.
- **Would the checks have caught it?** This happens before the seven purchase checks. The fail-closed runner cannot sign because it cannot start.

## 2026-10-05: a protected GitHub email blocked a push

- **What I saw:** GitHub returned `GH007: Your push would publish a private email address`.
- **What was actually wrong:** the local commit identity used the account email rather than the GitHub noreply address.
- **How I found it:** `git log --format` showed the author and committer emails.
- **What I changed:** configured the repository to use the GitHub noreply identity before committing.
- **What it cost:** no transaction or funds; one rejected Git push.
- **Would the checks have caught it?** No purchase field applies; this is repository delivery metadata.
