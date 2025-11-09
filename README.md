# forge-vhdl: AI-Assisted VHDL Development Template

**Version:** 3.2.0
**Purpose:** GitHub template for VHDL development with Claude Code (Local CLI or Cloud)
**Target Audience:** Students, engineers, FPGA developers learning VHDL-2008

---

## 🎯 What Is This?

**forge-vhdl** is a batteries-included GitHub template for VHDL component development with:

- **AI-assisted workflows** - 2-5 minute requirements gathering → automated VHDL + test generation
- **Progressive testing** - P1/P2/P3 test levels with 98% output reduction (<20 lines for LLM iteration)
- **Cloud-first design** - Full VHDL simulation in browser (no local toolchain required)
- **Local CLI support** - Interactive development for advanced users with local GHDL
- **VHDL-2008 standards** - Verilog-compatible patterns, no enums, hierarchical reset
- **Component library** - Reusable utilities, voltage packages, FSM debugging tools

**Key Innovation:** Optimized for Claude Code with token-efficient testing and environment auto-detection.

---

## 🚀 Getting Started (Choose Your Path)

### Option 1: Use This Template (Cloud - RECOMMENDED)

**Perfect for:** Students, beginners, anyone who wants zero local setup

1. **Click "Use this template" → "Create a new repository"**
2. **Open in GitHub Codespaces** (or clone and open in Claude Code Web)
3. **Run environment detection:**
   ```bash
   uv run python .claude/env_detect.py
   ```
4. **You'll see:**
   ```
   ╔════════════════════════════════════════════════════════════════════╗
   ║  🌐 CLOUD ENVIRONMENT DETECTED                                     ║
   ║  ✅ GHDL Found: GHDL 5.0 (LLVM backend)                            ║
   ║  Ready for VHDL development! Using cloud workflow.                 ║
   ╚════════════════════════════════════════════════════════════════════╝
   ```
5. **Read the cloud guide:** `.claude/CLAUDE_CLOUD.md`
6. **Try your first component:**
   ```
   "I need a PWM generator. Use the AI-First workflow."
   ```

**What happens automatically:**
- ✅ GHDL 5.0 pre-installed via DevContainer
- ✅ CocoTB testing framework ready
- ✅ Python dependencies installed (UV package manager)
- ✅ Claude Code configured for cloud workflow

---

### Option 2: Clone Locally (Advanced)

**Perfect for:** Engineers with local GHDL, advanced users, contributors

1. **Clone this repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Install GHDL locally:**
   ```bash
   # macOS
   brew install ghdl

   # Ubuntu/Debian
   sudo apt-get install ghdl ghdl-llvm
   ```

3. **Run environment detection:**
   ```bash
   uv run python .claude/env_detect.py
   ```

4. **You'll see:**
   ```
   ╔════════════════════════════════════════════════════════════════════╗
   ║  💻 LOCAL ENVIRONMENT DETECTED (Claude Code CLI)                   ║
   ║  ✅ GHDL Found: GHDL X.X.X                                         ║
   ║  Before we start, verify your output settings: /config             ║
   ╚════════════════════════════════════════════════════════════════════╝
   ```

5. **Read the local guide:** `.claude/CLAUDE_LOCAL.md`
6. **Verify Claude CLI output settings** (see local guide for details)

---

## 🧭 Environment Auto-Detection

This template **automatically detects** whether you're running:

| Environment | Detected When | Guide | Key Features |
|-------------|---------------|-------|--------------|
| **🌐 Cloud** | GitHub Codespaces, Gitpod, Docker containers | `.claude/CLAUDE_CLOUD.md` | GHDL pre-installed • Automated agents • Zero setup |
| **💻 Local** | Claude Code CLI on your machine | `.claude/CLAUDE_LOCAL.md` | Interactive requirements • Manual testing • Full control |

**Detection script:** `.claude/env_detect.py` (run anytime to see your environment)

**The split is critical because:**
- **Cloud:** GHDL must be installed automatically (users can't/won't install it)
- **Local:** GHDL may already be installed, users have more control over output settings

---

## 📖 Documentation Quick Links

**Start here after detecting your environment:**

| Document | Purpose | Audience |
|----------|---------|----------|
| `CLAUDE.md` | Master router - directs you to environment-specific guide | Everyone (first read) |
| `.claude/CLAUDE_LOCAL.md` | Local development guide (interactive, manual testing) | Local CLI users |
| `.claude/CLAUDE_CLOUD.md` | Cloud development guide (automated, pre-configured) | Web/Codespaces users |
| `llms.txt` | Component catalog quick reference (~800 tokens) | AI agents |

**Detailed references (load as needed):**
- `docs/VHDL_CODING_STANDARDS.md` - Complete VHDL-2008 style guide (600 lines)
- `docs/PROGRESSIVE_TESTING_GUIDE.md` - How to write P1/P2/P3 tests
- `docs/COCOTB_TROUBLESHOOTING.md` - Test debugging patterns
- `workflow/specs/reference/` - 5 gold-standard component examples

---

## ⚡ Quick Examples

### Example 1: AI-First Workflow (Default for Students)

```
User: "I need an edge detector for rising edges. Use the AI-First workflow."

Claude: What clock frequency will this run at? (e.g., 125 MHz)
User: 125 MHz

Claude: [Proposes complete specification based on pattern recognition]
        Does this look correct?
User: Yes

Claude: [Invokes 3 agents automatically]
        ✅ VHDL generated (workflow/artifacts/vhdl/forge_util_edge_detector.vhd)
        ✅ Tests designed (P1: 4 tests, P2: 7 tests)
        ✅ Tests passing (4/4 PASS, <20 line output)

Claude: Ready to review! Artifacts in workflow/artifacts/
```

**Time:** 2-5 minutes from idea to tested VHDL

---

### Example 2: Reference Spec Workflow (Fast Start)

```
User: "Read workflow/specs/reference/pwm_generator.md and execute the 3-agent workflow"

Claude: [Reads proven specification]
        [Invokes agents automatically]
        ✅ VHDL generated
        ✅ Tests passing (5/5 PASS)

Claude: PWM generator ready! See workflow/artifacts/
```

**Time:** <1 minute (no questions, uses proven pattern)

---

## 🧪 Progressive Testing (Key Innovation)

**Traditional VHDL testbenches:** 287 lines of metavalue warnings, timing noise, debug spam

**forge-vhdl P1 tests:** 8 lines total output

| Test Level | Tests | Output | Runtime | When to Use |
|------------|-------|--------|---------|-------------|
| **P1** | 2-4 essential | <20 lines | <5 sec | **Default** (LLM-optimized for fast iteration) |
| **P2** | 5-10 comprehensive | <50 lines | <30 sec | Standard validation before commit |
| **P3** | 15-25 stress tests | <100 lines | <2 min | Full coverage, edge cases |
| **P4** | Unlimited debug | No limit | No limit | Deep debugging only |

**Example P1 output:**
```bash
$ uv run python cocotb_tests/run.py forge_util_clk_divider

Running P1 tests for forge_util_clk_divider...

✅ PASS: Reset test
✅ PASS: Divide by 2
✅ PASS: Divide by 4
✅ PASS: Enable control

4/4 tests passed (0.8s)
```

**How?** GHDL output filtering + strategic test case selection + assertion-based validation.

**Why?** Token-efficient for LLM analysis - Claude can read full test results in context window.

---

## 🔧 VHDL Standards Summary

This template enforces **Verilog-compatible VHDL-2008** patterns:

| Standard | Correct ✅ | Forbidden ❌ |
|----------|-----------|--------------|
| **FSM States** | `constant STATE_IDLE : std_logic_vector(1 downto 0) := "00";` | `type state_t is (IDLE, ARMED);` ← NO ENUMS |
| **Port Order** | clk, rst_n, clk_en, enable, data, status | Random order |
| **Reset Hierarchy** | `if rst_n = '0' then ... elsif clk_en = '1' then ... elsif enable = '1'` | Flat structure |
| **Signal Prefixes** | `ctrl_`, `cfg_`, `stat_`, `dbg_` | No prefixes |

**Why these rules?**
- Verilog compatibility (Moku platform uses mixed VHDL/Verilog)
- Synthesis predictability (explicit state encoding)
- Safety (hierarchical reset prevents unsafe states)

**Full guide:** `docs/VHDL_CODING_STANDARDS.md`

---

## 📦 Included Components

**Utilities** (`vhdl/utilities/`)
- `forge_util_clk_divider` - Programmable clock divider with enable

**Voltage Packages** (`vhdl/packages/`)
- `forge_voltage_3v3_pkg` - 0-3.3V (TTL, GPIO, digital glitch)
- `forge_voltage_5v0_pkg` - 0-5.0V (sensor supply)
- `forge_voltage_5v_bipolar_pkg` - ±5.0V (Moku DAC/ADC - **most common**)

**LUT Utilities** (`vhdl/packages/`)
- `forge_lut_pkg` - Voltage/index conversion functions

**Debugging** (`vhdl/debugging/`)
- `forge_hierarchical_encoder` - FSM state encoding for oscilloscope

**All components include:**
- ✅ P1 tests (LLM-optimized, <20 lines)
- ✅ P2 tests (comprehensive validation)
- ✅ VHDL-2008 compliant code
- ✅ CocoTB testbenches

**Full catalog:** `llms.txt`

---

## 🎓 Workflows Included

### 1. AI-First Requirements (DEFAULT - 2-5 min)
**Best for:** Students, clear requirements, pattern-matched components

**Process:**
1. Tell Claude what you need in plain English
2. Answer 2-3 critical questions
3. Claude infers the rest from patterns
4. Automated 3-agent workflow generates VHDL + tests

**Guide:** `workflow/AI_FIRST_REQUIREMENTS.md`

---

### 2. Engineer Requirements (Advanced - 15-30 min)
**Best for:** Novel architectures, complex systems, learning VHDL in depth

**Process:**
1. Request Engineer workflow
2. Answer 30-question structured interview
3. Detailed specification with full control
4. Manual or automated implementation

**Guide:** `workflow/ENGINEER_REQUIREMENTS.md`

---

### 3. Reference Spec Execution (<1 min)
**Best for:** Learning from proven examples, fast prototyping

**Process:**
1. Choose a reference spec (edge detector, PWM, debouncer, etc.)
2. Claude executes 3-agent workflow automatically
3. VHDL + tests generated from proven pattern

**Reference specs:** `workflow/specs/reference/`

---

## 🐛 Troubleshooting

### Environment Detection Not Working

```bash
# Run detection script manually
uv run python .claude/env_detect.py

# Check indicators
echo $CODESPACES         # Should be "true" in GitHub Codespaces
echo $GITPOD_WORKSPACE_ID # Should be set in Gitpod
ls /.dockerenv           # Should exist in Docker containers
```

### GHDL Not Found (Local)

```bash
# macOS
brew install ghdl

# Ubuntu/Debian
sudo apt-get install ghdl ghdl-llvm

# Then restart Claude session
```

### GHDL Not Found (Cloud)

**Should NEVER happen in DevContainer environments** - GHDL is pre-installed.

If you see this error in cloud, report as bug. Workaround:
```bash
uv run python scripts/cloud_setup_with_ghdl.py
```

### Test Output Too Verbose (>20 lines)

Check your test level:
```bash
# Should show P1_BASIC or be unset
echo $TEST_LEVEL

# Check filter level
echo $GHDL_FILTER_LEVEL  # Should be "aggressive" for P1
```

See `docs/PROGRESSIVE_TESTING_GUIDE.md` for details.

---

## 🎯 Next Steps (Post-Fork Checklist)

After creating your repository from this template:

- [ ] **Detect environment:** `uv run python .claude/env_detect.py`
- [ ] **Read environment guide:** `.claude/CLAUDE_LOCAL.md` or `.claude/CLAUDE_CLOUD.md`
- [ ] **Verify GHDL:** Should show "✅ GHDL Found" in detection output
- [ ] **Try first component:** "I need an edge detector. Use the AI-First workflow."
- [ ] **Run P1 tests:** `uv run python cocotb_tests/run.py --list` then run a component test
- [ ] **Verify output:** Should be <20 lines for P1 tests
- [ ] **Commit your work:** Git workflow documented in environment guide

---

## 📄 License

MIT License - See `LICENSE` file

---

## 🤝 Contributing

This is a template repository. After forking:

1. Customize for your project (rename components, add your own)
2. Follow VHDL coding standards (`docs/VHDL_CODING_STANDARDS.md`)
3. Ensure P1 tests stay <20 lines (LLM-optimized)
4. Submit pull requests to original template if you improve the framework

---

## 📚 Additional Resources

**For AI Agents:**
- Start with `llms.txt` (quick reference)
- Then load `CLAUDE.md` (comprehensive guide)
- Load detailed docs only when needed (token-efficient)

**For Humans:**
- Start with environment detection (this README)
- Read environment-specific guide (`.claude/CLAUDE_LOCAL.md` or `.claude/CLAUDE_CLOUD.md`)
- Browse reference specs for examples (`workflow/specs/reference/`)
- Consult detailed guides as needed (`docs/`)

---

**Version:** 3.2.0
**Template Repository:** https://github.com/vmars-20/forge-vhdl-3v3-vmars
**Status:** Production-ready GitHub template
**Last Updated:** 2025-11-09
**Maintainer:** Moku Instrument Forge Team

**Quick Links:**
- Environment Detection: `.claude/env_detect.py`
- Local Guide: `.claude/CLAUDE_LOCAL.md`
- Cloud Guide: `.claude/CLAUDE_CLOUD.md`
- Component Catalog: `llms.txt`
- VHDL Standards: `docs/VHDL_CODING_STANDARDS.md`
