import anthropic
import time

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

TRANSCRIPT = """
Sarah: Okay let's kick off. We need to finalize the landing page by Friday.
John: I can handle the copy. Need the design from Priya first though.
Priya: I'll send designs by Wednesday EOD.
Sarah: Perfect. Also we need to pick a pricing tier before the investor call next Tuesday.
John: I vote we go with the three-tier model we discussed.
Sarah: Agreed. Priya can you put together a one-pager on that?
Priya: Sure, I'll have it ready by Monday.
Sarah: Great. Let's wrap — next sync Thursday 10am.
"""

def ask(prompt):
    for attempt in range(5):
        try:
            r = client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            return r.content[0].text
        except Exception as e:
            if "overloaded" in str(e).lower():
                print(f"  Server busy, retrying in 10s... (attempt {attempt+1}/5)")
                time.sleep(10)
            else:
                raise e
    raise Exception("Server still overloaded after 5 attempts")

def run_agent():
    print("\n🤖 Running Meeting Agent...\n")

    print("Step 1: Extracting action items...")
    action_items = ask(f"Extract all action items from this transcript. For each list owner, task, deadline as JSON array.\n\n{TRANSCRIPT}")
    print(action_items)

    print("\nStep 2: Generating summary...")
    summary = ask(f"Summarize this meeting in 3 bullet points: key decisions, blockers, next meeting.\n\n{TRANSCRIPT}")
    print(summary)

    print("\nStep 3: Drafting follow-up email...")
    email = ask(f"Write a professional follow-up email based on:\n\nSummary: {summary}\n\nAction items: {action_items}")
    print("\n--- FOLLOW-UP EMAIL ---")
    print(email)
    print("\n✅ Done!")

run_agent()