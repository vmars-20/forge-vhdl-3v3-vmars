# 🚀 forge-vhdl: AI-Powered VHDL Development in Minutes

**Build tested VHDL components in 2-5 minutes with AI agents.**

[![Use This Template](https://img.shields.io/badge/Use%20This%20Template-2ea44f?style=for-the-badge&logo=github)](../../generate)

---

## ⚡ Quick Start

### 1. Use This Template

**Click the green button:**

![Use This Template](static/github-webui-use-this-template-callout.png)

Or click here: [![Use This Template](https://img.shields.io/badge/Use%20This%20Template-2ea44f?style=for-the-badge&logo=github)](../../generate)

### 2. Clone & Launch

```bash
git clone git@github.com:YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
uv sync
claude
/forge-start
```

### 3. Build Your Component

The interactive workflow starts automatically:

![Claude CLI Running](static/Local-CLI-Running-user-input.png)

**That's it!** Answer 2-5 questions → Get tested VHDL → Done in minutes.

---

## 🌐 Setting Up Claude Code Web for Agent Execution

After generating your requirements locally, you'll run the 3-agent workflow in Claude Code Web for unlimited autonomous execution.

### Step 1: Complete Requirements Locally

Run `/forge-start` in your local Claude CLI and answer the questions. You'll see:

![Requirements Complete - Handoff Prompt](static/Local-CLI-Requirements-Complete-Handoff.png)
*📝 Note: This screenshot will be added - shows completion message and cloud handoff suggestion*

### Step 2: Push Your Specification

```bash
git add workflow/specs/pending/
git commit -m "spec: Add [your component name]"
git push
```

### Step 3: Open Claude Code Web

Navigate to **https://claude.ai/code/** in your browser.

### Step 4: Select Your Repository

Click the repository dropdown on the **left side** and select your forked repository:

![Select Repository](static/Claude-WEB-ui-new-session.png)

**Important:** The branch is automatically set to `main` - you cannot change this. Claude Web creates a temporary sandbox branch internally for its work.

### Step 5: Choose Network Access Policy

Click the environment dropdown on the **right side** and select a network policy:

![Choose Network Policy](static/Claude-WEB-ui-new-cloude-env-selection.png)

**Recommended:** Select **"Trusted network access"** or **"Full network access"**

- ✅ **Trusted network access** - Downloads packages from verified sources (needed for GHDL auto-install)
- ✅ **Full network access** - Unrestricted (use if trusted fails)
- ⚠️ **No network access** - Blocks GHDL installation, won't work for this project

### Step 6: Start the Agent Workflow

Once your session starts, paste this prompt:

```
Read workflow/specs/pending/[your-component-name].md and execute the 3-agent workflow
```

**What happens next:**
1. GHDL auto-installs in the cloud environment (zero setup!)
2. Agent 1 generates VHDL code
3. Agent 2 designs progressive tests (P1/P2/P3)
4. Agent 3 implements and runs tests with incremental commits
5. All work is committed to a temporary sandbox branch
6. You pull the results back locally (auto-merges to main)

### Step 7: Pull Results Locally

```bash
git pull
# Artifacts now in workflow/artifacts/
# Tests already in cocotb_tests/
```

---

## 🔄 Two Workflows

### 🚀 AI-First (DEFAULT - 2-5 Minutes)

**Best for:** Students, quick prototyping, learning

```
/forge-start
> Choose: AI-First Workflow
> Answer: 2-3 critical questions
> Claude infers everything else from patterns
> Get: Tested VHDL component
```

**Time:** 2-5 minutes
**Guide:** `workflow/AI_FIRST_REQUIREMENTS.md`

### 🔧 Engineer (Advanced - 15-30 Minutes)

**Best for:** Complex systems, full control, detailed specs

```
/forge-start
> Choose: Engineer Workflow
> Answer: 30-question structured interview
> Full specification with all details
> Get: Production-ready component
```

**Time:** 15-30 minutes
**Guide:** `workflow/ENGINEER_REQUIREMENTS.md`

---

## 💻 Local + Cloud Hybrid (Recommended)

**Use each environment for what it does best:**

### Local CLI: Requirements Gathering
```bash
claude
/forge-start
# Answer questions → Spec created
git add workflow/specs/pending/ && git commit && git push
```

### Cloud: Agent Execution

Open [Claude Code Web](https://claude.ai/code/):

![Select Repository](static/Claude-WEB-ui-new-session.png)

![Choose Environment](static/Claude-WEB-ui-new-cloude-env-selection.png)

```
"Read workflow/specs/pending/my_component.md and execute the 3-agent workflow"
```

**Agents run autonomously:**
- Agent 1: Generate VHDL
- Agent 2: Design tests (P1/P2/P3)
- Agent 3: Execute & validate

### Local CLI: Integration
```bash
git pull  # Get agent results
mv workflow/artifacts/vhdl/*.vhd vhdl/components/
# Tests already in cocotb_tests/
```

**Why?**
- ✅ Local = Fast prompts, controlled output
- ✅ Cloud = Unlimited agents, zero setup
- ✅ Local = Final review, integration

---

## 🧪 Progressive Testing

**Traditional VHDL:** 287 lines of metavalue warnings
**forge-vhdl P1:** 8 lines total

| Level | Tests | Output | Runtime | Use Case |
|-------|-------|--------|---------|----------|
| **P1** | 2-4 essential | <20 lines | <5 sec | Default (LLM-optimized) |
| **P2** | 5-10 comprehensive | <50 lines | <30 sec | Standard validation |
| **P3** | 15-25 stress tests | <100 lines | <2 min | Full coverage |

```bash
# Run P1 tests (default)
uv run python cocotb_tests/run.py my_component

# Example output:
# ✅ PASS: Reset test
# ✅ PASS: Basic operation
# ✅ PASS: Enable control
# 3/3 tests passed (0.5s)
```

---

## 📦 Included Components

**Utilities** (`vhdl/utilities/`)
- `forge_util_clk_divider` - Programmable clock divider

**Voltage Packages** (`vhdl/packages/`)
- `forge_voltage_3v3_pkg` - 0-3.3V (TTL, GPIO)
- `forge_voltage_5v0_pkg` - 0-5.0V (sensors)
- `forge_voltage_5v_bipolar_pkg` - ±5.0V (Moku DAC/ADC)

**LUT Utilities** (`vhdl/packages/`)
- `forge_lut_pkg` - Voltage/index conversion

**Debugging** (`vhdl/debugging/`)
- `forge_hierarchical_encoder` - FSM state encoding

**Full catalog:** `llms.txt`

---

## 🔧 Requirements

### Local Development

**Required:**
- [Claude Code CLI](https://claude.com/claude-code)
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- [GHDL](https://github.com/ghdl/ghdl) (VHDL simulator)

**Install GHDL:**
```bash
# macOS
brew install ghdl

# Ubuntu/Debian
sudo apt-get install ghdl ghdl-llvm
```

**Verify setup:**
```bash
uv run python .claude/env_detect.py
```

### Cloud Development

**Required:** None! GHDL auto-installs.

**Options:**
- [GitHub Codespaces](../../codespaces/new) - Zero setup
- [Claude Code Web](https://claude.ai/code/) - Browser-based

---

## 📖 Documentation

**Start here:**
- `README.md` (this file) - Quick start
- `CLAUDE.md` - Environment router
- `.claude/CLAUDE_LOCAL.md` - Local CLI guide
- `.claude/CLAUDE_CLOUD.md` - Cloud guide

**Detailed guides:**
- `workflow/AI_FIRST_REQUIREMENTS.md` - Fast workflow
- `workflow/ENGINEER_REQUIREMENTS.md` - Advanced workflow
- `docs/VHDL_CODING_STANDARDS.md` - Style guide
- `docs/PROGRESSIVE_TESTING_GUIDE.md` - Test patterns
- `workflow/specs/reference/` - Example components

**Quick reference:**
- `llms.txt` - Component catalog (~800 tokens)

---

## 🎓 Example Session

```
$ claude
Claude Code CLI started

> /forge-start

🚀 AI-FIRST WORKFLOW ACTIVATED (Student Mode)

Let's start! What component would you like to build?

Examples:
- "A PWM generator for LED dimming"
- "An edge detector for signal transitions"

> lets start with a PWM generator

Great! I need to know:
1. What clock frequency will this run at?
> 125 MHz

2. What PWM frequency range do you need?
> 1 kHz to 100 kHz

Perfect! Here's your specification:
[Shows complete spec with inferred defaults]

Does this look correct? (yes/no)
> yes

✅ Specification created: workflow/specs/pending/pwm_generator.md

Would you like to:
1. Execute agents in cloud (recommended - unlimited runtime)
2. Execute agents locally (uses your token budget)
> 1

📤 Push spec to GitHub first:
git add workflow/specs/pending/pwm_generator.md
git commit -m "spec: Add PWM generator"
git push

Then open Claude Web:
https://claude.ai/code/

Say: "Read workflow/specs/pending/pwm_generator.md and execute the 3-agent workflow"
```

---

## 🛠️ VHDL Standards

**Key rules enforced:**

| Rule | Correct ✅ | Wrong ❌ |
|------|-----------|----------|
| **FSM States** | `constant STATE_IDLE : std_logic_vector(1 downto 0) := "00";` | `type state_t is (IDLE, ARMED);` |
| **Port Order** | clk, rst_n, clk_en, enable, data, status | Random order |
| **Reset Hierarchy** | `if rst_n = '0' then ... elsif clk_en = '1'` | Flat structure |
| **Signal Prefixes** | `ctrl_`, `cfg_`, `stat_`, `dbg_` | No prefixes |

**Why?**
- Verilog compatibility (Moku uses mixed VHDL/Verilog)
- Synthesis predictability
- Safety (hierarchical reset prevents unsafe states)

**Full guide:** `docs/VHDL_CODING_STANDARDS.md`

---

## 🐛 Troubleshooting

### "GHDL not found"

**Local:**
```bash
brew install ghdl  # macOS
sudo apt-get install ghdl ghdl-llvm  # Linux
```

**Cloud:**
Should auto-install. If not: `uv run python scripts/cloud_setup_with_ghdl.py`

### "Test output too verbose"

Check test level:
```bash
echo $TEST_LEVEL  # Should be P1_BASIC or unset
echo $GHDL_FILTER_LEVEL  # Should be "aggressive"
```

See `docs/PROGRESSIVE_TESTING_GUIDE.md`

### "Can't find /forge-start command"

Verify Claude Code CLI output settings:

![Output Settings](static/Claude-CLI-output-settings.png)

Run `/config` to check settings.

---

## 📝 Post-Template Checklist

After creating your repository:

- [ ] Clone repository locally
- [ ] Run `uv sync`
- [ ] Install GHDL (if local development)
- [ ] Run `uv run python .claude/env_detect.py`
- [ ] Update this README with your repository URL
- [ ] Try first component: `claude` then `/forge-start`
- [ ] Verify P1 test output <20 lines
- [ ] Commit your work

---

## 🤝 Contributing

This is a template repository. After forking:

1. Customize for your project
2. Follow VHDL coding standards (`docs/VHDL_CODING_STANDARDS.md`)
3. Ensure P1 tests stay <20 lines
4. Submit PRs to original template for framework improvements

---

## 📄 License

MIT License - See `LICENSE` file

---

## 📚 Additional Resources

**For humans:**
- Start with environment detection (run `.claude/env_detect.py`)
- Read environment guide (`.claude/CLAUDE_LOCAL.md` or `.claude/CLAUDE_CLOUD.md`)
- Browse reference specs (`workflow/specs/reference/`)
- Try `/forge-start` command

**For AI agents:**
- Start with `llms.txt` (component catalog)
- Load `CLAUDE.md` (comprehensive guide)
- Load detailed docs only when needed

---

## 🎉 Ready to Build!

```bash
git clone git@github.com:YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
uv sync
claude
/forge-start
```

**Build your first component in the next 5 minutes!**

---

**Version:** 3.2.0
**Template:** https://github.com/vmars-20/forge-vhdl-3v3-vmars
**Your Repository:** 🔧 **UPDATE THIS** → `https://github.com/YOUR-USERNAME/YOUR-REPO-NAME`
**Last Updated:** 2025-11-09
**Maintainer:** Moku Instrument Forge Team
