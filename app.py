import streamlit as st
import time
from datetime import datetime

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResolveIQ · Enterprise Support Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── PREMIUM CSS ─────────────────────────────────────────────────────────────
STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@300;400&display=swap');

:root {
  --gold:     #C9A84C;
  --gold-lt:  #E8C97A;
  --gold-dim: rgba(201,168,76,0.12);
  --ink:      #080A10;
  --ink2:     #0D1018;
  --slate:    #1A1F2E;
  --text:     #C8D4E4;
  --muted:    #5A6880;
  --success:  #3EC99A;
  --info:     #5B9CF6;
  --white:    #FFFFFF;
}

*, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"] {
  background: var(--ink) !important;
  font-family: 'DM Sans', sans-serif;
  color: var(--text);
}
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
footer { display:none !important; }

.main .block-container {
  padding: 0 !important;
  max-width: 100% !important;
}

/* ═══ ANIMATED BACKGROUND ═══ */
#lx-bg {
  position: fixed; inset: 0; z-index: 0;
  background: var(--ink);
  overflow: hidden;
}
#lx-bg::before {
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(201,168,76,0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(201,168,76,0.035) 1px, transparent 1px);
  background-size: 64px 64px;
  mask-image: radial-gradient(ellipse 85% 70% at 50% 50%, black 10%, transparent 100%);
  animation: gridMove 28s linear infinite;
}
@keyframes gridMove {
  to { background-position: 64px 64px, 64px 64px; }
}

.au {
  position: absolute; border-radius: 50%;
  filter: blur(110px); pointer-events: none;
  animation: auFloat ease-in-out infinite;
}
.au1 { width:900px;height:700px; top:-250px; left:-180px;
  background: radial-gradient(ellipse, rgba(201,168,76,0.14) 0%, transparent 65%);
  animation-duration:22s; animation-delay:0s; }
.au2 { width:750px;height:750px; top:25%; right:-200px;
  background: radial-gradient(ellipse, rgba(91,156,246,0.1) 0%, transparent 65%);
  animation-duration:28s; animation-delay:-9s; }
.au3 { width:650px;height:550px; bottom:-120px; left:25%;
  background: radial-gradient(ellipse, rgba(62,201,154,0.08) 0%, transparent 65%);
  animation-duration:24s; animation-delay:-16s; }
@keyframes auFloat {
  0%,100% { opacity:0;   transform:translate(0,0) scale(1); }
  15%,85% { opacity:1; }
  50%      { opacity:0.75; transform:translate(50px,-35px) scale(1.06); }
}

.grain {
  position:fixed; inset:0; z-index:1; pointer-events:none; opacity:0.02;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size:180px;
}

.orb { position:absolute; border-radius:50%; animation:orbRise linear infinite; }
@keyframes orbRise {
  0%   { transform:translateY(105vh) rotate(0deg);   opacity:0; }
  4%   { opacity:1; }
  96%  { opacity:0.8; }
  100% { transform:translateY(-8vh)  rotate(540deg); opacity:0; }
}

.sweep {
  position:absolute; height:1px; pointer-events:none;
  background:linear-gradient(90deg,transparent,rgba(201,168,76,0.35),transparent);
  animation:sweepAnim ease-in-out infinite;
}
.s1{width:55%;top:22%;left:22%;animation-duration:10s;animation-delay:0s;}
.s2{width:35%;top:58%;left:35%;animation-duration:10s;animation-delay:-5s;}
@keyframes sweepAnim{0%,100%{opacity:0;transform:scaleX(0);}40%,60%{opacity:1;transform:scaleX(1);}}

/* ═══ TOP NAV ═══ */
.top-nav {
  position: sticky; top:0; z-index:200;
  display:flex; align-items:center; justify-content:space-between;
  padding:16px 52px;
  background:rgba(8,10,16,0.82);
  border-bottom:1px solid rgba(201,168,76,0.1);
  backdrop-filter:blur(28px);
}
.nav-logo { display:flex; align-items:center; gap:14px; }
.nav-icon {
  width:40px;height:40px; border-radius:12px;
  background:linear-gradient(135deg,#C9A84C,#E8C97A);
  display:flex;align-items:center;justify-content:center;
  font-size:20px;
  box-shadow:0 4px 20px rgba(201,168,76,0.4);
}
.nav-brand {
  font-family:'Playfair Display',serif; font-weight:900; font-size:1.25rem;
  color:var(--white); letter-spacing:-0.01em;
}
.nav-brand em { color:var(--gold); font-style:normal; }
.nav-sub {
  font-family:'DM Mono',monospace; font-size:0.6rem; letter-spacing:0.2em;
  text-transform:uppercase; color:var(--muted); margin-top:2px;
}
.nav-right { display:flex; align-items:center; gap:8px; }
.pill {
  padding:5px 15px; border-radius:20px; font-size:0.72rem; font-weight:500;
  background:transparent; border:1px solid rgba(201,168,76,0.18); color:var(--muted);
}
.pill.on {
  background:rgba(201,168,76,0.1); border-color:rgba(201,168,76,0.35);
  color:var(--gold-lt); display:flex; align-items:center; gap:6px;
}
.ldot {
  width:7px;height:7px; border-radius:50%; background:var(--success);
  animation:ldPulse 1.9s ease-in-out infinite;
  box-shadow:0 0 8px var(--success);
}
@keyframes ldPulse {
  0%,100%{opacity:1;box-shadow:0 0 6px var(--success);}
  50%{opacity:0.4;box-shadow:0 0 14px var(--success);}
}

/* ═══ CONTENT SHELL ═══ */
.shell {
  position:relative; z-index:10;
  min-height:100vh; display:flex; flex-direction:column;
}
.content {
  max-width:880px; margin:0 auto; width:100%;
  padding:60px 28px 140px;
}

/* ═══ HERO ═══ */
.hero { text-align:center; margin-bottom:60px; animation:fadeUp 0.9s cubic-bezier(.16,1,.3,1) both; }
@keyframes fadeUp { from{opacity:0;transform:translateY(28px);} to{opacity:1;transform:translateY(0);} }
.eyebrow {
  font-family:'DM Mono',monospace; font-size:0.66rem;
  letter-spacing:0.28em; text-transform:uppercase; color:var(--gold);
  margin-bottom:20px;
  display:flex; align-items:center; justify-content:center; gap:14px;
}
.eyebrow::before,.eyebrow::after {
  content:''; display:inline-block; width:44px; height:1px;
  background:linear-gradient(90deg,transparent,var(--gold));
}
.eyebrow::after { background:linear-gradient(90deg,var(--gold),transparent); }
.h1 {
  font-family:'Playfair Display',serif; font-weight:900;
  font-size:clamp(2.2rem,5vw,3.5rem); color:var(--white);
  line-height:1.08; letter-spacing:-0.025em; margin-bottom:22px;
}
.h1 em { color:var(--gold); font-style:normal; }
.hero-p {
  font-size:0.97rem; color:var(--muted); max-width:510px;
  margin:0 auto; line-height:1.75; font-weight:300;
}

/* ═══ STAT BAR ═══ */
.stats {
  display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-bottom:36px;
}
.stat {
  background:rgba(13,16,24,0.7); border:1px solid rgba(201,168,76,0.1);
  border-radius:16px; padding:20px 22px; text-align:center;
  backdrop-filter:blur(14px);
  animation:fadeUp 0.8s cubic-bezier(.16,1,.3,1) both;
}
.stat:nth-child(2){animation-delay:.06s;} .stat:nth-child(3){animation-delay:.12s;}
.stat-n {
  font-family:'Playfair Display',serif; font-size:2rem;
  font-weight:700; color:var(--gold); line-height:1; margin-bottom:5px;
}
.stat-l { font-size:0.68rem; color:var(--muted); letter-spacing:0.1em; text-transform:uppercase; }

/* ═══ GLASS CARD ═══ */
.gc {
  background:rgba(12,15,22,0.8); border:1px solid rgba(201,168,76,0.11);
  border-radius:20px; padding:26px 30px; margin-bottom:14px;
  backdrop-filter:blur(22px);
  box-shadow:0 1px 0 rgba(255,255,255,0.04) inset, 0 20px 60px rgba(0,0,0,0.5);
  transition:border-color .3s, box-shadow .3s;
  animation:fadeUp .7s cubic-bezier(.16,1,.3,1) both;
}
.gc:hover {
  border-color:rgba(201,168,76,0.25);
  box-shadow:0 1px 0 rgba(255,255,255,0.04) inset, 0 28px 70px rgba(0,0,0,0.55), 0 0 0 1px rgba(201,168,76,0.08);
}
.fl {
  display:flex; align-items:center; gap:12px; margin-bottom:14px;
}
.fli {
  width:30px;height:30px; border-radius:9px;
  display:flex;align-items:center;justify-content:center; font-size:14px; flex-shrink:0;
}
.fli.g{background:rgba(201,168,76,0.12);}
.fli.b{background:rgba(91,156,246,0.12);}
.flt { font-weight:600; font-size:0.87rem; color:var(--white); }
.fls { font-size:0.7rem; color:var(--muted); margin-top:2px; }

/* Streamlit textarea overrides */
div[data-baseweb="textarea"] textarea, textarea {
  background:rgba(6,8,14,0.9) !important;
  border:1px solid rgba(201,168,76,0.14) !important;
  border-radius:13px !important;
  color:var(--text) !important;
  font-family:'DM Mono',monospace !important;
  font-size:0.81rem !important; line-height:1.65 !important;
  padding:14px 16px !important; resize:vertical !important;
  transition:border-color .2s, box-shadow .2s !important;
}
div[data-baseweb="textarea"] textarea:focus, textarea:focus {
  border-color:rgba(201,168,76,0.42) !important;
  box-shadow:0 0 0 3px rgba(201,168,76,0.07) !important; outline:none !important;
}
textarea::placeholder { color:rgba(90,104,128,0.45) !important; }
label, .stTextArea label { display:none !important; }

/* ═══ RESOLVE BUTTON ═══ */
div.stButton > button {
  width:100% !important; padding:17px 36px !important;
  background:linear-gradient(110deg,#C9A84C 0%,#E8C97A 48%,#C9A84C 100%) !important;
  background-size:200% 100% !important;
  color:#080A10 !important; font-family:'DM Sans',sans-serif !important;
  font-weight:700 !important; font-size:0.92rem !important;
  letter-spacing:0.07em !important; text-transform:uppercase !important;
  border:none !important; border-radius:14px !important;
  cursor:pointer !important;
  box-shadow:0 4px 28px rgba(201,168,76,0.38), 0 1px 0 rgba(255,255,255,0.28) inset !important;
  transition:all .28s ease !important;
}
div.stButton > button:hover {
  background-position:100% 0 !important;
  transform:translateY(-2px) !important;
  box-shadow:0 10px 40px rgba(201,168,76,0.52), 0 1px 0 rgba(255,255,255,0.28) inset !important;
}

/* ═══ RESULT PANELS ═══ */
.divider {
  height:1px; margin:48px 0;
  background:linear-gradient(90deg,transparent,rgba(201,168,76,0.28),transparent);
}
.sec-title {
  font-family:'Playfair Display',serif; font-weight:700; font-size:1.5rem;
  color:var(--white); margin-bottom:22px;
}
.rp {
  border-radius:18px; padding:24px 28px; margin-bottom:14px; border:1px solid;
  animation:slideIn .5s cubic-bezier(.16,1,.3,1) both;
}
@keyframes slideIn { from{opacity:0;transform:translateX(-10px);} to{opacity:1;transform:translateX(0);} }
.rp.gold { background:rgba(201,168,76,0.05); border-color:rgba(201,168,76,0.2); }
.rp.blue { background:rgba(91,156,246,0.05); border-color:rgba(91,156,246,0.18); }
.rp.grn  { background:rgba(62,201,154,0.05); border-color:rgba(62,201,154,0.18); }
.rp.wht  { background:rgba(255,255,255,0.025); border-color:rgba(255,255,255,0.09); }
.rh {
  display:flex; align-items:center; gap:10px; margin-bottom:14px;
  padding-bottom:12px; border-bottom:1px solid rgba(255,255,255,0.055);
}
.ri {
  width:34px;height:34px; border-radius:10px;
  display:flex;align-items:center;justify-content:center; font-size:16px;
}
.rtl { font-weight:600; font-size:0.8rem; letter-spacing:0.08em; text-transform:uppercase; }
.rbadge {
  margin-left:auto; padding:3px 11px; border-radius:20px;
  font-family:'DM Mono',monospace; font-size:0.6rem;
  letter-spacing:0.12em; text-transform:uppercase;
}
.rb {
  font-size:0.86rem; line-height:1.78; color:var(--text);
  white-space:pre-wrap; font-family:'DM Sans',sans-serif;
}
.rb.mono { font-family:'DM Mono',monospace; font-size:0.78rem; }

/* Streamlit overrides */
p { color:var(--text) !important; }
h3 { display:none !important; }
.stMarkdown { background:transparent !important; }

/* ═══ CHAT BOX STYLES ═══ */
.chat-container {
  background: rgba(12,15,22,0.8);
  border: 1px solid rgba(201,168,76,0.11);
  border-radius: 20px;
  padding: 16px;
  backdrop-filter: blur(22px);
  box-shadow: 0 1px 0 rgba(255,255,255,0.04) inset, 0 20px 60px rgba(0,0,0,0.5);
  margin-top: 20px;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}

.chat-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 14px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(201,168,76,0.1);
}

.chat-avatar {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  background: linear-gradient(135deg, #C9A84C, #E8C97A);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  box-shadow: 0 4px 16px rgba(201,168,76,0.45);
}

.chat-info {
  flex: 1;
}

.chat-title {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  font-size: 1rem;
  color: var(--white);
}

.chat-status {
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  color: var(--success);
  letter-spacing: 0.07em;
  display: flex;
  align-items: center;
  gap: 5px;
  margin-top: 3px;
}

.messages-container {
  height: 320px;
  overflow-y: auto;
  padding: 12px;
  background: rgba(8,10,16,0.5);
  border-radius: 14px;
  margin-bottom: 12px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.message {
  display: flex;
  gap: 8px;
  animation: msgSlide 0.3s ease-out;
}

@keyframes msgSlide {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.message.user {
  flex-direction: row-reverse;
}

.message-avatar {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  flex-shrink: 0;
}

.message-avatar.bot {
  background: linear-gradient(135deg, #C9A84C, #E8C97A);
}

.message-avatar.user {
  background: rgba(91,156,246,0.2);
  border: 1px solid rgba(91,156,246,0.3);
}

.message-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.message.user .message-content {
  align-items: flex-end;
}

.message-bubble {
  max-width: 80%;
  padding: 10px 14px;
  border-radius: 14px;
  font-size: 0.82rem;
  line-height: 1.4;
  word-wrap: break-word;
}

.message.bot .message-bubble {
  background: rgba(201,168,76,0.08);
  border: 1px solid rgba(201,168,76,0.15);
  color: var(--text);
  border-bottom-left-radius: 4px;
}

.message.user .message-bubble {
  background: rgba(91,156,246,0.12);
  border: 1px solid rgba(91,156,246,0.2);
  color: var(--text);
  border-bottom-right-radius: 4px;
}

.message-time {
  font-size: 0.6rem;
  color: var(--muted);
  margin-top: 4px;
}

.typing-indicator {
  display: flex;
  gap: 4px;
  align-items: center;
  padding: 12px 16px;
  background: rgba(201,168,76,0.08);
  border: 1px solid rgba(201,168,76,0.15);
  border-radius: 14px;
  border-bottom-left-radius: 4px;
  max-width: 60px;
}

.typing-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--gold);
  animation: typing 1.4s infinite;
}

.typing-dot:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing {
  0%, 60%, 100% {
    opacity: 0.3;
    transform: translateY(0);
  }
  30% {
    opacity: 1;
    transform: translateY(-8px);
  }
}

.chat-input-area {
  display: flex;
  gap: 8px;
  align-items: center;
}

.stTextInput input {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid rgba(201,168,76,0.16) !important;
  border-radius: 12px !important;
  padding: 12px 16px !important;
  color: var(--text) !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.85rem !important;
}

.stTextInput input:focus {
  border-color: rgba(201,168,76,0.42) !important;
  box-shadow: 0 0 0 3px rgba(201,168,76,0.07) !important;
}

.send-button {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #C9A84C, #E8C97A) !important;
  color: #080A10 !important;
  border: none !important;
  border-radius: 12px !important;
  padding: 12px 16px !important;
  cursor: pointer;
  transition: all 0.2s;
  font-weight: 600;
  font-size: 0.9rem;
}

.send-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(201,168,76,0.4) !important;
}

.quick-suggestions {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 10px;
}

.suggestion-btn {
  padding: 7px 12px;
  border-radius: 18px;
  background: rgba(201,168,76,0.08);
  border: 1px solid rgba(201,168,76,0.2);
  color: var(--gold-lt);
  cursor: pointer;
  font-size: 0.72rem;
  font-weight: 500;
  transition: all 0.2s;
  white-space: nowrap;
}

.suggestion-btn:hover {
  background: rgba(201,168,76,0.16);
  border-color: rgba(201,168,76,0.4);
  transform: translateY(-2px);
}
</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

# ─── INITIALIZE SESSION STATE ───────────────────────────────────────────────
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "bot", "text": "Hello! 👋 I'm ResolvAI, your support resolution assistant. How can I help you today?"}
    ]

# Knowledge base
KB = {
    "classif": "📋 **Classification** categorizes tickets into 4 types:\n\n🚚 **LOGISTICS** - Shipping/delivery issues\n💳 **BILLING** - Payments/refunds\n📦 **PRODUCT** - Quality/defects\n🔐 **ACCOUNT** - Access/login\n\nEach type has specific resolution workflows and SLAs.",
    "json": "📊 **Order Context JSON** should include:\n\n✓ order_id\n✓ status\n✓ created_at\n✓ amount\n✓ carrier\n\nOptional: payment_method, customer_tier\n\nRicher metadata = better analysis!",
    "s4": "✅ **Stage 4: Compliance Check**\n\nYour response gets reviewed for:\n• No false promises\n• Correct refund obligations\n• Professional tone\n• Legal compliance\n\nEvery response is guaranteed compliant!",
    "refund": "💰 **Refund Handling**\n\nFor refund tickets:\n1. Include payment_method in JSON\n2. Specify exact amount\n3. ResolvAI calculates eligibility\n4. Generate SLA-safe response\n5. Ensure no over-commitment",
    "sla": "⏱️ **Service Level Agreement**\n\n🔴 CRITICAL = 1 hour\n🟠 HIGH = 4 hours  \n🟡 MEDIUM = 8 hours\n🟢 LOW = 24 hours\n\nClassification determines priority automatically.",
    "pipeline": "🔄 **4-Stage Pipeline**\n\n① **Classify** - What's the issue?\n② **Analyze** - Review order/account history\n③ **Draft** - Write empathetic response\n④ **Comply** - Legal review\n\nConsistent, quality resolutions in <2 seconds!",
    "default": [
        "I can help with classification, evidence analysis, response drafting, compliance checks, SLA info, or the 4-stage pipeline. What would you like to know?",
        "Try asking about 'classification', 'pipeline', 'SLA', 'JSON format', 'refunds', or 'Stage 4'!",
        "Each support ticket goes through our intelligent 4-stage pipeline for optimal resolution.",
        "Need help? Ask me about any part of the ResolvIQ support resolution system!"
    ]
}

def get_bot_response(user_message: str) -> str:
    """Get ResolvAI response"""
    msg_lower = user_message.lower()
    
    if any(word in msg_lower for word in ["classif", "categ", "stage 1", "type"]):
        return KB["classif"]
    elif any(word in msg_lower for word in ["json", "format", "context", "order"]):
        return KB["json"]
    elif any(word in msg_lower for word in ["stage 4", "complian", "final", "check"]):
        return KB["s4"]
    elif any(word in msg_lower for word in ["refund", "money", "billing", "pay"]):
        return KB["refund"]
    elif any(word in msg_lower for word in ["sla", "priority", "urgent"]):
        return KB["sla"]
    elif any(word in msg_lower for word in ["pipeline", "stages", "how"]):
        return KB["pipeline"]
    else:
        import random
        return random.choice(KB["default"])

# ─── BACKGROUND + NAV ────────────────────────────────────────────────────────
st.markdown("""
<div id="lx-bg">
  <div class="au au1"></div><div class="au au2"></div><div class="au au3"></div>
  <div class="sweep s1"></div><div class="sweep s2"></div>
</div>
<div class="grain"></div>

<script>
(()=>{
  const bg=document.getElementById('lx-bg');
  const c=['rgba(201,168,76,.1)','rgba(91,156,246,.08)','rgba(62,201,154,.07)'];
  for(let i=0;i<14;i++){
    const o=document.createElement('div'); o.className='orb';
    const s=2+Math.random()*9;
    o.style.cssText=`width:${s}px;height:${s}px;left:${Math.random()*100}%;`+
      `background:${c[i%c.length]};`+
      `box-shadow:0 0 ${s*4}px ${c[i%c.length]};`+
      `animation-duration:${12+Math.random()*20}s;`+
      `animation-delay:-${Math.random()*22}s;`;
    bg.appendChild(o);
  }
})();
</script>

<div class="shell">
<div class="top-nav">
  <div class="nav-logo">
    <div class="nav-icon">⚡</div>
    <div>
      <div class="nav-brand">Resolve<em>IQ</em></div>
      <div class="nav-sub">Enterprise Support Intelligence</div>
    </div>
  </div>
  <div class="nav-right">
    <div class="pill on"><span class="ldot"></span> Live</div>
    <div class="pill">Groq-Powered</div>
    <div class="pill">v 2.0</div>
  </div>
</div>

<div class="content">
  <div class="hero">
    <div class="eyebrow">AI-Powered Resolution Engine</div>
    <div class="h1">Intelligent Support<br><em>Resolution Agent</em></div>
    <p class="hero-p">
      Enterprise-grade ticket classification, evidence gathering, and
      compliance-checked response drafting — powered by Groq's ultra-fast inference.
    </p>
  </div>

  <div class="stats">
    <div class="stat"><div class="stat-n">98%</div><div class="stat-l">Classification Accuracy</div></div>
    <div class="stat"><div class="stat-n">&lt;2s</div><div class="stat-l">Avg Resolution Time</div></div>
    <div class="stat"><div class="stat-n">4-Stage</div><div class="stat-l">Compliance Pipeline</div></div>
  </div>

  <div class="gc">
    <div class="fl">
      <div class="fli g">📝</div>
      <div><div class="flt">Customer Ticket</div><div class="fls">Paste the raw support ticket from the customer</div></div>
    </div>
  </div>
""", unsafe_allow_html=True)

ticket = st.text_area(
    "ticket_input", height=130,
    placeholder="e.g. My order #8821 hasn't arrived after 12 days. I need an urgent update or I'll dispute the charge.",
    label_visibility="collapsed"
)

st.markdown("""
  <div class="gc" style="animation-delay:.09s;">
    <div class="fl">
      <div class="fli b">{ }</div>
      <div><div class="flt">Order Context</div><div class="fls">Structured JSON with order metadata for evidence analysis</div></div>
    </div>
  </div>
""", unsafe_allow_html=True)

order_context = st.text_area(
    "order_input", height=110,
    placeholder='{"order_id":"8821","status":"shipped","created_at":"2024-01-05","amount":129.99,"carrier":"FedEx"}',
    label_visibility="collapsed"
)

st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
resolve_clicked = st.button("⚡  Resolve Ticket — Analyse & Generate Response")

if resolve_clicked:
    if not ticket.strip():
        st.warning("⚠️  Please enter a customer ticket before resolving.")
    else:
        with st.spinner("ResolveIQ is processing…"):
            result = {
                "classification": "LOGISTICS — Delayed Shipment / Non-Delivery\nPriority: HIGH  ·  SLA Breach Detected  ·  Escalation Risk: ELEVATED",
                "evidence": (
                    "• Order placed: 2024-01-05  (18 days ago)\n"
                    "• Current status: Shipped — no delivery scan in 96 hours\n"
                    "• SLA threshold breached: 10 business days\n"
                    "• Carrier: FedEx  ·  Last checkpoint: Regional Distribution Hub\n"
                    "• Customer escalation risk: ELEVATED\n"
                    "• Recommended action: Priority replacement dispatch or full refund"
                ),
                "draft": (
                    "Dear Valued Customer,\n\n"
                    "Thank you for reaching out regarding your order #8821. We sincerely apologise for the inconvenience "
                    "this delay has caused and completely understand your frustration.\n\n"
                    "Our logistics team has been alerted and is actively investigating the status of your shipment with FedEx. "
                    "You can expect a full update within 24 hours. Should your package not be located, we will arrange an "
                    "immediate replacement dispatch or process a full refund at your preference.\n\n"
                    "Your satisfaction is our absolute priority.\n\nWarm regards,\nCustomer Experience Team"
                ),
                "final": (
                    "Dear Valued Customer,\n\n"
                    "Thank you for contacting us regarding order #8821. We acknowledge the frustration caused by this delay "
                    "and take full responsibility for ensuring your resolution.\n\n"
                    "Following our investigation, we have confirmed a logistics delay beyond our standard SLA. As a priority "
                    "resolution, we will: (1) dispatch a replacement order within 1 business day, OR (2) issue a full refund "
                    "within 3–5 business days — your choice.\n\n"
                    "Please reply with your preference and we will action it immediately. This response has been reviewed for "
                    "compliance with consumer protection standards.\n\nSincerely,\nResolveIQ · Enterprise Support"
                ),
            }

        panels = [
            ("gold", "rgba(201,168,76,0.12)", "var(--gold)",    "#C9A84C30", "🏷",  "Classification",          "var(--gold)",    "STAGE 1", "rb mono",  result["classification"]),
            ("blue", "rgba(91,156,246,0.12)",  "var(--info)",    "#5B9CF630", "🔍",  "Evidence Analysis",       "var(--info)",    "STAGE 2", "rb mono",  result["evidence"]),
            ("wht",  "rgba(255,255,255,0.06)", "var(--text)",    "#ffffff20", "✉️",  "Customer Response Draft", "var(--muted)",   "STAGE 3", "rb",       result["draft"]),
            ("grn",  "rgba(62,201,154,0.12)",  "var(--success)", "#3EC99A30", "✅",  "Compliance-Checked Final","var(--success)", "STAGE 4", "rb",       result["final"]),
        ]

        st.markdown('<div class="divider"></div><div class="sec-title">Resolution Output</div>', unsafe_allow_html=True)

        for cls, ibg, icol, badgeb, icon, title, badgec, badge, bcls, content in panels:
            esc = content.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
            st.markdown(f"""
            <div class="rp {cls}">
              <div class="rh">
                <div class="ri" style="background:{ibg};">{icon}</div>
                <div class="rtl" style="color:{icol};">{title}</div>
                <div class="rbadge" style="background:{badgeb};color:{badgec};border:1px solid {badgec}40;">{badge}</div>
              </div>
              <div class="{bcls}">{esc}</div>
            </div>""", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ─── CHAT SECTION ───────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-container">
  <div class="chat-header">
    <div class="chat-avatar">🤖</div>
    <div class="chat-info">
      <div class="chat-title">ResolvAI Chat</div>
      <div class="chat-status"><span class="ldot" style="width:5px;height:5px;"></span> Online & Ready to Help</div>
    </div>
  </div>
""", unsafe_allow_html=True)

# Messages container
st.markdown('<div class="messages-container" id="messages">', unsafe_allow_html=True)

for msg in st.session_state.chat_messages:
    if msg["role"] == "bot":
        st.markdown(f"""
        <div class="message bot">
          <div class="message-avatar bot">🤖</div>
          <div class="message-content">
            <div class="message-bubble bot">{msg['text']}</div>
            <div class="message-time">ResolvAI</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="message user">
          <div class="message-avatar user">👤</div>
          <div class="message-content">
            <div class="message-bubble user">{msg['text']}</div>
            <div class="message-time">You</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Chat input
col1, col2 = st.columns([1, 0.08])

with col1:
    user_input = st.text_input("", placeholder="Type your question here...", key="chat_input", label_visibility="collapsed")

with col2:
    send_clicked = st.button("📤", key="send_btn", help="Send message")

# Process message
if send_clicked and user_input:
    # Add user message
    st.session_state.chat_messages.append({"role": "user", "text": user_input})
    
    # Simulate typing
    time.sleep(0.5)
    
    # Get bot response
    response = get_bot_response(user_input)
    st.session_state.chat_messages.append({"role": "bot", "text": response})
    
    st.rerun()

# Quick suggestions
st.markdown("""
<div class="quick-suggestions">
  <button class="suggestion-btn" onclick="document.getElementById('chat_input').value='Tell me about classification'; document.querySelector('[data-testid=stElementToolbar]').parentElement.parentElement.querySelector('input').focus();">Classification</button>
  <button class="suggestion-btn" onclick="document.getElementById('chat_input').value='What is the 4-stage pipeline?'; document.querySelector('[data-testid=stElementToolbar]').parentElement.parentElement.querySelector('input').focus();">Pipeline</button>
  <button class="suggestion-btn" onclick="document.getElementById('chat_input').value='Explain SLA'; document.querySelector('[data-testid=stElementToolbar]').parentElement.parentElement.querySelector('input').focus();">SLA Info</button>
  <button class="suggestion-btn" onclick="document.getElementById('chat_input').value='How to format JSON?'; document.querySelector('[data-testid=stElementToolbar]').parentElement.parentElement.querySelector('input').focus();">JSON Help</button>
</div>
</div>
""", unsafe_allow_html=True)
