# Ship It: Deploy an App From Git to a Live URL

## The app

`app.py` — a minimal deployable app using only the Python standard library
(no dependencies, so no `requirements.txt` entries are needed for it to run).

- `GET /` → `{"message": "Hello from hello-api!"}`
- `GET /health` → `{"status": "ok"}`
- Listens on `$PORT` (defaults to 8000), bound to `0.0.0.0` so a host can reach it.

Verified locally on 2026-11-25: `Listening on port 8000`, `/` and `/health`
both returned the expected JSON, and an edit → commit → restart → reload
cycle showed the new greeting live.

## Status

Done for real on 2026-11-26: this app lives in the public GitHub repo
`hello-api`, and the GitHub Codespaces run below was carried out end to end —
the forwarded public URL served the greeting on `/` and
{"status": "ok"} on `/health`. The two paths below are kept as the
how-it-was-done record.

## Finish it for real — path A: GitHub Codespaces (fastest, GitHub only)

GitHub Free personal accounts include 120 Codespaces core-hours and 15 GB of
storage per month (GitHub Docs, checked 2026-11-25) — about 60 hours on a
2-core machine. No card needed.

1. Create a free account at github.com/signup (your own email, your own
   password — never share the password in chat).
2. Create a new public repository, e.g. `dewa-first-app`. Leave it empty
   (no README/license added by GitHub, to avoid a merge conflict).
3. Upload `app.py` (+ this README and `.gitignore`) via the web UI:
   repo page → Add file → Upload files. Or push from a terminal:
   `git remote add origin https://github.com/<you>/dewa-first-app.git`
   then `git push -u origin master` (this repo's branch is `master`).
4. On the repo page: Code → Codespaces → Create codespace on master.
5. In the codespace terminal: `python3 app.py`
6. Ports panel → port 8000 → right-click → Port Visibility → Public.
   Open the forwarded URL — that is your live public URL. It stays live
   while the codespace runs; stop/delete the codespace when done so it does
   not burn free hours.

## Finish it for real — path B: Render (a URL that stays up)

Render's free tier: 750 instance hours/month, no credit card required, public
`https://<service>.onrender.com` URL. Free services sleep after 15 minutes
without traffic and take ~1 minute to wake on the next visit.

1. Do steps 1–3 above (GitHub account + repo with `app.py`).
2. Create a free account at render.com (sign in with GitHub).
3. New → Web Service → pick the repo. Build command: leave empty
   (stdlib-only app, nothing to install). Start command: `python app.py`.
   Instance type: Free.
4. Create the service and open the `onrender.com` URL it assigns.
   `/health` should return `{"status": "ok"}`.

## Notes

- Do not commit `server.log` / `server.pid` — `.gitignore` already covers them.
- The Codespaces URL changes per codespace and only lives while it runs;
  the Render URL is stable but sleeps when idle. Pick A for the quick win,
  B for a link you can share.
