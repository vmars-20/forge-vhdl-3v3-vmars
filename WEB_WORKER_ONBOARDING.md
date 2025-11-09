# Web Worker Onboarding Prompt

**Copy-paste this into Claude Code Web to validate and test the forge-vhdl environment.**

---

## Mission

You're onboarding to the **forge-vhdl** repository - a cloud-first VHDL framework with AI-assisted workflows. Your task is to:

1. **Verify environment setup** (check for setup scripts, run if needed)
2. **Run pre-existing tests** (validate VHDL simulation infrastructure)
3. **Gather requirements for a new module** (test the requirements workflow)

**IMPORTANT:** Not all steps may succeed on first try. Follow diagnostic protocols below.

---

## Phase 1: Environment Setup & Validation

### Step 1.1: Read Project Documentation
```
Read llms.txt and CLAUDE.md to understand the repository structure.
```

### Step 1.2: Check for Setup Scripts
```
Look for setup scripts in scripts/ directory. Common patterns:
- scripts/cloud_setup_with_ghdl.py
- scripts/setup.sh
- scripts/validate_setup.sh
```

### Step 1.3: Run Cloud Setup (if in browser/container)
```bash
# If you're in Claude Code Web, GitHub Codespaces, or container:
uv run python scripts/cloud_setup_with_ghdl.py

# Expected: GHDL installation, Python environment setup, validation test
# Duration: ~2-3 minutes
```

**Diagnostic Protocol - Setup Failures:**
- ❌ **"uv command not found"** → Install UV: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- ❌ **"GHDL not found after setup"** → Check `which ghdl`, verify `/usr/bin/ghdl` exists
- ❌ **"LLVM library not found"** → Setup script should create symlink, check error messages
- ❌ **"Permission denied"** → May need `sudo` for system package installation

**Log to file:** `environment_setup_status.txt`

### Step 1.4: Commit Phase 1
```bash
# Create a git commit documenting environment status
git add environment_setup_status.txt
git commit -m "web-worker: Environment setup validation completed

Setup script: scripts/cloud_setup_with_ghdl.py
GHDL version: [insert from 'ghdl --version']
Python version: [insert from 'python --version']
UV version: [insert from 'uv --version']

Status: [SUCCESS/PARTIAL/FAILED]
Issues: [list any problems encountered]

🤖 Web Worker Session - Phase 1
Co-Authored-By: Claude <noreply@anthropic.com>"

git push origin main
```

---

## Phase 2: Test Validation

### Step 2.1: List Available Tests
```bash
uv run python cocotb_tests/run.py --list

# Expected output: List of VHDL component tests
# Key tests to look for:
# - forge_util_clk_divider
# - forge_lut_pkg
# - forge_voltage_3v3_pkg
# - forge_hierarchical_encoder
```

**Diagnostic Protocol - Test Listing Failures:**
- ❌ **"ModuleNotFoundError: No module named 'cocotb'"** → Run `uv sync` to install dependencies
- ❌ **"test_configs.py not found"** → Check `cocotb_tests/test_configs.py` exists
- ❌ **Empty test list** → Check `test_configs.py` has test entries

### Step 2.2: Run P1 Tests (LLM-Optimized)
```bash
# Run a simple component test first
uv run python cocotb_tests/run.py forge_util_clk_divider

# Expected: <20 line output, PASS result, ~5 second runtime
```

**Diagnostic Protocol - Test Execution Failures:**
- ❌ **"GHDL elaboration failed"** → VHDL syntax error, check GHDL output for file:line
- ❌ **"Simulation timeout"** → Test hung, check for infinite loops in VHDL
- ❌ **"AttributeError: 'HierarchyObject' object has no attribute 'value'"** → CocoTB type constraint violation (see CLAUDE.md "Critical CocoTB Interface Rules")
- ❌ **287 lines of metavalue warnings** → GHDL filter not working, check `GHDL_FILTER_LEVEL` env var

**Log to file:** `test_execution_results.txt`

### Step 2.3: Run Multiple P1 Tests
```bash
# Test voltage packages (should be fast)
uv run python cocotb_tests/run.py forge_voltage_3v3_pkg
uv run python cocotb_tests/run.py forge_voltage_5v0_pkg
uv run python cocotb_tests/run.py forge_voltage_5v_bipolar_pkg

# Expected: All PASS, <20 lines each, total <60 lines
```

### Step 2.4: Commit Phase 2
```bash
# Document test results
git add test_execution_results.txt
git commit -m "web-worker: Test validation completed

Tests executed:
- forge_util_clk_divider: [PASS/FAIL]
- forge_voltage_3v3_pkg: [PASS/FAIL]
- forge_voltage_5v0_pkg: [PASS/FAIL]
- forge_voltage_5v_bipolar_pkg: [PASS/FAIL]

Total tests: X
Passed: Y
Failed: Z
Output lines: [should be <80 for 4 P1 tests]

Issues: [list any problems]

🤖 Web Worker Session - Phase 2
Co-Authored-By: Claude <noreply@anthropic.com>"

git push origin main
```

---

## Phase 3: Requirements Gathering (If Tests Pass)

### Step 3.1: Run Requirements Gathering Slash Command
```
Type this command:
/gather-requirements

# This launches an interactive 7-phase Q&A to gather requirements for a new VHDL component.
# You'll be asked about:
# - Component identification (name, purpose, category)
# - Functionality (what it does, how it works)
# - Interface specification (ports, generics)
# - Behavior specification (states, timing, edge cases)
# - Testing strategy (what to test, expected results)
# - Design guidance (architectural patterns)
# - Specification generation (creates markdown spec file)
```

**Diagnostic Protocol - Requirements Gathering Issues:**
- ❌ **"slash command not found"** → Check `.claude/commands/gather-requirements.md` exists
- ❌ **"No response from agent"** → Slash command may not be supported in your environment
- ⚠️ **Manual alternative:** Read `workflow/specs/pending/edge_detector.md` as example, create similar spec manually

### Step 3.2: Review Generated Specification
```bash
# Check for generated spec file
ls workflow/specs/pending/

# Expected: A new .md file with your component specification
# Example: workflow/specs/pending/my_component.md
```

### Step 3.3: Commit Phase 3 (Optional)
```bash
# If requirements gathering succeeded
git add workflow/specs/pending/*.md
git commit -m "web-worker: Requirements gathering completed

Component: [component name]
Category: [utilities/debugging/loader]
Specification: workflow/specs/pending/[filename].md

Ready for: Automated 4-agent workflow (generate → design → test)

🤖 Web Worker Session - Phase 3
Co-Authored-By: Claude <noreply@anthropic.com>"

git push origin main
```

---

## Success Criteria

### ✅ Minimum Success (Environment Works)
- Setup script completed without errors
- `ghdl --version` returns valid output
- At least 1 P1 test passes
- Git commits pushed successfully

### ✅ Good Success (Tests Work)
- 3+ P1 tests pass
- Total output <60 lines for all tests
- Test runtime <15 seconds total
- No GHDL filter issues

### ✅ Excellent Success (Full Workflow)
- All P1 tests pass
- Requirements gathering works
- Specification generated successfully
- Ready to run 4-agent automated workflow

---

## Troubleshooting Resources

**If stuck, read these in order:**
1. `CLAUDE.md` - Section "Quick Start: Cloud Setup"
2. `docs/CLOUD_SETUP_PROMPT.md` - Detailed setup walkthrough
3. `docs/COCOTB_TROUBLESHOOTING.md` - Test-specific debugging
4. `docs/diagnostic_reports/README.md` - Known issues and fixes

**Common first-time issues:**
- GHDL not in PATH after installation → Restart shell or run `hash -r`
- UV virtual environment not activated → Should be automatic, check `.venv/`
- Test timeouts in cloud environments → Normal, GHDL simulation is CPU-intensive
- Missing dependencies → Run `uv sync` to install all workspace packages

---

## Next Steps After Onboarding

If all phases succeed:
1. **Run automated workflow** on example spec: `workflow/specs/pending/edge_detector.md`
2. **Implement new component** using requirements gathering
3. **Review existing components** in `vhdl/components/` for patterns
4. **Extend test coverage** by adding P2/P3 tests to existing components

---

## Commit Message Template

For consistency, use this format for all commits:

```
web-worker: [Brief description]

[Detailed explanation of what was done]

Phase: [1-Environment / 2-Testing / 3-Requirements]
Status: [SUCCESS/PARTIAL/FAILED]
Issues: [any problems encountered]

🤖 Web Worker Session - Phase [N]
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

**Ready? Copy this entire document and paste into Claude Code Web to begin!**
