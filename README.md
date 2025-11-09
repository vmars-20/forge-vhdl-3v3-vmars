# forge-vhdl v3.2

**Cloud-first VHDL framework with AI-assisted workflows and progressive testing**

Reusable VHDL components (clock dividers, voltage utilities, FSM encoders) + CocoTB test infrastructure with 98% output reduction for LLM-friendly iteration. Batteries-included setup for Claude Code Web, GitHub Codespaces, and containers.

**Repository:** https://github.com/vmars-20/forge-vhdl-3v3-vmars

---

## 🤖 For AI Agents: Quick Start

**Read these files in order:**

1. **`llms.txt`** - Quick reference (~800 tokens): component catalog, testing commands, structure overview
2. **`CLAUDE.md`** - Complete guide (~3.5k tokens): testing standards, VHDL patterns, agent workflows, troubleshooting

**Then execute:**
```bash
# One-command setup (cloud environments)
uv run python scripts/cloud_setup_with_ghdl.py

# List available tests
uv run python cocotb_tests/run.py --list

# Run P1 tests (LLM-optimized, <20 lines output)
uv run python cocotb_tests/run.py forge_util_clk_divider
```

**Expected:** Setup in ~2-3 minutes, test output <20 lines, PASS result.

---

## 👤 For Humans: Web Worker Onboarding

**New to this repository? Start here:**

📋 **Copy-paste this file into Claude Code Web:** `QUICK_START_WEB_WORKER.txt`

The onboarding prompt will:
1. ✅ Verify environment setup (GHDL, Python, UV)
2. ✅ Run pre-existing tests (validates VHDL simulation works)
3. ✅ Test requirements gathering workflow (interactive component specification)
4. ✅ Create git commits documenting progress

**Alternative:** Read `WEB_WORKER_ONBOARDING.md` for detailed manual instructions.

---

## 🚀 Local Development

**For contributors with local GHDL installed:**

```bash
git clone https://github.com/vmars-20/forge-vhdl-3v3-vmars.git
cd forge-vhdl-3v2-claude
./scripts/setup.sh
./scripts/validate_setup.sh
```

---

## 🎯 What's Inside

### Progressive Testing Infrastructure
CocoTB + GHDL with 98% output reduction for LLM-friendly iteration:
- **P1 tests:** <20 lines output, <5 sec runtime, 3-5 essential tests
- **P2 tests:** <50 lines, comprehensive validation
- **P3 tests:** Full coverage with edge cases
- **GHDL filter:** Strips metavalue warnings, preserves errors/assertions

### VHDL Components
- **`forge_util_clk_divider`** - Programmable clock divider
- **`forge_hierarchical_encoder`** - FSM state encoder for oscilloscope debugging
- **`forge_voltage_*_pkg`** - Voltage domain utilities (3.3V, 5V, ±5V bipolar)
- **`forge_lut_pkg`** - Look-up table utilities
- **`forge_serialization_*_pkg`** - Register serialization (types, voltage, time)
- **`forge_common_pkg`** - FORGE_READY control scheme

### AI Agent Workflow
Four specialized agents for autonomous VHDL development:
1. **`/gather-requirements`** - Interactive component specification (slash command)
2. **`forge-vhdl-component-generator`** - VHDL-2008 code generation
3. **`cocotb-progressive-test-designer`** - Test architecture design
4. **`cocotb-progressive-test-runner`** - Test implementation + execution

**Usage:** `/gather-requirements` → automated 4-agent workflow → VHDL + tests

### Python Packages
- **`forge_cocotb/`** - Progressive testing framework, GHDL filter, test runner
- **`forge_platform/`** - Simulation/hardware backends (MCC, oscilloscope)
- **`forge_tools/`** - Hierarchical voltage decoder, utilities

---

## 📚 Documentation Hierarchy

**Tier 1 (Always Load):** `llms.txt` (~800 tokens)
- Component catalog, basic usage, file structure

**Tier 2 (Primary Reference):** `CLAUDE.md` (~3.5k tokens)
- Testing standards (AUTHORITATIVE)
- CocoTB progressive testing guide
- VHDL coding standards summary
- Agent workflow patterns

**Tier 3 (On-Demand):** `docs/` directory
- `CLOUD_SETUP_PROMPT.md` - Cloud deployment walkthrough
- `COCOTB_TROUBLESHOOTING.md` - Test debugging guide
- `VHDL_CODING_STANDARDS.md` - Complete style guide

**Workflows:** `workflow/` directory
- `specs/pending/` - Example component specifications (edge_detector, synchronizer, debouncer)
- `artifacts/` - Generated VHDL + tests staging area
- `prompts/` - Agent workflow prompts

---

## 🧪 Testing Examples

```bash
# List all available tests
uv run python cocotb_tests/run.py --list

# Run P1 test (default, LLM-optimized)
uv run python cocotb_tests/run.py forge_util_clk_divider
# Expected: <20 lines output, PASS result, ~5 seconds

# Run P2 test (comprehensive)
TEST_LEVEL=P2_INTERMEDIATE uv run python cocotb_tests/run.py forge_util_clk_divider
# Expected: <50 lines output, more edge cases

# Run all P1 tests
uv run python cocotb_tests/run.py --all
```

---

## 🎯 Design Principles

1. **Cloud-First** - Works in browser without local toolchain
2. **LLM-Friendly** - Token-efficient testing, progressive documentation
3. **Type Safety** - Explicit voltage domains, function-based utilities
4. **Verilog Compatible** - No VHDL enums, records, physical types
5. **Standards-Driven** - VHDL-2008, consistent naming, port order conventions
6. **Progressive Testing** - Start fast (P1), validate thoroughly (P2), stress test (P3)

---

## 📖 Additional Resources

**Repository Summary:** `REPO_SUMMARY.md` - Complete overview and status
**Web Worker Guide:** `WEB_WORKER_ONBOARDING.md` - Detailed onboarding reference
**Quick Start:** `QUICK_START_WEB_WORKER.txt` - Copy-paste prompt for Claude Code Web
**Migration Guide:** `MIGRATION.md` - Upgrading from older versions
**Changelog:** `CHANGELOG.md` - Version history
**Release Notes:** `RELEASE_NOTES_v3.1.0.md` - Latest features

---

## 📄 License

MIT License - See `LICENSE` file

---

**Version:** 3.2.0
**Repository:** https://github.com/vmars-20/forge-vhdl-3v3-vmars
**Status:** Production-ready template for web-workers
**Last Updated:** 2025-11-08
