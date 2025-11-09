# Repository Summary - forge-vhdl v3.1.0

## Git History Status

✅ **History rewritten successfully**
- Single clean initial commit with all production files
- 2 additional commits for web-worker onboarding documentation
- No development artifacts in main history
- All stale files archived or removed

```
b9cc02d docs: Add quick-start web worker prompt (copy-paste format)
6d2df8d docs: Add web-worker onboarding prompt
20cd1b0 Initial commit: forge-vhdl VHDL framework v3.1.0
```

## Repository Structure

```
forge-vhdl/
├── llms.txt                           # LLM quick reference (~800 tokens)
├── CLAUDE.md                          # Main design guide (~3.5k tokens)
├── README.md                          # Entry point
├── QUICK_START_WEB_WORKER.txt        # Copy-paste onboarding prompt ⭐
├── WEB_WORKER_ONBOARDING.md          # Detailed onboarding guide ⭐
│
├── vhdl/                              # VHDL components
│   ├── packages/                      # Voltage types, serialization, common
│   └── components/                    # Utilities, debugging, loaders
│
├── cocotb_tests/                      # VHDL simulation tests (CocoTB + GHDL)
│   ├── components/                    # Per-component test suites
│   └── run.py                         # Test runner with progressive levels
│
├── scripts/
│   ├── cloud_setup_with_ghdl.py      # One-command cloud setup ⭐
│   ├── setup.sh                       # Local development setup
│   └── validate_setup.sh              # Environment validation
│
├── workflow/                          # AI-assisted development workflow
│   ├── specs/pending/                 # Example component specifications
│   ├── artifacts/                     # Generated VHDL + tests staging area
│   └── prompts/                       # Agent workflow prompts
│
├── .claude/                           # AI agent definitions
│   ├── agents/                        # 4-agent workflow (generate → design → test)
│   └── commands/gather-requirements.md # Interactive requirements Q&A
│
└── docs/
    ├── CLOUD_SETUP_PROMPT.md         # Cloud deployment guide
    ├── COCOTB_TROUBLESHOOTING.md     # Test debugging
    ├── VHDL_CODING_STANDARDS.md      # Coding standards
    └── archive/                       # Archived development artifacts
```

## Web Worker Quick Start

**For Claude Code Web users:**

1. **Copy-paste this file:** `QUICK_START_WEB_WORKER.txt`
2. **Or read detailed guide:** `WEB_WORKER_ONBOARDING.md`

The prompt will:
- ✅ Verify environment setup (GHDL, Python, UV)
- ✅ Run pre-existing VHDL tests (forge_util_clk_divider, voltage packages)
- ✅ Test requirements gathering workflow (/gather-requirements)
- ✅ Create git commits documenting progress (2 phases: setup → tests)

**Expected results:**
- Phase 1: Environment setup completes in ~2-3 minutes
- Phase 2: 3-4 P1 tests pass with <60 lines total output
- Phase 3: Requirements gathering creates spec file

## Key Features

### Cloud-First Development
- One-command setup: `uv run python scripts/cloud_setup_with_ghdl.py`
- Works in: Claude Code Web, GitHub Codespaces, containers
- No local VHDL toolchain required

### Progressive Testing
- **P1 (Basic):** <20 line output, <5 sec runtime, LLM-optimized
- **P2 (Intermediate):** <50 lines, comprehensive validation
- **P3 (Comprehensive):** Full coverage
- GHDL output filtering: 98% noise reduction

### AI Agent Toolkit
- `/gather-requirements` - Interactive specification gathering
- `forge-vhdl-component-generator` - VHDL code generation
- `cocotb-progressive-test-designer` - Test architecture design
- `cocotb-progressive-test-runner` - Test implementation

### Voltage Type System
- `forge_voltage_3v3_pkg` - 0-3.3V (TTL, GPIO)
- `forge_voltage_5v0_pkg` - 0-5.0V (sensors, unipolar)
- `forge_voltage_5v_bipolar_pkg` - ±5.0V (Moku DAC/ADC)

## Testing Quick Reference

```bash
# List all tests
uv run python cocotb_tests/run.py --list

# Run P1 test (default, LLM-optimized)
uv run python cocotb_tests/run.py forge_util_clk_divider

# Run P2 test (comprehensive)
TEST_LEVEL=P2_INTERMEDIATE uv run python cocotb_tests/run.py forge_util_clk_divider

# Run all P1 tests
uv run python cocotb_tests/run.py --all
```

## Cleanup Summary

**Files removed:** 25 (test logs, diagnostic reports, debugging artifacts)
**Files archived:** 7 (development prompts → `docs/archive/development_prompts/`)
**Documentation fixed:** 3 broken references corrected
**Result:** Clean template repository ready for web-workers

See: `docs/archive/CLEANUP_2025-11-08.md` for complete cleanup details

## Next Steps

1. **Onboard web worker:** Use `QUICK_START_WEB_WORKER.txt`
2. **Validate environment:** Run cloud setup + tests
3. **Try example workflow:** `workflow/specs/pending/edge_detector.md`
4. **Create new component:** Use `/gather-requirements` slash command
5. **Run automated workflow:** 4-agent pipeline (generate → design → test)

## Documentation Hierarchy

**Tier 1 (Always Load):** `llms.txt` - Quick reference, ~800 tokens
**Tier 2 (Primary Reference):** `CLAUDE.md` - Complete guide, ~3.5k tokens
**Tier 3 (On-Demand):** `docs/` - Specialized troubleshooting, standards

## Status

- **Version:** 3.1.0
- **License:** MIT
- **Repository:** https://github.com/vmars-20/forge-vhdl-3v3-vmars
- **History:** Clean (rewritten 2025-11-08)
- **Ready for:** Web-worker onboarding, template usage

---

**Last Updated:** 2025-11-08
**Maintainer:** Moku Instrument Forge Team
