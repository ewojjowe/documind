# DocuMind PH

Ask questions about Philippine tax, labor and business rules (BIR, DOLE, DTI) and get
answers with clickable citations to the exact source passage.

Informational only, not legal advice. The full project plan is in [Docs.md](Docs.md).

## Prerequisites

- Docker with Docker Compose
- [uv](https://docs.astral.sh/uv/) (installs Python 3.12 for the API)
- Node.js 22.18+ or 24.12+
- Go 1.26+

## Database

Start Postgres with pgvector from the repo root:

```bash
docker compose up -d
```

Stop it with `docker compose down` (data stays in the `pgdata` volume).

## API (`api/`)

FastAPI on Python 3.12. Run these from `api/`.

Install dependencies:

```bash
uv sync
```

Create `api/.env` with the app's own keys (never commit it):

```
DOCUMIND_ANTHROPIC_KEY=...
VOYAGE_API_KEY=...
```

Start the dev server with auto-reload:

```bash
uv run uvicorn app.main:app --reload
```

Check it at <http://localhost:8000/api/health>; interactive docs are at <http://localhost:8000/docs>.

Run tests and lint:

```bash
uv run pytest
```

```bash
uv run ruff check
```

## Web (`web/`)

Vue 3 + Vite + TypeScript. Run these from `web/`.

Install dependencies:

```bash
npm install
```

Start the dev server with hot reload (proxies `/api` to the API on port 8000):

```bash
npm run dev
```

Open <http://localhost:5173>.

Type-check and build for production into `web/dist/`:

```bash
npm run build
```

Rebuild `web/dist/` and re-run the type check on every file change:

```bash
npm run build:watch
```

Run unit tests (`-- --run` runs once instead of watching):

```bash
npm run test:unit -- --run
```

## MCP server (`mcp/`)

Go server that will let MCP clients (Claude Desktop, Claude Code) search the corpus.
It is a placeholder until Phase 4; after that it needs the API running and reads
`DOCUMIND_API` (default `http://localhost:8000`). Run these from `mcp/`.

Run it:

```bash
go run .
```

Build a binary:

```bash
go build -o documind-mcp .
```

Run tests:

```bash
go test ./...
```
